from funcaoDistancia import alcance
from pacote import Pacote
from listas import *
from constantes import *


class CamadaFisica:

    def __init__(self, x, y, id, cobertura, bateria):
        self._x = x
        self._y = y
        self._id = id
        self._cobertura = cobertura
        self._bateria = bateria
        self._vizinhos = []
        self._pacotesEnviados = []
        self._pacotesRecebidos = []
        self._pacotesSalvos = []

    # Descobre nós vizihos e add na lista
    def encontraVizinhos(self):
        if(self._bateria == 0):
            print(RED, "\nID:", self._id,
                  "Bateria descarregada, impossibilitado de encontrar vizinhos", RESET)
        else:
            for no in nos:
                # se o nó não for ele mesmo e se puder alcançá-lo
                if((no._id != self._id) and (alcance(self._x, self._y, self._cobertura, no._camadaRede._camadaEnlace._camadaFisica._x, no._camadaRede._camadaEnlace._camadaFisica._y))):
                    # se o não estiver na lista de vizinhos
                    if(no not in self._vizinhos):
                        # add a lista de vizinhos
                        self._vizinhos.append(no)
            self._bateria -= 1

    # Recebe pacote
    def recebePacote(self, pacote):
        if(self._bateria == 0):
            print(RED, "\nID:", self._id,
                  "Bateria descarregada, impossibilitado de receber pacote", RESET)
            '''
            del nos[:]
            del indicesParaEnvio[:]
            del indicesParaVer[:]
            for no in nos:
                if(no._id == self._id):
                    nos.remove(no)
                    if(len(indicesParaEnvio) != 0):
                        print(indicesParaEnvio.pop())
                    elif(len(indicesParaVer) != 0):
                        print(indicesParaVer.pop())
            '''
        else:
            # Add a lista global
            indicesParaVer.append(self._id)
            # Add a lista local de recebidos
            self._pacotesRecebidos.append(pacote)
            self._bateria -= 1

    # Envia pacote
    def enviaPacote(self):
        if(self._bateria == 0):
            print(RED, "\nID:", self._id,
                  "Bateria descarregada, impossibilitado de enviar pacote", RESET)
            '''
            del nos[:]
            del indicesParaEnvio[:]
            del indicesParaVer[:]
            for no in nos:
                if(no._id == self._id):
                    nos.remove(no)
                    if(len(indicesParaEnvio) != 0):
                        print(indicesParaEnvio.pop())
                    elif(len(indicesParaVer) != 0):
                        print(indicesParaVer.pop())
            '''
        else:
            # Encontra e add os vizinhos na lista
            self.encontraVizinhos()
            # Percorre vizinhos
            for no in self._vizinhos:
                # Envia pacote aos vizinhos
                no._camadaRede._camadaEnlace._camadaFisica.recebePacote(
                    self._pacotesEnviados[0])
            # Add o pacote na lista de salvos
            self._pacotesSalvos.append(self._pacotesEnviados.pop(0))
            self._bateria -= 1
