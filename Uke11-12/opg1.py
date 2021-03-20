from microbit import *

while True:
    temp = temperature()

    with open('file.txt', 'r') as file:
        file.write(temp+',')

    sleep(10000)
