kontostand = float(input("Wie viel Geld hast du auf dem Konto?"))
zinsen = float(input("Was ist dein aktueller Jahreszins?"))
gewollter_kontostand = float(input("Wie viel Geld möchtest du auf den Konto haben?"))
A = zinsen/100
B = kontostand*A
i = 0
if kontostand > gewollter_kontostand:
    print("Du merkst schon, dass das keinen Sinn macht, oder?")
    exit(1)
while gewollter_kontostand > kontostand:
    A = zinsen / 100
    B = kontostand * A
    kontostand += B
    i += 1
if i == 1:
    print(f"Du musst 1 Jahr warten, um {gewollter_kontostand} nur durch Zinsen auf dem Konto zu haben.")
else:
    print(f"Du musst {i} Jahre lang warten, um {gewollter_kontostand} nur durch Zinsen auf dem Konto zu haben.")
