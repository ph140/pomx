tall = int(input("tall:\n"))  # Input fra bruker
faktorliste = []  # Definerer listen som skal lagre faktorene

if tall < 0:
    tall = abs(tall)
    faktorliste.append(-1)


while tall > 1:
    for i in range(2, tall+1):  # Itererer gjennom tallene fra 2 til tall
        if tall % i == 0:
            # Legger til "i" i faktorliste dersom det er en faktor
            # og endrer verdien til tall for å sjekke neste faktor
            tall = int(tall/i)
            faktorliste.append(int(i))
            break

# Reverserer listen og printer den ut
faktorliste.sort(reverse=True)
print(faktorliste)
