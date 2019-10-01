
# Classes implementadas
from no import No
from pacote import Pacote
from camadaRede import CamadaRede
from graficos import criaGraficos

# Bibliotecas do sistema
import random
import argparse

# Variáveis globais do programa
from listas import *
from constantes import *


# No(id, cobertura, x, y, bateria)
Lucas = No(0, 1.7, 0, 0, 30)
Thales = No(1, 1.7, 1, 1, 30)
Joao = No(2, 1.7, 2, 2, 30)
Pessoa = No(3, 1.7, 3, 3, 30)
Danielle = No(4, 1.7, 4, 4, 30)
Luciano = No(5, 1.7, 5, 5, 30)
Luiz = No(6, 2, 2, 4, 30)
Fortaleza = No(7, 2, 2.5, 1.5, 30)


def main_rand():
    # Posição inicial dos pontos no grafico
    criaGraficos("Inicio")

    numPac = True
    # Loop do tempo
    for tempo in range(100):
        print("\n", BLUE, "Tempo: ", tempo, RESET, end="\n\n")

        # Loop para percorrer
        # for no in nos:
        for i in range(len(nos)):
            try:
                no = nos[i]
                if(no._camadaRede._camadaEnlace._camadaFisica._bateria <= 0):
                    print(RED, "Nó com ID: {} possui bateria descarregada.".format(
                        no._id), RESET)
                    nos.remove(no)
                    print(RED, "Nó com ID: {} foi morto.".format(no._id), RESET)
                    criaGraficos(f"Gráfico sem o nó com ID {no._id} removido")
            except:
                continue

            if(tempo == 99):
                print(CYAN, "Nó com ID: {} possui bateria {} carregada".format(no._id,
                                                                               no._camadaRede._camadaEnlace._camadaFisica._bateria), RESET)

            # Numero aleatorio entre 0 e 100 para probabilidade de criação de pacotes
            rand = random.randint(0, 100)

            # Numero aleatorio entre 0 e a quantidade de hosts, para escolher um para enviar
            enviar = random.randint(0, len(nos)-1)

            mensagem = random.randint(0, 256**6)
            mensagem = hex(mensagem).upper()

            # Teste se rand é menor que 6
            if(rand < 6):
                # Se o ID do destino for diferente do dele mesmo, adiciona o pacote no host
                if(enviar != (no._camadaRede._camadaEnlace._camadaFisica._id)):
                    duracao = 1
                    no.criarPacote(duracao, enviar, mensagem)
                    indicesParaEnvio.append(
                        no._camadaRede._camadaEnlace._camadaFisica._id)

        if(proximoAEnviar != []):
            for i in proximoAEnviar:
                indicesParaEnvio.append(i)
        del proximoAEnviar[:]

        # Existe algum nó querendo receber, recebe
        for j in indicesParaReceber:
            try:
                nos[j]._camadaRede.recebePacote()
            except:
                print(RED, "Nó não existe mais para poder receber.", RESET)
                continue
            # if(nos[j]._camadaRede._camadaEnlace._camadaFisica._bateria <= 0):
        del indicesParaReceber[:]

        # Existe algum nó querendo transmitir, transmite naquele instante se posssível
        for i in indicesParaEnvio:
            try:
                nos[i]._camadaRede.enviaPacote()
            except:
                print(RED, "Nó não existe mais para poder transmitir.", RESET)
                continue
        del indicesParaEnvio[:]


def main():
    # Posição inicial dos pontos no grafico
    criaGraficos("Inicio")

    numPac = 0
    # Loop do tempo
    for tempo in range(50):

        print("\n", BLUE, "Tempo: ", tempo, RESET, end="\n\n")

        # Se o tempo for igual a 25, o nó 2 morre
        if (tempo == 25):
            #nos[2]._camadaRede._camadaEnlace._camadaFisica._bateria = 0
            numPac = 0

        # Loop para percorrer
        # for no in nos:
        for i in range(len(nos)):
            try:
                no = nos[i]
                if(no._camadaRede._camadaEnlace._camadaFisica._bateria <= 0):
                    print(RED, "Nó com ID: {} possui bateria descarregada.".format(
                        no._id), RESET)
                    nos.remove(no)
                    print(RED, "Nó com ID: {} foi morto.".format(no._id), RESET)
                    criaGraficos(f"Gráfico sem o nó com ID {no._id} removido")
            except:
                continue

            if(tempo == 49):
                print(CYAN, "Nó com ID: {} possui bateria {} carregada".format(no._id,
                                                                               no._camadaRede._camadaEnlace._camadaFisica._bateria), RESET)

            # Numero aleatorio entre 0 e 100 para probabilidade de criação de pacotes
            # rand = random.randint(0, 100)

            # Numero aleatorio entre 0 e a quantidade de hosts, para escolher um para enviar
            # enviar = random.randint(0, len(nos)-1)
            enviar = 6

            # Criando mensagem aleatória
            mensagem = random.randint(0, 256**6)
            mensagem = hex(mensagem).upper()

            # Teste se rand é menor que 6
            # if(rand < 6):
            if(numPac < 1):
                # Se o ID do destino for diferente do dele mesmo, adiciona o pacote no host
                # if(enviar != (no._camadaRede._camadaEnlace._camadaFisica._id) and (no._camadaRede._camadaEnlace._camadaFisica._id) == 0):
                # Somente o nó 0 envia para o nó 6
                if((no._camadaRede._camadaEnlace._camadaFisica._id) == 0):
                    duracao = 1
                    no.criarPacote(duracao, enviar, mensagem)
                    indicesParaEnvio.append(
                        no._camadaRede._camadaEnlace._camadaFisica._id)
                numPac += 1

        if(proximoAEnviar != []):
            for i in proximoAEnviar:
                indicesParaEnvio.append(i)
        del proximoAEnviar[:]

        # Existe algum nó querendo receber, recebe
        for j in indicesParaReceber:
            try:
                nos[j]._camadaRede.recebePacote()
            except:
                print(RED, "Nó não existe mais para poder receber.", RESET)
                continue
            # if(nos[j]._camadaRede._camadaEnlace._camadaFisica._bateria <= 0):
        del indicesParaReceber[:]

        # Existe algum nó querendo transmitir, transmite naquele instante se posssível
        for i in indicesParaEnvio:
            try:
                nos[i]._camadaRede.enviaPacote()
            except:
                print(RED, "Nó não existe mais para poder transmitir.", RESET)

                continue
        del indicesParaEnvio[:]


if (__name__ == "__main__"):

    parser = argparse.ArgumentParser(
        description='Código para cadeira de redes sem fio')
    parser.add_argument(
        'modo', type=str, help='Modo da função main: "rand" para aleatório; "deter" para deterministica')

    args = parser.parse_args()

    if args.modo == "rand":
        print(GREEN, "Modo randômico escolhido", RESET)
        main_rand()
    elif args.modo == "deter":
        print(GREEN, "Modo deterministico escolhido", RESET)
        main()
