import os
import requests
from dotenv import load_dotenv
load_dotenv()

CONSULTADADOSCB = os.getenv("CONSULTADADOSCB")
CONSULTAIMAGEMCB = os.getenv("CONSULTAIMAGEMCB")


def consultaDados(codigoBarra: str, tipoConsulta:int):
    """Consulta uma API externa para obter dados do código de barras fornecido.

    Args:
        codigoBarra (str): O código de barras a ser consultado.
        tipoConsulta (int): O tipo de consulta a ser realizada.
        1 = Dados do Produto
        2 = Imagem do Produto   
    
    """
    url = f"{CONSULTADADOSCB if tipoConsulta == 1 else CONSULTAIMAGEMCB}{codigoBarra}"
    
    ## Buscando os dados base do código de barras
    try:
        dadosCB = requests.get(url, timeout=10)
        dadosCB.raise_for_status()
        return dadosCB
    except requests.exceptions.RequestException as e:
        # Criando uma resposta simulada para erros
        from unittest.mock import Mock
        
        error_response = Mock()
        error_response.status_code = 503
        error_response.content = b''
        error_response.headers = {}
        
        if isinstance(e, requests.exceptions.ConnectionError):
            error_message = "Não foi possível conectar à API externa"
        elif isinstance(e, requests.exceptions.Timeout):
            error_message = "Tempo de resposta da API esgotado"
        else:
            error_message = f"Erro ao consultar API: {str(e)}"
        
        error_response.json = lambda: {
            "status": "error",
            "message": error_message
        }
        
        return error_response