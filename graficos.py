import matplotlib.pyplot as plt


def criaGraficos(id, x, y, cobertura):
    fig, ax = plt.subplots(1, 1)

    for idi, xi, yi, coberturai in zip(id, x, y, cobertura):

        area = 9900*(coberturai**2)

        ax.scatter(xi, yi, color="r")
        ax.scatter(xi, yi, s=area, alpha=0.2, color="r")
        ax.annotate("%s\n%s" % (coberturai, idi), xy=(xi, yi))

    ax.grid()
    ax.set_aspect("equal")
    ax.set_title("Nós")
    #ax.set_xticklabels([i for i in range(1, 10)], fontsize=12)
    #plt.ylim(-10, 10)
    #plt.xlim(-10, 10)

    fig.savefig('./plotcircles.png')
    plt.show()


if __name__ == "__main__":
    criaGraficos()
