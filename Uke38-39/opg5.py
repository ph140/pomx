tall = int(input("Tall: "))  # Tar inn input

if tall == 2:
    print("Primtall")


for i in range(2, tall):
    # Begynner å iterere gjennom tallene fra 2 til "tall"
    # og sjekker om "tall" er delelig på noen av de.
    if tall % i == 0:
        print("Ikke primtall")
        break
    # Bryter ut av loopen dersom den har gått gjennom alle mulige faktorene
    elif i > tall/i:
        print("Primtall")
        break
