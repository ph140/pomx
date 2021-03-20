
# Nødvendig bibliotek for at innebygde funksjonaliteter skal virke.
from microbit import *
import utime


time = 0  # Brukes til å registrere tidsmålinger.

while True:
    if button_a.is_pressed():
        # Åpner en ny fil her, dersom knapp a er blitt trykket på
        data = open('temperatur.txt', 'w')
        while True:
            # Viser et MEH-fjes mens målingene pågår
            display.show(Image.MEH)

            # Tar inn en referansetid
            start = utime.ticks_ms()
            # Måler temperaturen
            temp = temperature()

            # Skriver til filen, tid og temperatur.
            data.write('{:<10.3f} {:<20.3f} \n'.format(time, temp))

            # Stopper loopen derom det har gått mer enn 1800s (30min)
            if time >= 1800:
                break

            # Ny referansetid
            now = utime.ticks_ms()

            # Kalkulerer hvor lang tid det gikk fra før vi målte og skrev til
            # filen, til etterpå
            if utime.ticks_diff(now, start) < 10000:
                # Tar pause til det har gått 10000ms (10s) til sammen.
                utime.sleep_ms(10000 - utime.ticks_diff(now, start))
            # + 10s
            time += 10

        # Stenger filen, og hopper ut av loopen.
        data.close()
        break
# Glad når jobben er gjort
display.show(Image.HAPPY)
