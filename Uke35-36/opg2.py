fornavn = str(input("Fornavn: "))
etternavn = str(input("Etternavn: "))
adr = str(input("Addresse: "))
tlf = str(input("Telefonnummer: "))


class person():

    # Metode som konstruerer et nytt objekt
    def __init__(self, fornavn, etternavn, adr, tlf):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.adr = adr
        self.tlf = tlf

    # Metode for å lagre personen i en tekstfil der hver person er adskilt med
    # en ny linje og hver info-del er adkilt med komma.
    def save(cls):
        f = open("personer/personer.txt", "a")
        f.write(cls.fornavn + ", " + cls.etternavn +
                ", " + cls.adr + ", " + cls.tlf + "\n")
        f.close()
        print("Du er lagret", cls.fornavn)


# Lager et nytt objekt med tidligere input som argumenter
nyperson = person(fornavn, etternavn, adr, tlf)
# Kaller på lagremetoden
nyperson.save()
del nyperson
