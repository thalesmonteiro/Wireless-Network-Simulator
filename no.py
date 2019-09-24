from camadaEnlace import CamadaEnlace
from camadaFisica import CamadaFisica
from camadaRede import CamadaRede
from listas import *
from pacote import Pacote 
from cabecalhos import Cabecalho
from constantes import *

class No:
    def __init__(self, id, cobertura, x, y, bateria):
        self._id = id
        #Adds a si mesmo na lista global de nós
        nos.append(self)
        self._camadaRede = CamadaRede(CamadaEnlace(CamadaFisica(x, y, id, cobertura,bateria)))
    #Criar pacote
    def criarPacote(self, duracao, macDestino, mensagem):
        self._camadaRede.addPacote(macDestino, mensagem, duracao)
        self.exibePacote(self._camadaRede._camadaEnlace._camadaFisica._id, macDestino, mensagem)
    #Exibe pacote criado
    def exibePacote(self, macDestino, id, mensagem):
        print("Pacote criado \nID:", id ,"Mensagem: ", mensagem, " Destino:", macDestino)  

        