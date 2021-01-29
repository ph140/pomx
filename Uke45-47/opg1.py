import numpy as np
from matplotlib import pyplot as plt


# Definerer funskjonene som skal brukes
def d(x):
    return (np.e)**x - 5*x


def g(x):
    return x**2 - 4*x + 5


def i(x):
    return 2*x + 1


# Funksjon for den deriverte
def derivert(f, x, h):
    return ((f(x+h)-f(x))/h)


# Bestemmer h-ferdi og definisjonsmengde
h = 0.01
xmin = 2
xmax = 5

# Bergner antall punkter vi akn ha med den gitte h-verdien
N = int((xmax - xmin)/h)
# Lager en array med punktene
xes = np.linspace(xmin, xmax, N)


# Funskjon som tar inn et funskjonsnavn som argument, og
# plotter funksjonen og den deriverte av funksjonen.
def showres(f):
    func = f(xes)
    df = derivert(f, xes, h)

    plt.plot(xes, func, label='f (x)')
    plt.plot(xes, df, label="f' (x)")
    plt.xlabel('x')
    plt.grid('both')
    plt.legend()
    plt.show()


# Viser alle funksjonen hver for seg
showres(d)
showres(g)
showres(i)
