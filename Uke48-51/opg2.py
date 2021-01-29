from numpy import e

# Definerer steglangde og starverdi for x
h = 0.1
x = 0


# Definerer funksjonene
def f(x):
    return (2*x+1)/((2/3)-2*x)


def g(x):
    return (e**(2*x))-10


# Definerer en funksjon som bruker newtons metode for å finne røtter
# av en funskjon.
def newtons_metode(f):
    global x
    while abs(f(x)) > 0.0001:
        x -= f(x)/((f(x+h)-f(x))/h)
    return x


# Printer ut svaret i a og b på hver sin linje
print(f"a) {newtons_metode(f)} \nb) {newtons_metode(g)}")
