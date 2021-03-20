from matplotlib import pyplot as plt
import numpy as np

# Laster inn temperatur-data
data = np.loadtxt('temperatur.txt', float)

# Definerer konstanter, k=0.003 passer best med målingene
k = 0.003
temp_omgivelse = 3

# Hvor nær omgivelsene vi søker etter
nøyaktighet = 0.5


# Newtons avkjølingslov
def derivert(x):
    return k*(temp_omgivelse-x)


# Lager listene som trengs
time1 = []
time2 = [0]
temp = []
modell = [39]


# Lager lister med tid og temperatur
for i, j in enumerate(data):
    time1.append(j[0])
    temp.append(j[1])

# Lager enn ny tidsliste og en liste for anslåtte temperatur-verdier.
for i in range(10000):
    # Ganger med 10 siden det er 10 sekunder mellom målingene.
    time2.append(i*10)
    modell.append(modell[i] + derivert(modell[i]))

    # Stopper dersom temperaturen er 0.5 unna omgivelsene
    if modell[i] - nøyaktighet < temp_omgivelse:
        break

print(f'Vannet når temperaturen utendørs etter {time2[-1]/60} minutter.')

# Plotter grafene
plt.plot(time1, temp, 'g-', label='måling')
plt.plot(time2, modell, 'r:', label='modell')
plt.xlabel('Tid/s')
plt.ylabel('Temperatur/C')
plt.legend()
plt.title('Newtons avkjølingslov')
plt.show()
