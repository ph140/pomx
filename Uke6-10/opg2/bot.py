from microbit import *


# Funksjoner for å kjøre høyre venster og rett frem
def rightDrive():
    pin14.write_analog(300)
    pin8.write_analog(0)
    pin16.write_analog(0)


def leftDrive():
    pin16.write_analog(300)
    pin12.write_analog(0)
    pin14.write_analog(0)


def forward():
    pin16.write_analog(300)
    pin14.write_analog(300)


while True:
    # Venter 20ms og leser av info fra i2c
    sleep(20)
    value = i2c.read(0x1c, 1)[0]

    # Kjører til venster dersom høyre hjul er utenfor sort linje,
    # til høyre dersom venstre hjul er utenfor, og rett frem ellers
    if value == 113:
        rightDrive()
    elif value == 114:
        leftDrive()
    elif value == 112 or value == 115:
        forward()
