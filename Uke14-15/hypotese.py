# Importerer nødvendige bibliotek
from matplotlib import pyplot as plt
import numpy as np
from itertools import count

# Konstanten 3.27 passer best med målingen jeg gjorde.
k0 = 3.27


h = 0.5  # Hoyde/m
diameter_basseng = 1.35  # Radius/m
diameter_propp = 0.024  # Radius/m

A = (diameter_basseng/1)**2*np.pi  # Areal propp/m^2
Ap = (diameter_propp/1)**2*np.pi  # Areal grunnflate/m^2

# Utrykk for k
k = k0*(Ap/A)


def waterchange(h):
    # Funskjon for endring av vannhoyde
    return -k*np.sqrt(h)


# Definere lister som trengs
time = [0]  # Tid/ms
model = [h]  # Hoyde/m

# Uendelig loop, i inkrementerer.
for i in count(0):
    # Avslutter dersom vannstanden har nådd halveis
    if model[i] < h/2:
        break

    # Eulers metode. Deler på 100 for større nøyaktighet
    model.append(model[i] + waterchange(model[i])/1000)  # Eulers metode
    time.append(i+1)

# Skriver hvr lang tid det tar
print(f'Halveis etter {time[-1]/1000} sekunder.')

# Plotter grafen
plt.plot(time, model, 'r-')
plt.xlabel('Tid/ms')
plt.ylabel('Vannstand/m')
plt.show()
