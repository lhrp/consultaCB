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
    codigoStatus = 0

    ## Buscando os dados base do código de barras
    try:
        dadosCB = requests.get(url)
        dadosCB.raise_for_status()
        return dadosCB
    except requests.exceptions.RequestException as e:
        return dadosCB

        
        
    
    # Consultando os dados
    if tipoConsulta == 1:
        return dadosCB
    # Consultando a imagem
    elif tipoConsulta == 2:
        return {
            "content": dadosCB.content,
            "content_type": dadosCB.headers.get("content-type", "image/jpeg")
        }