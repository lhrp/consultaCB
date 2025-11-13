# routes/codigoBarra.py
from flask_restx import Namespace, Resource
from flask import send_file
from io import BytesIO
from routes.consultaAPI import consultaDados

# Namespace substitui o Blueprint e aparece no Swagger automaticamente
codigoBarra = Namespace(name="codigoBarra",
    description="Rotas para consulta de dados e imagens por código de barras",
    path="/codigoBarra"
)

# GET /codigoBarra/<codigoBarra>/dados
@codigoBarra.route("/<string:codigoBarra>/dados")
class BuscarProduto(Resource):
    def get(self, codigoBarra):
        """Consulta os dados do produto pelo código de barras"""
        
        dadosCB = consultaDados(codigoBarra, 1)

        if dadosCB.status_code != 200:
            return dadosCB.json(), dadosCB.status_code

        return dadosCB.json(), dadosCB.status_code


# GET /codigoBarra/<codigoBarra>/imagem
@codigoBarra.route("/<string:codigoBarra>/imagem")
class BuscarImagem(Resource):
    def get(self, codigoBarra):
        """Retorna a imagem associada ao código de barras"""

        dadosImagemCB = consultaDados(codigoBarra, 2)

        if dadosImagemCB.status_code != 200:
            return dadosImagemCB.json(), dadosImagemCB.status_code
        return send_file(
            BytesIO(dadosImagemCB.content),
            mimetype=dadosImagemCB.headers.get("content-type"),
        )