tall = int(input("Tall: "))  # Tar inn input


def fibonacci(n):
    # Definerer startverdiene
    x1 = 0
    x2 = 1
    for i in range(n-1):
        # Legger sammen de to foregående verdiene n-1 antall ganger
        x_gammel = x1
        x1 = x2
        x2 += x_gammel
    return x1


print(fibonacci(tall))
