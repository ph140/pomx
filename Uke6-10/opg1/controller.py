from microbit import *
import neopixel
import radio
radio.config(group=23)
radio.on()

while True:
    sleep(40)
    x = accelerometer.get_x()
    y = accelerometer.get_y()

    if button_b.is_pressed():
        radio.send('f,'+str(x)+','+str(y))
    elif button_a.is_pressed():
        radio.send('b,'+str(x)+','+str(y))
    elif x > 500:
        radio.send('l')
    elif x < -500:
        radio.send('r')
    else:
        radio.send('s')
