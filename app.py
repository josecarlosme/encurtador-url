import os, sqlite3, string, secrets
from urllib.parse import urlparse
from flask import Flask, request, redirect, render_template, abort
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

DB = os.environ.get("DB_PATH", "urls.db")
ALPHABET = string.ascii_letters + string.digits


def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT UNIQUE NOT NULL,
                original_url TEXT NOT NULL,
                clicks INTEGER DEFAULT 0,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )""")


def valid_url(url):
    p = urlparse(url)
    return p.scheme in ("http", "https") and bool(p.netloc)


def new_code(size=6):
    return "".join(secrets.choice(ALPHABET) for _ in range(size))


@app.route("/", methods=["GET", "POST"])
def index():
    short_url = error = None
    if request.method == "POST":
        url = request.form.get("url", "").strip()
        if url and not url.startswith(("http://", "https://")):
            url = "https://" + url
        if not valid_url(url):
            error = "URL inválida. Confira o endereço e tente novamente."
        else:
            with get_db() as conn:
                while True:
                    code = new_code()
                    exists = conn.execute(
                        "SELECT 1 FROM urls WHERE code = ?", (code,)).fetchone()
                    if not exists:
                        break
                conn.execute(
                    "INSERT INTO urls (code, original_url) VALUES (?, ?)",
                    (code, url))
            short_url = request.host_url + code
    return render_template("index.html", short_url=short_url, error=error)


@app.route("/<code>")
def go(code):
    with get_db() as conn:
        row = conn.execute(
            "SELECT original_url FROM urls WHERE code = ?", (code,)).fetchone()
        if row is None:
            abort(404)
        conn.execute("UPDATE urls SET clicks = clicks + 1 WHERE code = ?", (code,))
    return redirect(row["original_url"])


init_db()

if __name__ == "__main__":
    app.run(debug=True)