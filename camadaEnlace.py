from camadaFisica import CamadaFisica
from listas import *
from pacote import Pacote
from cabecalhos import Cabecalho
from random import randint
from constantes import *


class CamadaEnlace:

    def __init__(self, camadaFisica):
        self._backoff = 0
        self._acessoAoMeio = True
        self._camadaFisica = camadaFisica
        self._pacotesLidos = []

    # Envia os pacotes para outros nós
    def enviaPacote(self):
        self._acessoAoMeio = self.acessoAoMeio()
        # Se o meio está livre
        if(self._acessoAoMeio == True):
            # Se a lista de pacotes para envio da camada da física não está vazia
            if(self._camadaFisica._pacotesEnviados != []):
                # Se o nó não está em backoff
                if(self._backoff == 0):
                    # Envia pacote pela camada fisica
                    self._camadaFisica.enviaPacote()
                # Caso contrário
                else:
                    # Adiciona o no na lista global de proximo a enviar
                    proximoAEnviar.append(self._camadaFisica._id)
                    # Subtrai backoff
                    self._backoff = (self._backoff - 1)

        # Caso o meio esteja ocupado o host entrará em backoff
        else:
            # Se a lista de pacotes para envio da camada da física não está vazia
            if(self._camadaFisica._pacotesEnviados != []):
                # Se o nó não está em backoff, deve estar
                if(self._backoff == 0):
                    # coloca no em backoff
                    self._backoff = randint(1, 8)
                    # Exibe backoff
                    self.exibeBackoff(self._camadaFisica._id, self._backoff)
                    # Adiciona o no na lista global de proximo a envir
                    proximoAEnviar.append(self._camadaFisica._id)

    # Exibe backoff
    def exibeBackoff(self, id, backoff):
        print(YELLOW, "\rID:", id, "No entrou em Backoff  valor:",
              backoff, RESET, end="\n\n")

    # Pacotes recebidos
    def recebePacote(self):
        # Se mais de um pacote chegou no instante, detecta colisão
        if(len(self._camadaFisica._pacotesRecebidos) > 1):
            self._camadaFisica._pacotesRecebidos.clear()
            self.exibeColisao(self._camadaFisica._id)
        # Caso não haja colisão
        else:
            # Se existe pacote para receber
            if(len(self._camadaFisica._pacotesRecebidos) == 1):
                pacote = self._camadaFisica._pacotesRecebidos.pop(0)
                cabecalho = pacote.getCabecalhoEnlace()
                # Se o pacote é para aquele nó
                if(cabecalho._macDestino == self._camadaFisica._id):
                    # Adiciona o pacote a lista de lidos
                    self._pacotesLidos.append(pacote)
                elif(cabecalho._macDestino == -1):
                    # Adiciona o pacote a lista de lidos
                    self._pacotesLidos.append(pacote)

    # Exibe colisão
    def exibeColisao(self, id):
        print(RED, "\rID:", id, "Houve Colisão neste nó", RESET)

    # Detecta o meio

    def acessoAoMeio(self):
        # Se a lista de pacotes recebidos for vazia
        if(self._camadaFisica._pacotesRecebidos == []):
            # Então o meio vai estar livre
            return True
        else:
            # Então o meio vai estar ocupado
            return False

    # Add pacote na camada fisica
    def addPacote(self, pacote, macDestino):
        cabecalho = Cabecalho(
            "ENLACE", self._camadaFisica._id, macDestino, 0, -1, -1, -1)
        pacote.addCabecalho(cabecalho)
        self._camadaFisica._pacotesEnviados.append(pacote)
