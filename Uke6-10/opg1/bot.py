from microbit import *
import radio
import neopixel
from math import acos, cos, sin, sqrt, pi

radio.config(group=23)
radio.on()

np = neopixel.NeoPixel(pin13, 12)

# Definerer farger på forhånd
purple = (100, 0, 100)
red = (100, 0, 0)
green = (0, 100, 0)
blue = (0, 0, 100)
orange = (100, 100, 0)


# Funksjon som returnerer hvor fort venstre og høyre skal gå
# Basert på vektorer og vinkler
def move(pace, direction):
    if direction/sqrt(direction**2+pace**2) > 1:
        v = 0
    elif direction/sqrt(direction**2+pace**2) < -1:
        v = pi
    else:
        v = acos(direction/sqrt(direction**2+pace**2))

    rpace = pace*sin(v)-pace*sin(v)*cos(v)
    lpace = pace*sin(v)-pace*sin(v)*cos(pi-v)

    # Begrenser styrken til 1000
    if lpace > 1000:
        lpace = 1000
    if rpace > 1000:
        rpace = 1000
    return lpace, rpace


# Funksjoner for å kjøre forover og bakover
def forward(lpace, rpace):
    pin16.write_analog(lpace)
    pin8.write_digital(0)
    pin14.write_analog(rpace)
    pin12.write_digital(0)


def backward(lpace, rpace):
    pin16.write_digital(0)
    pin8.write_analog(lpace)
    pin14.write_digital(0)
    pin12.write_analog(rpace)


# Funksjon for å svinge med begge hjulene motsatt vei
# Returnerer hvilken type sving, for å vite hvilke lys som skal tennes
def turn(pace):
    pace *= 0.8
    if pace > 0:
        pin16.write_analog(pace)
        pin12.write_analog(pace)
        return 'lturn'
    else:
        pin14.write_analog(pace*-1)
        pin8.write_analog(pace*-1)
        return 'rturn'

# Funksjon for å stoppe


def stop():
    pin16.write_digital(0)
    pin8.write_digital(0)
    pin14.write_digital(0)
    pin12.write_digital(0)


"""
Variablene current og previous benyttes for hvilket modus roboten er  i
og dermed hvilke lys som skal lyse.
"""

previous = 'stopped'
while True:
    sleep(20)
    message = radio.receive()

    if message:
        # Splitter opp til direction og pace
        direction = int(message.split(',')[1])
        pace = int(message.split(',')[2])

        # Kjører forover dersom kodeord er f, og bakover dersom kodeord er b
        if 'f' in message:
            if pace < 0:
                lpace, rpace = move(pace*-1, direction)
                forward(lpace, rpace)
                current = 'drive_f'
        elif 'b' in message:
            if pace > 0:
                lpace, rpace = move(pace, direction)
                backward(lpace, rpace)
                current = 'drive_b'

        # Snurrer rundt dersom turn er i beskjeden
        elif 'turn' in message:
            current = turn(direction)

    # Stopper dersom det ikke kommer beskjed i radioen
    else:
        stop()
        current = 'stopped'

    # Dersom robotens modus har endret seg, skal lyset endre seg
    if current != previous:
        np.clear()
        if current == 'drive_f':
            np[5] = green
            np[11] = green
        if current == 'drive_b':
            np[0] = red
            np[6] = red
        if current == 'stopped':
            np[3] = blue
            np[8] = blue
        if current == 'rturn':
            np[3] = green
        if current == 'lturn':
            np[8] = green
        previous = current
        np.show()
