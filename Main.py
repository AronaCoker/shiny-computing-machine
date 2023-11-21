import random

rn = random.randrange(0, 100)


def numberGame():
    i = 0
    try:
        userI = int(input("Gebe eine Zahl ein:"))
    except ValueError:
        print("Nur zahlen sind erlaubt")

    while rn != userI:

        if userI < rn:
            print("Deine Zahl ist kleiner")

            userI = int(input("Gebe eine Zahl ein:"))
            i += 1
        elif userI > rn:
            print("Deine Zahl ist Größer")

            userI = int(input("Gebe eine Zahl ein:"))
            i += 1
        if userI == rn:
            i += 1
            print(f"du hast die zahl erraten es war {rn} du hast {i} versuche gebraucht")


numberGame()
