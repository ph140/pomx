import numpy as np
from matplotlib import pyplot as plt


# Funksjoner som returnerer den deriverte i henhold til oppgitt difflikning.
def f1_derivert(t):
    return(1)


def f2_derivert(t):
    return(2*t + 4)


def f3_derivert(ft):
    return 4 + 3*ft


def f4_derivert(t):
    return np.e**t


t_0 = 0  # startverdi for t (initialbetingelse)
f_0 = 0  # startverdi for f (initialbetingelse)
t_slutt = 2  # sluttverdi for t

N = 10000  # antall steg
h = (t_slutt-t_0)/(N-1)  # regner ut steglengden

# lager et array for verdier av t fra startverdi til sluttverdi
t = np.linspace(t_0, t_slutt, N)
# lager array for å lagre verdier for f
# Siden initialbetingelsen er at f(0) = 0 trenger vi ikke gjøre mer
f1 = np.zeros(N)
f2 = np.zeros(N)
f3 = np.zeros(N)
f4 = np.zeros(N)


# Bruker Eulers metode for å regne ut neste steg.
for i in range(N-1):
    f1[i+1] = f1[i] + f1_derivert(t[i])*h
    f2[i+1] = f2[i] + f2_derivert(t[i])*h
    f3[i+1] = f3[i] + f3_derivert(f3[i])*h
    f4[i+1] = f4[i] + f4_derivert(t[i])*h


# PLotter alle funskjonene
plt.plot(t, f1)
plt.show()

plt.plot(t, f2)
plt.show()

plt.plot(t, f3)
plt.show()

plt.plot(t, f4)
plt.show()
