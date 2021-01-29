from numpy import sqrt, pi, e


# Standard normalfordeling
def f(x):
    return (1/sqrt(2*pi)) * e**((-x**2)/2)


# Returnerer det samlede arealet mellom funksjonen f og x-aksen, fra a til b.
# Ved bruk av rektangelmetoden
def rektangelmetoden(f, a, b, N, offset=0.5):
    S = 0
    dx = (b-a)/N

    for n in range(N):
        x = a + n*dx
        h = f(x+offset*dx)
        A = dx*h
        S += A

    return S


# Returnerer det samlede arealet mellom funksjonen f og x-aksen, fra a til b.
# Ved bruk av trapesmetoden
def trapesmetoden(f, a, b, N):
    S = 0
    dx = (b-a)/N

    for n in range(N):
        x = a + n*dx
        h1 = f(x)
        h2 = f(x+dx)
        A = dx*(h1+h2)/2
        S += A

    return S


# Lager en fil, eller sletter alt som er i den fra for, slik at den er blank.
with open('normalfordeling.txt', 'w') as _:
    pass


def res(h):
    '''
    Bruker både rektangelmetoden og trapesemetoden til å finne arealet fra
    -1, 1 -2,2 og -3, 3, med funskjonen f. Bruker steglengde h.
    Og skriver ut resultatene fra utregningen i filen normalfordeling.txt,
    runder også av til bare to desimaler.
    '''
    for k in range(1, 4):
        N = int((k*2)/h)
        rek = round(rektangelmetoden(f, -k, k, N), 2)
        trapes = round(trapesmetoden(f, -k, k, N), 2)
        with open('normalfordeling.txt', 'a') as file:
            file.write(f'k={k}, h={h}\n')
            file.write(f'Rektangelmetoden: {rek}\n')
            file.write(f'Trapesmetoden: {trapes}\n\n')

        print(f"k={k}, h={h}")
        print(f"Rektangelmetoden: {rek}")
        print(f"Trapesmetoden: {trapes}\n")


# Kjører h=0.1 og h=0.00001 gjennom resfunksjonen
res(0.1)
res(0.00001)
