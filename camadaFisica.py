from funcaoDistancia import alcance
from pacote import Pacote
from lists import nos
from lists import indicesParaVer
from constantes import *

class CamadaFisica:

    def __init__(self, x, y, id, cobertura):
        self._x = x
        self._y = y
        self._id = id
        self._cobertura = cobertura
        self._vizinhos = []
        self._pacotesEnviados = []
        self._pacotesRecebidos = []
        self._pacotesSalvos = []

    #Descobre nós vizihos e add na lista
    def encontraVizinhos(self):
        for no in nos:
            #se o nó não for ele mesmo e se puder alcançá-lo
            if((no._id != self._id) and (alcance(self._x, self._y, self._cobertura, no._camadaRede._camadaEnlace._camadaFisica._x, no._camadaRede._camadaEnlace._camadaFisica._y))):
                # se o não estiver na lista de vizinhos
                if(no not in self._vizinhos):
                    #add a lista de vizinhos
                    self._vizinhos.append(no) 
                    
    #Recebe pacote
    def recebePacote(self, pacote):
        #Add a lista global
        indicesParaVer.append(self._id)
        #Add a lista local de recebidos
        self._pacotesRecebidos.append(pacote)
        

    #Envia pacote
    def enviaPacote(self):
        #Encontra e add os vizinhos na lista 
        self.encontraVizinhos()
        #Percorre vizinhos
        for no in self._vizinhos:
            #Envia pacote aos vizinhos
            no._camadaRede._camadaEnlace._camadaFisica.recebePacote(self._pacotesEnviados[0])
        #Add o pacote na lista de salvos
        self._pacotesSalvos.append(self._pacotesEnviados.pop(0))

