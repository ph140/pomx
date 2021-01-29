import numpy as np
from matplotlib import pyplot as plt


# Laster datafilen og lager tome lister
data = np.loadtxt('vogn.txt', float, skiprows=1)
time = []
speed1 = []
speed2 = []


# Lager funskjoner for den deriverte ved hjelp av newtons kvotient, og
# Newton's symetriske kvotient.
def derivert(x):
    return data[x+1][1] - data[x][1]


def symmetrisk_derivert(x):
    return (data[x+1][1] - data[x-1][1])/2


# Går gjennom listen bortsett fra det første og siste elementet
# Legger til derivert-verdier i sped1 og speed2, og legger til tidspunkt i time
for i, j in enumerate(data[:-1]):
    if i:
        speed1.append(derivert(i))
        speed2.append(symmetrisk_derivert(i))
        time.append(j[0])

# Plotter derivert og symmetrisk derivert
plt.plot(time, speed1, 'g-')
plt.plot(time, speed2, 'r-')
plt.show()
