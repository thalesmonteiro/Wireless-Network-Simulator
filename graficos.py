import matplotlib.pyplot as plt
from listas import *

def criaGraficos(nome):

    id = []
    x = []
    y = []
    cobertura = []

    for no in nos:
        id.append(no._camadaRede._camadaEnlace._camadaFisica._id)
        x.append(no._camadaRede._camadaEnlace._camadaFisica._x)
        y.append(no._camadaRede._camadaEnlace._camadaFisica._y)
        cobertura.append(no._camadaRede._camadaEnlace._camadaFisica._cobertura)

    fig, ax = plt.subplots(1, 1)

    for idi, xi, yi, coberturai in zip(id, x, y, cobertura):

        area = 7500*(coberturai**2)
        #area = 13500*(coberturai)

        ax.scatter(xi, yi, color="r")
        ax.scatter(xi, yi, s=area, alpha=0.2, color="r")
        ax.annotate("%s\n%s" % (coberturai, idi), xy=(xi, yi))

    ax.grid()
    ax.set_aspect("equal")
    ax.set_title("Nós")
    #ax.set_xticklabels([i for i in range(1, 10)], fontsize=12)
    #plt.ylim(-10, 10)
    #plt.xlim(-10, 10)
    
    fig.canvas.set_window_title(f'{nome}')
    fig.savefig(f'./Graficos/{nome}.png')
    plt.show()


if __name__ == "__main__":
    criaGraficos()
