from microbit import *
import neopixel
import radio
from random import randint
radio.config(group=23)
radio.on()
np = neopixel.NeoPixel(pin13, 11)


def forward():
    for i in range(0, len(np)):
        if i % 2 == 0:
            np[i] = (0, 255, 0)
    pin16.write_analog(511)
    pin8.write_analog(0)
    pin14.write_analog(511)
    pin12.write_analog(0)


def backward():
    for i in range(0, len(np)):
        if i % 2 == 0:
            np[i] = (255, 0, 0)
    pin16.write_analog(0)
    pin8.write_analog(511)
    pin14.write_analog(0)
    pin12.write_analog(511)


def turn_right():
    for i in range(0, len(np)):
        if i % 2 == 0 and i < 6:
            np[i] = (255, 0, 255)
    pin16.write_analog(0)
    pin8.write_analog(400)
    pin14.write_analog(400)
    pin12.write_analog(0)


def turn_left():
    for i in range(0, len(np)):
        if i % 2 == 0 and i > 5:
            np[i] = (255, 0, 255)
    pin16.write_analog(400)
    pin8.write_analog(0)
    pin14.write_analog(0)
    pin12.write_analog(400)


def stop():
    for i in range(0, len(np)):
        if i % 2 == 0:
            np[i] = (0, 0, 255)
    pin16.write_analog(0)
    pin8.write_analog(0)
    pin14.write_analog(0)
    pin12.write_analog(0)


while True:
    sleep(5)
    message = str(radio.receive())
    np.clear()

    if 'f' in message:
        forward()
    elif 'b' in message:
        backward()
    elif 'r' in message:
        turn_right()
    elif 'l' in message:
        turn_left()
    else:
        stop()
    np.show()
