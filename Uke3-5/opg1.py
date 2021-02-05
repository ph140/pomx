import numpy as np
from matplotlib import pyplot as plt


def integrasjon(tid, y_verdier):
    """
    Integrasjon ved trapesmetoden
    """
    y = np.zeros(len(tid))
    for i in range(len(y_verdier[:-1])):
        y[i+1] = y[i] + (tid[i+1] - tid[i])*(y_verdier[i]+y_verdier[i*1])/2
    return y


def hentData(navn):
    """
    Åpner filen og splitter opp for å lese av dataene. Mapper om dataene til
    floats, og lagrer de i lister
    """
    with open(navn+'fallskjerm.txt', 'r') as file:
        data = file.read()

    aks = list(map(float, data.split("[")[1].split("]")[0].split(", ")))
    tid = list(map(float, data.split("[")[2].split("]")[0].split(", ")))
    return aks, tid


def lagre(navn, tid, akselerasjon):
    """
    Lagrer akselersajonsverdier og tidsverdier i en ny fil, tids-verdiene +
    whitespace bruker opp 12 plasser. Deretter skrives akselerasjonen.
    Runder av tids+verdiene, uten at det har betydning.
    """
    with open(navn+'_kolonne.txt', 'w') as file:
        file.write(f"{'Tid':<12} Akselerasjon\n")
        for index, j in enumerate(tid):
            file.write(f'{str(round(j, 8)):<12} {str(akselerasjon[index])}\n')


def lag_prognose(tid, k):
    """
    Bruker Eulers metode til å lage verdier for fart.
    """
    g = 9.81  # tyngdeakselerasjon
    m = 0.37  # vekten til ballen
    tslutt = tid[-1]  # Sluttverdi er det samme som siste element i tids-listen
    N = len(tid)  # 500 steg som i tidsslisten
    h = (tslutt)/(N-1)  # Samme tidsintervalll som i tidslisten
    v = np.zeros(N)  # Liste der vi fyller inn verdier for fart

    # Eulers metode
    for i in range(N-1):
        v[i+1] = v[i] + h * (g - k * v[i]**2 / m)

    return(v)


def laggraf(navn, tid, fart, distanse, v, farge):
    """
    Plotter grafene ved eulers metode, de målte dataene og distansen.
    """
    plt.plot(tid, v, farge+'--', label=navn + ' Prognose')
    plt.plot(tid, fart, farge, label=navn + ' Målte data')
    plt.plot(tid, distanse, farge+':', label=navn+' Distanse')


def skriv_svar(navn, forhold, distanse):
    """
    Printer forholdet mellom areal og k-verdi, og distanse.
    """
    navn = navn.capitalize()  # Stor forbokstav
    print(f'{navn} fallskjerm:')
    print(f'Forhold: {forhold}')
    print(f'Distanse: {round(distanse[-1], 4)}\n')


def main(navn, radius, k, farge):
    """
    Hovedfunksjon som bruker alle de andre funksjonene.
    """
    akselerasjon, tid = hentData(navn)
    fart = integrasjon(tid, akselerasjon)
    distanse = integrasjon(tid, fart)
    v = lag_prognose(tid, k)
    forhold = round(np.pi*radius**2/k, 4)  # Areal/k, runder av til 4 desimaler
    lagre(navn, tid, akselerasjon)
    laggraf(navn, tid, fart, distanse, v, farge)
    skriv_svar(navn, forhold, distanse)


# Kjører liten, middels og stor gjennom hovedfunksjonen
main('liten', 0.11, 0.043, 'r')
main('middels', 0.17, 0.19, 'g')
main('stor', 0.26, 0.84, 'b')

# Lager aksetitler, legend og viser grafen
plt.xlabel('Tid (s)')
plt.ylabel('Fart (m/s)')
plt.legend(title='Fallskjerm')
plt.show()
