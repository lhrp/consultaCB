import os

from flask import Flask, send_from_directory
from routes import rotasAPI
from flask_restx import Api

def createAPP():
    app = Flask(__name__, template_folder="templates", static_folder="static")

    # Configuração de sessão
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    
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
        from flask import render_template
        return render_template('home.html', title='Consulta de Código de Barras')

    @app.route('/consultar', methods=['POST'])
    def consultar():
        from flask import render_template, request, session, redirect, url_for
        from routes.consultaAPI import consultaDados
        
        barcode = request.form.get('barcode', '').strip()
        
        if barcode and barcode.isdigit() and 8 <= len(barcode) <= 14:
            try:
                # Consulta os dados do produto
                dadosCB = consultaDados(barcode, 1)
                
                if dadosCB and dadosCB.status_code == 200:
                    data = dadosCB.json()
                    
                    # Verifica se a resposta tem a estrutura esperada
                    if data.get('status') == 'success' and 'data' in data:
                        session['resultado'] = data['data']
                        session['barcode'] = barcode
                        session['imagem_url'] = f"/api/codigoBarra/{barcode}/imagem"
                        session['erro'] = None
                    else:
                        session['erro'] = data.get('message', 'Produto não encontrado')
                        session['resultado'] = None
                elif dadosCB:
                    try:
                        error_data = dadosCB.json()
                        session['erro'] = error_data.get('message', f'Erro {dadosCB.status_code}: Não foi possível consultar o código de barras')
                    except Exception:
                        session['erro'] = f'Erro {dadosCB.status_code}: Não foi possível consultar o código de barras'
                    session['resultado'] = None
                else:
                    session['erro'] = 'Erro inesperado ao consultar o código de barras'
                    session['resultado'] = None
                        
            except Exception as e:
                session['erro'] = f'Erro ao processar consulta: {str(e)}'
                session['resultado'] = None
        else:
            session['erro'] = 'Por favor, digite um código de barras válido (8 a 14 dígitos)'
            session['resultado'] = None
        
        # Redireciona para a página de resultado (padrão Post/Redirect/Get)
        return redirect(url_for('resultado'))
    
    @app.route('/resultado')
    def resultado():
        from flask import render_template, session
        
        # Pega os dados da sessão
        resultado = session.pop('resultado', None)
        erro = session.pop('erro', None)
        barcode = session.pop('barcode', None)
        imagem_url = session.pop('imagem_url', None)
        
        return render_template('home.html', 
                             title='Consulta de Código de Barras',
                             resultado=resultado,
                             erro=erro,
                             barcode=barcode,
                             imagem_url=imagem_url)

    return app


if __name__ == '__main__':
    app = createAPP()
    app.run(debug=True, port=5775)
