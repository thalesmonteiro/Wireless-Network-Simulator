from no import No
from listas import *
from pacote import Pacote
from camadaRede import CamadaRede
import random
from graficos import criaGraficos
from constantes import *

#No(id, cobertura, x, y, bateria)
Lucas = No(0, 1, 0, 0, 10)
Thales = No(1, 2, 2, 0, 10)
Joao = No(2, 2, 3, 2, 10)
Pessoa = No(3, 2, 3, 0, 10)
Danielle = No(4, 1, 5, 1, 10)
Luciano = No(5, 2, 5, 3, 10)

id = []
x = []
y = []
cobertura = []

for no in nos:
    id.append(no._camadaRede._camadaEnlace._camadaFisica._id)
    x.append(no._camadaRede._camadaEnlace._camadaFisica._x)
    y.append(no._camadaRede._camadaEnlace._camadaFisica._y)
    cobertura.append(no._camadaRede._camadaEnlace._camadaFisica._cobertura)

#criaGraficos(id, x, y, cobertura)
# exit()

# Loop do tempo
for i in range(100):

    print("\n", BLUE, "Tempo: ", i, RESET, end="\n\n", )

    # Loop para percorrer
    for no in nos:

        # Numero aleatorio entre 0 e 100 para probabilidade de criação de pacotes
        rand = random.randint(0, 100)

        # Numero aleatorio entre 0 e a quantidade de hosts, para escolher um para enviar
        enviar = random.randint(0, len(nos)-1)

        # Teste se rand é menor que 6
        if(rand < 6):
            # Se o ID do destino for diferente do dele mesmo, adiciona o pacote no host
            if(enviar != (no._camadaRede._camadaEnlace._camadaFisica._id)):
                no.criarPacote(1, enviar, "F9 99 A2 09 A4 FB")
                indicesParaEnvio.append(
                    no._camadaRede._camadaEnlace._camadaFisica._id)

    if(proximoAEnviar != []):
        for i in proximoAEnviar:
            indicesParaEnvio.append(i)
    del proximoAEnviar[:]

    # Existe algum nó querendo receber, recebe
    for j in indicesParaVer:
        nos[j]._camadaRede.recebePacote()
    del indicesParaVer[:]

    # Existe algum nó querendo transmitir, transmite naquele instante se posssível
    for i in indicesParaEnvio:
        nos[i]._camadaRede.enviaPacote()
    del indicesParaEnvio[:]
