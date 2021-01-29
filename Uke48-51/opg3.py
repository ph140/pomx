from numpy import sin, pi, cos

# Definerer kjente verdier
g = 9.81
tetha = pi/10
h = 0.0001
x0 = 1


# Definerer funskjonene for høyde og strekning.
def y(t):
    return (-0.5*g*t**2)+(18*(sin(tetha))*t)


def x(t):
    return 18*cos(tetha)*t


# Newtons metode for å finne nullpunkt
while abs(y(x0)) > 0.0001:
    x0 -= y(x0)/((y(x0+h)-y(x0))/h)

# Printer ut hvor langt ballen ble kastet ved å finne x-verdi av nullpunktet.
print(f"Ballen ble kastet {round(x(x0), 2)} meter langt.")
