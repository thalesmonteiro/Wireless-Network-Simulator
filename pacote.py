from cabecalhos import Cabecalho


class Pacote:

    def __init__(self, mensagem, duracao):
        self._id = -1
        self._dados = mensagem
        self._duracao = duracao
        self._cabecalhos = []

    # Retorna um pacote criado
    @staticmethod
    def criaPacote(mensage, duracao):
        return Package(mensage, duracao)

    # Obtem cabeçalho da camada de rede
    def getCabecalhoRede(self):
        for cabecalho in self._cabecalhos:
            if(cabecalho._camada == "REDE"):
                return cabecalho

    # Obtem cabeçalho da camada de enlace
    def getCabecalhoEnlace(self):
        for cabecalho in self._cabecalhos:
            if(cabecalho._camada == "ENLACE"):
                return cabecalho

    # Adiciona novos cabeçalhos na lista
    def addCabecalho(self, cabecalho):
        self._cabecalhos.append(cabecalho)

    # Exibe as informações do pacote
    def ExibeInfoPacote(self):
        print("Dados: ", self._dados)

    # Atualiza sequencia
    def atualizaSequen(self, sequencia):
        for cabecalho in self._cabecalhos:
            if(cabecalho._camada == "REDE"):
                cabecalho._sequenList = sequencia
