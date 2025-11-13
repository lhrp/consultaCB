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



## ⚙️ **Etapa 2 – Integração com a API Interna**
- [ ] Criar módulo `service_interno.py` para consumo da API principal
- [ ] Definir variáveis de ambiente (`URL_API_INTERNA`, `API_KEY_INTERNA`, etc.)
- [ ] Testar consumo com um código de barras real
- [ ] Implementar tratamento de erros e respostas HTTP adequadas (404, 502, etc.)

---

## 🧾 **Etapa 3 – Criação das Rotas Públicas**
- [ ] Criar rota `GET /cb/{gtin}` → retorna JSON de dados
- [ ] Criar rota `GET /cb/{gtin}/imagem` → retorna imagem (via `StreamingResponse`)
- [ ] Implementar *caching* leve (ex: `lru_cache` ou Redis)
- [ ] Testar endpoints localmente

---

## 🪵 **Etapa 4 – Registro e Consulta de Logs Públicos**
- [ ] Criar módulo `service_log.py` para envio de logs à API principal
- [ ] Definir formato padrão dos logs (ex: data, rota, status, tempo, erro/sucesso)
- [ ] Implementar log automático em cada requisição (via `middleware` ou decorator)
- [ ] Criar rota pública `GET /logs` → lista logs registrados (sucessos e falhas)
- [ ] Adicionar filtro opcional por data ou tipo de evento
- [ ] Garantir que a API principal armazene e disponibilize os logs via endpoint próprio

---

## 📚 **Etapa 5 – Documentação e Configuração**
- [ ] Habilitar Swagger UI e ReDoc (`/docs` e `/redoc`)
- [ ] Definir título, descrição e versão no `FastAPI()`
- [ ] Adicionar exemplos de resposta nos `response_model`
- [ ] Configurar `CORS` para permitir consumo público
- [ ] Criar README detalhado (instalação, uso, endpoints, exemplos)

---

## 🌐 **Etapa 6 – Página Web de Consulta**
- [ ] Criar página HTML simples para consulta pública
- [ ] Campo de busca por código de barras
- [ ] Exibir resultado JSON formatado e imagem do produto
- [ ] Adicionar links para Swagger, GitHub e API de Logs
- [ ] Garantir design responsivo e leve (Material Design opcional)

---

## 🚀 **Etapa 7 – Publicação e Deploy**
- [ ] Configurar domínio/subdomínio (`cb.lhrp.com.br`)
- [ ] Deploy com `uvicorn` via aaPanel ou Docker
- [ ] Configurar HTTPS e logs de sistema
- [ ] Testar endpoints externos e page de consulta
- [ ] Publicar link público do Swagger e página de exemplo

---

## 📈 **Etapa 8 – Futuras Evoluções**
- [ ] Implementar cache persistente (Redis, SQLite local ou Mongo)
- [ ] Criar dashboard interno com estatísticas de uso (requisições, erros, etc.)
- [ ] Adicionar rota `/status` para monitoramento
- [ ] Suporte a busca por nome, marca ou categoria
- [ ] Habilitar chave opcional para acesso privado estendido
