# Importerer nødvendige bibliotek
from matplotlib import pyplot as plt
import numpy as np
from itertools import count

# Konstanten 3.27 passer best med målingen jeg gjorde.
k0 = 3.27


h = 0.096  # Hoyde/m
diameter_botte = 0.176  # Radius/m
diameter_propp = 0.011  # Radius/m

A = (diameter_botte/2)**2*np.pi  # Areal propp/m^2
Ap = (diameter_propp/2)**2*np.pi  # Areal grunnflate/m^2

# Utrykk for k
k = k0*(Ap/A)


def waterchange(h):
    # Funskjon for endring av vannhoyde
    return -k*np.sqrt(h)


# Definere lister som trengs
time = [0]  # Tid/ms
model = [h]  # Hoyde/m

# Uendelig loop, i inkrementerer
for i in count(0):
    # Avslutter dersom vannstanden har nådd halveis
    if model[i] < h/2:
        break

    # Eulers metode. Deler på 1000 for bedre nøyaktighet
    model.append(model[i] + waterchange(model[i])/1000)
    time.append(i+1)

# Skriver hvor lang tid det tar
print(f'Halveis etter {time[-1]/1000} sekunder.')

# Plotter grafen
plt.plot(time, model, 'r-')
plt.xlabel('Tid/ms')
plt.ylabel('Vannstand/m')
plt.show()
