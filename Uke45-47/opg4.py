import numpy as np
from matplotlib import pyplot as plt

data = np.loadtxt('fallskjerm.txt', float, skiprows=1)

# Oppretter startverdier
trapesliste = [0]
rektliste = [0]
timelist = [0]
Sum_trapes = 0
Sum_rekt = 0

for i, _ in enumerate(data[:-1]):
    # Finner tid og steglengde
    time1 = data[i][0]
    time2 = data[i+1][0]
    dx = time2-time1

    # Finner akselerasjonsverdier (hoyde)
    h1 = data[i][1]
    h2 = data[i+1][1]

    # Regner ut areal ved bruk av trapes og rektangelmetoden
    A_trapes = dx*(h1+h2)/2
    A_rekt = dx*h1

    # Lagrer summen av alle arealene
    Sum_trapes += A_trapes
    Sum_rekt += A_rekt

    # Legger til verdiene i listene
    timelist.append(time1)
    trapesliste.append(A_trapes+trapesliste[i])
    rektliste.append(A_rekt+rektliste[i])

# Plotter trapesmetoden og rektangelmetoden
plt.plot(timelist, trapesliste, 'b-')
plt.title('Trapesmetoden')
plt.show()
plt.plot(timelist, rektliste, 'r-')
plt.title('Rektangelmetoden')
plt.show()
