from camadaFisica import CamadaFisica
from camadaEnlace import CamadaEnlace
from listas import *
from pacote import Pacote
from cabecalhos import Cabecalho
from rota import Rota
import random
from constantes import *


class CamadaRede:
    def __init__(self, camadaEnlace):
        self._camadaEnlace = camadaEnlace
        self._listaPacotes = []
        self._listaRREQS = []
        self._ListasRotasEspera = []
        self._rotas = []

    # Inicia o processo de descoberta de rota
    def enviaRREQ(self, macDestino):
        # Inicializa uma sequencia e coloca o seu ID como primeiro
        # add o proprio endereço da camada fisica no pacote
        sequencia = []
        sequencia.append(self._camadaEnlace._camadaFisica._id)
        # numero do pacote
        sequenNum = random.randint(1, 4412349)
        self._listaRREQS.append(sequenNum)
        # Cria um pacote e inseri o cabeçalho da camada de rede
        cabecalho = Cabecalho(
            "REDE", self._camadaEnlace._camadaFisica._id, macDestino, -1, 0, sequenNum, sequencia)
        pacote = Pacote("", 1)
        pacote.addCabecalho(cabecalho)
        msg = "Enviando um RREQ"
        # exibe pacote criado
        # TROQUEI CABEÇALHO._SEQUENNUM por sequenNUM
        self.exibePacote(
            msg, self._camadaEnlace._camadaFisica._id, macDestino, sequenNum)
        # add a camada de enlace o pacote
        self._camadaEnlace.addPacote(pacote, -1)

    # Envia pacote de resposta de rota (pacote de controle)
    def enviaRREP(self, macDestino, sequencia, rota):
        # Cria um pacote e inseri o cabeçalho da camada de rede
        cabecalho = Cabecalho(
            "REDE", self._camadaEnlace._camadaFisica._id, macDestino, -1, 1, -1, sequencia)
        pacote = Pacote(rota, 1)
        pacote.addCabecalho(cabecalho)
        msg = "Enviando um RREP com destino para ID:"
        # exibe pacote criado
        self.exibePacote(
            msg, self._camadaEnlace._camadaFisica._id, macDestino, rota)
        # Define a rota requisitada
        print("rota", rota)
        for indice, mac in enumerate(cabecalho._sequenList):
            if(mac == self._camadaEnlace._camadaFisica._id):
                proximoDestino = cabecalho._sequenList[indice+1]
                proximoPacote = pacote
                self._camadaEnlace.addPacote(proximoPacote, proximoDestino)
                break

    # Recebe e trata o pacote recebido na camada de rede
    def recebePacote(self):
        # Chama a função de tratar pacote recebido na camada de enlace
        self._camadaEnlace.recebePacote()
        # Verifica se tem pacotes recebidos
        if(self._camadaEnlace._pacotesLidos != []):
            pacote = self._camadaEnlace._pacotesLidos.pop(0)
            cabecalho = pacote.getCabecalhoRede()
            # Se o pacote for recebido for de dados
            if(cabecalho._requisicao == -1):
                # Verifica se o pacote é para aquele nó
                if(cabecalho._macDestino == self._camadaEnlace._camadaFisica._id):
                    msg = "Pacote de dados"
                    self.exibePacote(
                        msg, self._camadaEnlace._camadaFisica._id, pacote._dados, cabecalho._sequenNum)
                else:
                    msg = "Chegada de pacote de dados mas não é pra mim "
                    self.exibePacote(msg, self._camadaEnlace._camadaFisica._id,
                                     cabecalho._macDestino, cabecalho._sequenNum)
                    msg_2 = "Enviando pacote de dados para o nó seguinte"
                    self.exibePacote(msg_2, self._camadaEnlace._camadaFisica._id,
                                     cabecalho._macDestino, cabecalho._sequenNum)  # !!!!!!
                    for indice, mac in enumerate(pacote._cabecalhos[0]._sequenList):
                        if(mac == self._camadaEnlace._camadaFisica._id):
                            proximoDestino = cabecalho._sequenList[indice-1]
                            break
                    pacote._cabecalhos.pop(1)
                    self._camadaEnlace.addPacote(pacote, proximoDestino)
                    indicesParaEnvio.append(
                        self._camadaEnlace._camadaFisica._id)

            # Se o pacote for recebido for um RREQ
            elif(cabecalho._requisicao == 0):
                msg = "Chegada de pacote RREQ"
                self.exibePacote(msg, self._camadaEnlace._camadaFisica._id,
                                 cabecalho._macDestino, cabecalho._sequenNum)
                # Verifica se esse RREQ já foi recebido pelo nó
                if(not cabecalho._sequenNum in self._listaRREQS):
                    self._listaRREQS.append(cabecalho._sequenNum)
                    cabecalho._sequenList.append(
                        self._camadaEnlace._camadaFisica._id)

                    # Verifica se o RREQ é para o nó
                    if(cabecalho._macDestino == self._camadaEnlace._camadaFisica._id):
                        msg = "Eu sou o destino do RREQ"
                        self.exibePacote(
                            msg, self._camadaEnlace._camadaFisica._id, cabecalho._macDestino, cabecalho._sequenNum)
                        rota = cabecalho._sequenList
                        macDestino = rota[0]
                        sequenParaFonte = rota
                        sequenParaFonte.reverse()
                        self.enviaRREP(macDestino, sequenParaFonte, rota)
                        indicesParaEnvio.append(
                            self._camadaEnlace._camadaFisica._id)
                    else:
                        print("ID:", self._camadaEnlace._camadaFisica._id,
                              "Eu não sou o destino do RREQ")
                        self._camadaEnlace.addPacote(pacote, -1)
                        indicesParaEnvio.append(
                            self._camadaEnlace._camadaFisica._id)

                else:
                    msg = "Ja tenho esse RREQ"
                    self.exibePacote(msg, self._camadaEnlace._camadaFisica._id,
                                     cabecalho._macDestino, cabecalho._sequenNum)
            # Se o pacote for recebido for um RREP
            elif(cabecalho._requisicao == 1):
                destino = cabecalho._macDestino
                msg = "Chegada de pacote RREP: "
                self.exibePacote(msg, self._camadaEnlace._camadaFisica._id,
                                 cabecalho._macDestino, cabecalho._sequenList)
                # Verifica se o RREP é para o nó
                if(destino == self._camadaEnlace._camadaFisica._id):
                    msg = "Eu sou o destino do RREP"
                    self.exibePacote(msg, self._camadaEnlace._camadaFisica._id,
                                     cabecalho._macDestino,  cabecalho._sequenNum)
                    msg_2 = "Enviando dados"
                    self.exibePacote(msg_2, self._camadaEnlace._camadaFisica._id,
                                     cabecalho._macDestino, cabecalho._sequenNum)
                    sequenParaFonte = pacote._dados
                    rota = Rota(cabecalho._sequenList[0], sequenParaFonte)
                    self._rotas.append(rota)
                    indicesParaEnvio.append(
                        self._camadaEnlace._camadaFisica._id)

                else:
                    msg = "Eu não sou o destino do RREP"
                    self.exibePacote(msg, self._camadaEnlace._camadaFisica._id,
                                     cabecalho._macDestino,  cabecalho._sequenNum)
                    for indice, mac in enumerate(cabecalho._sequenList):
                        if(mac == self._camadaEnlace._camadaFisica._id):
                            proximoDestino = cabecalho._sequenList[indice+1]
                            proximoPacote = pacote
                            pacote._cabecalhos.pop(1)
                            self._camadaEnlace.addPacote(
                                proximoPacote, proximoDestino)
                            indicesParaEnvio.append(
                                self._camadaEnlace._camadaFisica._id)
                            break

    # Cria um pacote novo e adicionar o cabeçalho de rede

    def addPacote(self, macDestino, mensage, tempo):
        pacote = Pacote(mensage, tempo)
        cabecalho = Cabecalho(
            "REDE", self._camadaEnlace._camadaFisica._id, macDestino, -1, -1, -1, None)
        pacote.addCabecalho(cabecalho)
        self._listaPacotes.append(pacote)

    # Envia os pacotes da camada de rede
    def enviaPacote(self):
        # Verifica pacotes a serem enviados
        if(self._listaPacotes != []):
            pacote = self._listaPacotes[0]
            cabecalho = pacote.getCabecalhoRede()
            sequencia = None

            # Para cada rota
            for rota in self._rotas:
                if(rota._destino == pacote._cabecalhos[0]._macDestino):
                    sequencia = rota._sequencia
                    if (pacote._cabecalhos[0]._macDestino in self._ListasRotasEspera):
                        self._ListasRotasEspera.remove(
                            pacote._cabecalhos[0]._macDestino)

            # Se a rota para o destino é conhecida
            if(sequencia != None):
                '''
                print("sequencia", sequencia)
                nos_ativos = [
                    nos[i]._camadaRede._camadaEnlace._camadaFisica._id for i in range(len(nos))]
                print(list(set(sequencia) - set(nos_ativos)))
                nos_mortos = list(set(sequencia) - set(nos_ativos))
                if (nos_mortos in sequencia):
                    self._rotas = []
                    self._ListasRotasEspera.append(
                        pacote._cabecalhos[0]._macDestino)
                    self.enviaRREQ(pacote._cabecalhos[0]._macDestino)
                '''
                pacote.atualizaSequen(sequencia)
                self._listaPacotes.pop(0)

                for indice, mac in enumerate(pacote._cabecalhos[0]._sequenList):
                    if(mac == self._camadaEnlace._camadaFisica._id):
                        proximoDestino = cabecalho._sequenList[indice-1]
                        print("proximoDestino: ", proximoDestino)
                        break

                self._camadaEnlace.addPacote(pacote, proximoDestino)
                indicesParaEnvio.append(self._camadaEnlace._camadaFisica._id)

            elif(not cabecalho._macDestino in self._ListasRotasEspera):
                self._ListasRotasEspera.append(
                    pacote._cabecalhos[0]._macDestino)
                self.enviaRREQ(pacote._cabecalhos[0]._macDestino)

        # Chama a função de enviar pacotes da camada de enlace
        self._camadaEnlace.enviaPacote()

    def exibePacote(self, mensagem,  id, macDestino, NumSequencia, rota=''):
        if(mensagem == "Pacote de dados"):
            print(GREEN, "\nID:", id, "Mensagem:", macDestino, RESET)
        elif(mensagem == "Enviando um RREQ"):
            print("ID:", id, mensagem, "para ID:", macDestino,
                  "com NumSequencia:", NumSequencia)
        elif(mensagem == "Chegada de pacote RREQ"):
            print("ID:", id, mensagem, "com:", NumSequencia)
        elif(mensagem == "Eu sou o destino do RREQ"):
            print(GREEN, "\rID:", id, mensagem, RESET)
        elif(mensagem == "Ja tenho esse RREQ"):
            print("ID:", id, mensagem)
        elif(mensagem == "Enviando um RREP com destino para ID:"):
            print("ID:", id, mensagem, macDestino, rota)  # ARRUMAR
        else:
            print("ID:", id, mensagem, "MacDestino", macDestino)
