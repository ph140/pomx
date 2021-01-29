# Definerer funksjonene
def f(x):
    return 2*x + 1


def g(x):
    return x**2-x-6


# Definerer to x-verdier langt fra hverandre og et tall tiln'rmet null
a = 10000
b = -10000
null = 0.0001


# Bruker halveringsmetoden mellom a og b, med funksjonen f.
def halveringsmetoden(a, b, f):
    m = (a+b)/2
    while abs(f(m)) > null:
        if f(a)*f(m) > 0:
            a = m
        else:
            b = m
        m = (a+b)/2
    return f.__name__, m


print(halveringsmetoden(a, b, f))
print(halveringsmetoden(a, b, g))
