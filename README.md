# 🔗 Encurtador de URL

Aplicação web que transforma links longos em links curtos e redireciona o usuário para o endereço original. Projeto desenvolvido para praticar backend, banco de dados e deploy.

🌐 **Projeto no ar:** [(https://encurtador-url-z6gp.onrender.com)]

> ⚠️ Hospedado em plano gratuito: a primeira visita pode demorar alguns segundos para carregar, e os links criados podem ser apagados quando o serviço reinicia.

## Funcionalidades

- Encurtamento de URLs com código aleatório de 6 caracteres
- Redirecionamento automático para a URL original
- Validação de entrada (aceita apenas endereços `http` e `https`)
- Contagem de cliques de cada link salva no banco de dados
- Tratamento de links inexistentes (erro 404)

## Tecnologias

- **Python** e **Flask** (backend e rotas)
- **SQLite** (armazenamento dos links)
- **HTML e CSS** (interface)
- **Gunicorn** (servidor de produção)
- **Git/GitHub** (versionamento) e **Render** (deploy)

## Como funciona

1. O usuário cola uma URL no formulário.
2. O sistema valida o endereço e gera um código único com a biblioteca `secrets`, verificando no banco se ele já existe.
3. A URL original e o código são salvos na tabela `urls`.
4. Ao acessar `/<código>`, o sistema busca a URL original, incrementa o contador de cliques e redireciona.

## Como rodar localmente

```bash
# clonar o repositório
git clone https://github.com/josecarlosme/encurtador-url.git
cd encurtador-url

# criar e ativar o ambiente virtual
python -m venv venv
venv\Scripts\activate        # Mac/Linux: source venv/bin/activate

# instalar dependências
pip install -r requirements.txt

# rodar a aplicação
python app.py
```

Acesse `http://127.0.0.1:5000` no navegador.

## Estrutura do projeto

```
encurtador-url/
├── app.py              # rotas, regras de negócio e banco de dados
├── requirements.txt    # dependências
├── templates/
│   └── index.html      # interface
└── README.md
```

## Próximos passos

- [ ] Página de estatísticas por link
- [ ] Código personalizado escolhido pelo usuário
- [ ] Limite de requisições por IP
- [ ] Testes automatizados com `pytest`
- [ ] Migração do SQLite para PostgreSQL

## Autor

**José Carlos** · [LinkedIn](https://www.linkedin.com/in/jose-carlos82a35b202) · [GitHub](https://github.com/josecarlosme)
