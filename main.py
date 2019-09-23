from no import No
from lists import nos
from lists import indicesParaEnvio, indicesParaVer, proximoAEnviar
from pacote import Pacote 
from camadaRede import CamadaRede
import random
from graficos  import criaGraficos 
from constantes import *


Lucas = No(0, 2, 0, 0, 10)
Thales = No(1, 2, 1, 0, 10)
Joao = No(2, 2, 2, 1, 10)
Pessoa = No(3, 2, 3, 0, 10)
Danielle = No(4, 2, 4, 0, 10)
Luciano = No(5, 4, 5, 3, 10)

id = []
x = []
y = []
cobertura = []

for no in nos:
    id.append(no._camadaRede._camadaEnlace._camadaFisica._id)
    x.append(no._camadaRede._camadaEnlace._camadaFisica._x)
    y.append(no._camadaRede._camadaEnlace._camadaFisica._y)
    cobertura.append(no._camadaRede._camadaEnlace._camadaFisica._cobertura)

criaGraficos(id, x, y, cobertura)

#Loop do tempo
for i in range(100):
     
    print("\n", BLUE, "Tempo: ", i, RESET, end="\n\n", )

    #Loop para percorrer 
    for no in nos:

        #Numero aleatorio entre 0 e 100 para probabilidade de criação de pacotes
        rand = random.randint(0, 100)

        #Numero aleatorio entre 0 e a quantidade de hosts, para escolher um para enviar
        enviar = random.randint(0, len(nos)-1)

        #Teste se rand é menor que 6
        if(rand < 6):
                #Se o ID do destino for diferente do dele mesmo, adiciona o pacote no host
                if(enviar != (no._camadaRede._camadaEnlace._camadaFisica._id)):
                        no.criarPacote(1, enviar, "F9 99 A2 09 A4 FB")
                        indicesParaEnvio.append(no._camadaRede._camadaEnlace._camadaFisica._id)
                
    if(proximoAEnviar != []):
        for i in proximoAEnviar:
                indicesParaEnvio.append(i)
    del proximoAEnviar[:]

    #Existe algum nó querendo receber, recebe
    for j in indicesParaVer:
            nos[j]._camadaRede.recebePacote()
    del indicesParaVer[:]

    #Existe algum nó querendo transmitir, transmite naquele instante se posssível
    for i in indicesParaEnvio: 
            nos[i]._camadaRede.enviaPacote()
    del indicesParaEnvio[:]