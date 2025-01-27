from abc import abstractmethod
import logging
import string
from urllib.error import URLError
import urllib.request

class RequisicoesAPI():

    @abstractmethod
    def __init__(self, url):
        self.url = url
    
    def executa_requisicao(self) -> bool:
        requisicao_ok: bool
        try:
            with urllib.request.urlopen(self.url) as f:
                data = f.read()
            self.data = data
            requisicao_ok =  True
        except URLError as e:
            msg_erro: string
            if hasattr(e, 'reason'):
                msg_erro = 'url: ' + self.url + " || Falha em encontrar o servidor, razão: " + e.reason
            elif hasattr(e, 'code'):
                msg_erro = 'url: ' + self.url + 'O servidor não conseguiu completar a requisição, código de erro: ' + e.code
            requisicao_ok = False
            logging.error(msg_erro)
        
        return requisicao_ok

    #Transforma dados da requisição para objeto (a depender da estrutura)  
    @abstractmethod
    def trata_dados(self) -> bool:
        pass


