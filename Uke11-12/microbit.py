
# Nødvendig bibliotek for at innebygde funksjonaliteter skal virke.
from microbit import *
import utime


time = 0  # Brukes til å registrere tidsmålinger.

while True:
    if button_a.is_pressed():
        data = open('data.txt', 'w')
        while True:
            display.show(Image.MEH)
            start = utime.ticks_ms()
            temp = temperature()

            data.write('{:<10.3f} {:<20.3f} \n'.format(time, temp))

            if time >= 1800:
                break

            now = utime.ticks_ms()
            if utime.ticks_diff(now, start) < 10000:
                utime.sleep_ms(10000 - utime.ticks_diff(now, start))
            time += 10
        data.close()
        break
display.show(Image.HAPPY)
