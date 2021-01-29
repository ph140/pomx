import numpy as np
from matplotlib import pyplot as plt

k = 0.1
t_0 = 0  # startverdi for t (initialbetingelse)
f_0 = 1000  # startverdi for f (initialbetingelse)
t_slutt = 20  # sluttverdi for t

N = 10000  # antall steg
h = (t_slutt-t_0)/(N-1)  # regner ut steglengden
t = np.linspace(t_0, t_slutt, N)  # Array med alle tidsverdier

f = np.zeros(N)  # lager array med N nuller
f[0] = f_0  # Første element er startverdien for f (antall harer satt ut)


# Funksjon for den deriverte
def f_derivert(ft):
    return k*ft


# Eulers metode
for i in range(N-1):
    f[i+1] = f[i] + f_derivert(f[i])*h

# Printer antall harepuser
print(f"Det blir {f[-1]} harepuser etter {t_slutt - t_0} måneder.")

# Plotter resultat
plt.plot(t, f)
plt.show()
