# consultaCB
Repositório para testes em criar API usando o Flask ao invés do FastAPI. Permitindo a consulta a uma outra API, via página WEB.
O Swagger está sendo gerado automáticamente com a lib flask-restx

# 📋 **Checklist – API Pública de Consulta de Código de Barras (FastAPI ou Flask)**

---

## 🧩 **Etapa 1 – Planejamento e Estruturação**
- [✅] Criar estrutura de diretórios:
  - `consultaCB/`
     - `app.py`
     - `routes/`
       - `__init__.py`
       - `codigoBarra.py`
       - `log.py`
- [✅] Configurar ambiente virtual
  - Utilizando o próprio `venv` (`python -m venv venv`)
- [✅] Dependências iniciais:
  - `flask`
  - `requests`
  - `python-dotenv`
  - `flask-restx`
- [✅] Gerar requirements.txt
---

## 🧾 **Etapa 2 – Exemplos das Rotas Públicas**
- [✅] Criar rota `GET /codiboBarra/{gtin}/dados` → retorna JSON de dados (Propositalmente mantendo /dados, ao invés de apenas o /gtin)
- [✅] Criar rota `GET /codiboBarra/{gtin}/imagem` → retorna imagem (via `StreamingResponse`)
- [✅] Testar endpoints localmente

---

## 📚 **Etapa 3 – Documentação e Configuração**
- [✅] Habilitar Swagger UI e ReDoc (`/docs` e `/redoc`)
- [✅] Definir título, descrição e versão

---

## 🪵 **Etapa 4 – Consulta de Logs**
- [ ] Criar rota pública `GET /logs` → lista logs registrados (sucessos e falhas)
- [ ] Adicionar filtro opcional por data ou tipo de evento
- [ ] Garantir que a API principal armazene e disponibilize os logs via endpoint próprio

---

## 🌐 **Etapa 5 – Página Web de Consulta**
- [ ] Criar página HTML simples para consulta pública
- [ ] Campo de busca por código de barras
- [ ] Exibir resultado JSON formatado e imagem do produto
- [ ] Adicionar links para Swagger, GitHub e API de Logs
- [ ] Garantir design responsivo e leve (Material Design opcional)

---

## 🚀 **Etapa 6 – Publicação e Deploy**
- [ ] Configurar domínio/subdomínio (`cb.lhrp.com.br`)
- [✅] Configurar envio a VPS com o Github Actions
- [ ] Publicar via aaPanel ou Docker