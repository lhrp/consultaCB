# consultaCB
Repositório para testes em criar API usando o Flask ao invés do FastAPI. Permitindo a consulta a uma outra API, via página WEB.
O Swagger está sendo gerado automáticamente com a lib flask-restx

# 📋 **Checklist – API Pública de Consulta de Código de Barras (FastAPI ou Flask)**

---

## 🧩 **Etapa 1 – Planejamento e Estruturação** ✅ 
- [x] Criar estrutura de diretórios:
- `consultaCB/`
  - `app.py`
    - `routes/`
      - `__init__.py`
      - `codigoBarra.py`
      - `consultaAPI.py`
      - `log.py`

- [x] Configurar ambiente virtual
- Utilizando o próprio `venv` (`python -m venv venv`)

- [x] Dependências iniciais:
- `flask`
- `requests`
- `python-dotenv`
- `flask-restx`

- [x] Gerar requirements.txt

---

## 🧾 **Etapa 2 – Exemplos das Rotas Públicas** ✅
- [x] Criar rota `GET /codiboBarra/{gtin}/dados` → retorna JSON de dados (Propositalmente mantendo /dados, ao invés de apenas o /gtin)
- [x] Criar rota `GET /codiboBarra/{gtin}/imagem` → retorna imagem (via `StreamingResponse`)
- [x] Testar endpoints localmente

---

## 📚 **Etapa 3 – Documentação e Configuração** ✅
- [x] Habilitar Swagger UI e ReDoc (`/docs` e `/redoc`)
- [x] Definir título, descrição e versão

---

## 🌐 **Etapa 4 – Página Web de Consulta**
- [x] Criar página HTML simples para consulta pública
- [x] Campo de busca por código de barras
- [x] Exibir resultado JSON formatado e imagem do produto
- [x] Adicionar links para Swagger, GitHub
- [ ] Página para a consulta dos logs gerados
- [ ] Divulgar

---

## 🚀 **Etapa 5 – Publicação e Deploy** ✅
- [x] Configurar domínio/subdomínio (`https://consultacb.lhrp.com.br`)
- [x] Configurar envio para VPS com o Github Actions
- [x] Publicar via aaPanel ou Docker

---

## 🪵 **Etapa 6 – Consulta de Logs**
- [ ] Criar rota pública `GET /logs` → lista logs registrados (sucessos e falhas)
- [ ] Adicionar filtro opcional por data ou tipo de evento
- [ ] Garantir que a API principal armazene e disponibilize os logs via endpoint próprio