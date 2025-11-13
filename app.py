import os

from flask import Flask, send_from_directory
from routes import rotasAPI
from flask_restx import Api

def createAPP():
    app = Flask(__name__, template_folder="templates", static_folder="static")

    app.config['JSON_AS_ASCII'] = False
    app.json.ensure_ascii = False

    app.config['RESTX_JSON'] = {'ensure_ascii': False,
                                'indent': 4
                                }

    # Gerando o Swagger UI automático
    docAPI = Api(
        app,
        prefix="/api",
        title="Consulta de Código de Barras",
        version="1.1",
        doc="/api/docs",  # Rota para acessar o Swagger UI
        description="""Documentação automática via Flask-RESTX
        Atualmente:

        - Consulta de informações de produtos via código de barras
          - Utiliza a base de dados do Open Food Facts e de outros sites via scraping
          - Caso o produto não seja encontrado, retorna uma mensagem informando que não foi localizado nas fontes de dados utilizadas
          - Se o produto for localizado, grava suas informações em um banco de dados local para consultas futuras
          - Retorna os dados:
            - Código de barras
            - Nome do produto
            - Marca
            - Imagem do produto (Em rota específica, se disponível)
        """,
    )

    for rota in rotasAPI: 
        """
        Loop para registrar todas as rotas do pacote "routes"
        Entre aspas, substituindo o trecho abaixo em cada rota:
        url_prefix="/codigoBarra"
        """
        #app.register_blueprint(rota, url_prefix=f'/{rota.name}')
        docAPI.add_namespace(rota)

    @app.route("/favicon.ico")
    def favicon():
        return send_from_directory(
            os.path.join(app.root_path, "static", "img"),
            "favicon.svg",
            mimetype="image/svg+xml"
        )
    
    @app.route('/')
    def home():
        return "Hello, World!"

    return app


if __name__ == '__main__':
    app = createAPP()
    app.run(debug=True, port=5775)
