class Cabecalho:

    def __init__(self, camada, macOrigem, macDestino, numero, requesicao, sequenNum, sequenList):
        
        #Cabeçario para a camada de enlace 
        if(camada == "ENLACE"):
            self._camada = "ENLACE"
            self._macOrigem = macOrigem
            self._macDestino = macDestino
            self._numero = numero

        #Cabeçario para a camada de rede  
        if( camada == "REDE"):
            self._camada = "REDE"
            self._macDestino = macDestino
            #identifica tipos de pacote de controle, requisição 
            self._requesicao = requesicao
            # numero do pacote
            self._sequenNum = sequenNum
            # endereço mac da camada fisica
            self._sequenList = sequenList