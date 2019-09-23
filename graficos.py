import matplotlib.pyplot as plt


def criaGraficos(id, x, y, cobertura):
    fig, ax = plt.subplots(1, 1)

    for idi, xi, yi, coberturai in zip(id, x, y, cobertura):
        ax.scatter(xi, yi, color="r")
        ax.scatter(xi, yi, s=13950*coberturai, alpha=0.2, color="r")
        ax.annotate("%s" % idi, xy=(xi, yi))

    ax.grid()
    ax.set_aspect("equal")
    ax.set_title("Nós")
    #ax.set_xticklabels([i for i in range(1, 10)], fontsize=12)
    #plt.ylim(-10, 10)
    #plt.xlim(-10, 10)

    fig.savefig('./plotcircles.png')


if __name__ == "__main__":
    criaGraficos()
