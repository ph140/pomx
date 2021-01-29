from matplotlib import pyplot as plt
from numpy import sin, cos, tan, pi, linspace
from random import randint


def polynom(x):
    return (x**2/10) - 2*x + 5


# lager en liste med x-verdeier fra 0 til 12.56
xverdier = []
steglengde = 0.1
steg = int((4*pi)/steglengde)
for i in range(steg):
    if i*steglengde > pi * 4:
        break
    xverdier.append(i*steglengde)


# Plotter funksjonen som blir gitt som argument
def visgraf(funksjon):
    yverdier = []

    for x in xverdier:
        yverdier.append(funksjon(x))

    plt.plot(xverdier, yverdier, 'b--')
    plt.xlabel("x-akse")
    plt.ylabel("y-akse")
    plt.title(str(funksjon))
    plt.ylim(-10, 10)
    plt.show()


def opg1a():
    visgraf(sin)
    visgraf(tan)
    visgraf(cos)
    visgraf(polynom)


# Plotter fire funksjoner i samme ramme, fra 0 til 12.56
def opg1bc():
    punkter = round(4*pi/0.1)

    x = linspace(0, 12.56, punkter)
    y1 = sin(x)
    y2 = cos(x)
    y3 = tan(x)
    y4 = polynom(x)

    plt.figure()
    plt.subplot(2, 2, 1)
    plt.plot(x, y1, 'g-')
    plt.subplot(2, 2, 2)
    plt.plot(x, y2, 'r-')
    plt.subplot(2, 2, 3)
    plt.ylim(-10, 10)
    plt.plot(x, y3, 'y-')
    plt.subplot(2, 2, 4)
    plt.plot(x, y4, 'b-')
    plt.show()


# O P P G A V 2

# Legger til 100 tilfeldige tall mellom 1 og 100 til en fil
# Leser deretter av filen og printer de som en liste fra st;rst til minst
def opg2():
    with open("tilfeldigeTall.txt", "w") as file:
        for i in range(100):
            file.write(str(randint(1, 100))+",")

    with open("tilfeldigeTall.txt", "r") as file:
        minliste = file.read().split(",")

    # Sletter det siste elementet siden det blir en tom string
    minliste.pop()

    # Gj;r om fra string til int
    minliste = list(map(int, minliste))
    minliste.sort(reverse=True)
    print(minliste)


# Leser av akselerasjon.txt og plotter verdiene som milli-g over tid
def opg3():
    xliste = []
    yliste = []

    with open('akselerasjon.txt', 'r') as f:
        akselerasjonsliste = f.read().split(' ')

    for i, val in enumerate(akselerasjonsliste):
        xliste.append(i*5)
        yliste.append(int(val))

    plt.plot(xliste, yliste, 'y-')
    plt.title('Akselerasjon over tid')
    plt.xlabel('Tid / ms')
    plt.ylabel('Milli-g')
    plt.show()


opg1bc()
