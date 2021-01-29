# O P P G A V E  1

def primtallsum(sum):
    primliste = [2]
    x = 2
    primsum = 2
    while primsum < sum:
        # Kjører loopen så lenge summen av alle primtallene den finner
        # er mindre enn argumentet 'sum'
        for i in range(2, x):
            if x % i == 0:
                # Sjekker om x er delelig paa i
                break
            elif x == i+1:
                # om x ikke er delelig med i noen gang
                primliste.append(x)
                primsum = primsum + x

        x += 1

    # Printer ut primtallene i listen dersom de har index som primtall
    for i, j in enumerate(primliste):
        if i in primliste:
            print(j)

    return len(primliste)


# O P P G A V E  2

lag = "Molde Brann Vålerenga Haugesund Mjøndalen"

tippelagliste = ["Bodø/glimt", "Molde", "Odd", "Rosenborg",
                 "Kristiansund", "Vålerenga", "Brann", "Haugesund",
                 "Stabæk", "Viking", "Strømsgodset", "Sarpsborg 08",
                 "Sandefjord", "Start", "Mjøndalen", "Aalesund"]


def listehandtering(lag, tippelaglisteliste):
    # Splitter opp lagene ved mellomrom
    lag = lag.split(" ")

    for i in tippelagliste:
        # Gå gjennom alle lagene i tippeligaen og legger til de
        # om de ikke er i den andre lag-listen
        if i not in lag:
            lag.append(i)

    # Reverserer og returnerer den oppdaterte listen.
    return sorted(lag, reverse=True)


def opprykk(tippelag, oboslag):
    # Fjerner tippelaget og legger til oboslaget i tippeligalisten
    tippelagliste.remove(tippelag)
    tippelagliste.append(oboslag)

    # Reverserer og returnerer tippeligalisten
    return sorted(tippelagliste, reverse=True)


# O P P G A V E  3

valorer = {"kronestykke": 1, "femkrone": 5, "tikrone": 10, "tjuekrone": 20,
           "femtilapp": 50, "hundrelapp": 100, "tohundrelapp": 200,
           "femhundrelapp": 500, "tusenlapp": 1000}

kassabeholdning = {"kronestykke": 5, "femkrone": 5, "tikrone": 5,
                   "tjuekrone": 5, "femtilapp": 5, "hundrelapp": 5,
                   "tohundrelapp": 5, "femhundrelapp": 5, "tusenlapp": 5}


def vekslepenger(betalt, pris):
    veksel = betalt - pris

    if veksel < 0:
        print('Kunden betalte for lite')
    elif not veksel:
        # Dersom veksel er 0
        print('Kunden har betalt akkurat nok')
    else:
        for valor, verdi in reversed(valorer.items()):
            # Går gjennom dictionaryen baklengs, og lagrer nøkler og verdier
            # i variablene valor og verdi.

            # Finner ut hvor mye som trengs av valoren ved å heltallsdividere
            # trekker fra den samlede summen fra veksel
            antall = veksel // verdi
            veksel -= verdi * antall

            # Printer antall og valor dersom antall ikke er null
            if antall:
                print(antall, valor)


def innskudd():
    # Tar inn input med f.eks '2 hundrelapp'
    verdi = input('Skriv hva du vil sette inn i banken: \n')

    # Deler opp inputen i to deler, antall og valor
    antall = int(verdi.split(' ')[0])
    valor = verdi.split(' ')[1]

    # Legger til antall av valor i kassabeholdingen og returnerer den
    kassabeholdning[valor] += antall
    return kassabeholdning


def uttak(belop):
    if belop < 0:
        # Returnerer False siden man ikke kan ta ut negative penger
        return False
    else:
        for valor in reversed(valorer):
            # Går gjennom listen valorer baklengs, slik at de største
            # verdiene kommer først
            while kassabeholdning[valor] > 0 and belop >= valorer[valor]:
                # Trekker fra 1 av valoren i kassabeholdningen dersom det
                # det er nok igjen i beholdningen og beløpet som skal tas ut
                # er større en valoren.
                kassabeholdning[valor] -= 1

                # Trekker fra en sum med samme verdi som valoren fra belop
                belop -= valorer[valor]

    return kassabeholdning


def pengebehandling(metode):
    # Tar inn argumentet metode, som skal være et navn på en funksjon
    if metode == uttak:
        # Tar inn input om funksjonen er 'uttak' siden den krever argument
        verdi = int(input('Hvor mye vil du ta ut av banken? \n'))
        metode(verdi)
    else:
        metode()


# Eksempler av hvordan man kan kalle paa funksjonene

# vekslepenger(108, 80)
# innskudd()
# print(uttak(6000))
# pengebehandling(innskudd)
