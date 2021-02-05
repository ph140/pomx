import numpy as np
from matplotlib import pyplot as plt


def trapes_metode(x, y, i):
    return (x[i+1] - x[i]) * ((y[i] + y[i+1]))


class fallSkjerm():
    def __init__(self, navn, radius, k, color):
        self.navn = navn.capitalize()
        self.color = color
        self.radius = radius
        self.k = k
        self.akselerasjon, self.tid = self.hentData()
        self.fart = self.integrasjon(self.akselerasjon)
        self.distanse = self.integrasjon(self.fart)
        self.t, self.v = self.lag_prognose()
        self.forhold = round(np.pi*self.radius**2/self.k, 4)
        self.lagre()
        self.laggraf()
        self.skriv_svar()

    def hentData(cls):
        with open(cls.navn+'fallskjerm.txt', 'r') as file:
            data = file.read()

        aks = list(map(float, data.split("[")[1].split("]")[0].split(", ")))
        tid = list(map(float, data.split("[")[2].split("]")[0].split(", ")))
        return aks, tid

    # Lagrer akselersajonsverdiene i kolonneform i nye filer.
    def lagre(cls):
        with open(cls.navn+'_kolonne.txt', 'w') as file:
            file.write(f"{'Tid':<12} Akselerasjon\n")
            for index, j in enumerate(cls.tid):
                file.write(
                    f'{str(round(j, 8)):<12} {str(cls.akselerasjon[index])}\n')

    def integrasjon(cls, y_verdier):
        y = [0]
        for i, tid in enumerate(cls.tid[:-1]):
            y.append(y[i-1] + trapes_metode(cls.tid, y_verdier, i))
        return y

    def lag_prognose(cls):
        g = 9.81  # tyngdeakselerasjon
        m = 0.37  # vekten til ballen
        tslutt = cls.tid[-1]
        N = 500  # 500 steg som i fartslisten
        h = (tslutt)/(N-1)  # Samme tidsintervalll som i tidslisten

        v = np.zeros(N)  # Liste der vi fyller inn verdier for fart
        t = np.zeros(N)  # Liste der vi fyller inn verdier for tid

        # Eulers metode
        for i in range(N-1):
            v[i+1] = v[i] + h * (g - cls.k * v[i]**2 / m)
            t[i+1] = t[i] + h

        return(t, v)

    # Plotter grafer for fart, prognose-fart og distanse
    def laggraf(cls):
        plt.plot(cls.t, cls.v, cls.color+'--', label=cls.navn + ' Prognose')
        plt.plot(cls.tid, cls.fart, cls.color, label=cls.navn + ' Målte data')
        plt.plot(cls.tid, cls.distanse, cls.color +
                 ':', label=cls.navn+' Distanse')

    # Printer areal, k-verdi og forhold.
    def skriv_svar(cls):
        print(f'{cls.navn} fallskjerm:')
        print(f'Forhold: {cls.forhold}')
        print(f'Distanse: {round(cls.distanse[-1], 4)}\n')


# Lager de tre instansene av fallskjermene
liten = fallSkjerm('liten', 0.11, 0.043, 'r')
middels = fallSkjerm('middels', 0.17, 0.19, 'g')
stor = fallSkjerm('stor', 0.26, 0.84, 'b')

# Lager aksetitler, legend og viser grafen
plt.xlabel('Tid (s)')
plt.ylabel('Fart (m/s)')
plt.legend(title='Fallskjerm')
plt.show()
