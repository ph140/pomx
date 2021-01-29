# Tar inn input fra brukeren.
navn = input("Navn: ")
alder = int(input("Alder: "))


if alder < 18:
    print(f"Hei å hopp {navn}, du er for ung til å kjøre!")
else:
    print(f"Hei å hopp {navn}, du er gammel nok til å kjøre!")
