# Tar inn tre tall fra brukeren
a = float(input("Tall1:\n"))
b = float(input("Tall2:\n"))
c = float(input("Tall3:\n"))


def triple(a, b, c):
    # Endrer variablene til kvadratet av seg selv
    a = a**2
    b = b**2
    c = c**2

    # Sjekker om det er pytagorisk sammenheng mellom de, og returner True/False
    if a + b == c:
        return True
    elif a + c == b:
        return True
    elif b + c == a:
        return True


# Skriver ut resultatet basert på svaret fra funksjonen
if triple(a, b, c):
    print("Tallene er pytagoriske tripler")
else:
    print("Tallene er ikke pytagoriske tripler")
