import random   # liste von txt importieren

result1 = 0
total1 = 0
note1 = 0

def abfrage1():
    def plusOnePoint():
        global result1
        result1 += 1

    def plusOneTotal():
        global total1
        total1 += 1

    def a1():
        inpAntw = input("senator auf deutsch?")
        plusOneTotal()
        if inpAntw == "senator":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_1_list.remove(a1)

    def a2():
        inpAntw = input("forum auf deutsch?")
        plusOneTotal()
        if inpAntw == "marktplatz":
            plusOnePoint()
            print("+1 Punkt")
        elif inpAntw == "forum":
            plusOnePoint()
            print("+1 Punkt")
        elif inpAntw == "öffentlichkeit":
            plusOnePoint()
            print("+1 Punkt")
        else:
            print("+0 Punkte")
        question_1_list.remove(a2)

    def a3():
        inpAntw = input("properare auf deutsch?")
        plusOneTotal()
        if inpAntw == "eilen":
            plusOnePoint()
            print("+1 Punkt")
        elif inpAntw == "sich beeilen":
            plusOnePoint()
            print("+1 Punkt")
        elif inpAntw == "beeilen":
            plusOnePoint()
            print("+1 Punkt")
        else:
            print("+0 Punkte")
        question_1_list.remove(a3)

    def a4():
        inpAntw = input("nam auf deutsch?")
        plusOneTotal()
        if inpAntw == "denn":
            plusOnePoint()
            print("+1 Punkte")
        elif inpAntw == "nämlich":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_1_list.remove(a4)

    def a5():
        inpAntw = input("ibi auf deutsch?")
        plusOneTotal()
        if inpAntw == "dort":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_1_list.remove(a5)

    def a6():
        inpAntw = input("curia auf deutsch?")
        plusOneTotal()
        if inpAntw == "kurie":
            plusOnePoint()
            print("+1 Punkte")
        elif inpAntw == "rathaus":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_1_list.remove(a6)

    def a7():
        inpAntw = input("esse/est auf deutsch?")
        plusOneTotal()
        if inpAntw == "sein":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_1_list.remove(a7)

    def a8():
        inpAntw = input("hic auf deutsch?")
        plusOneTotal()
        if inpAntw == "hier":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_1_list.remove(a8)

    def a9():
        inpAntw = input("turba auf deutsch?")
        plusOneTotal()
        if inpAntw == "menschenmenge":
            plusOnePoint()
            print("+1 Punkte")
        elif inpAntw == "lärm":
            plusOnePoint()
        elif inpAntw == "verwirrung":
            plusOnePoint()
        else:
            print("+0 Punkte")
        question_1_list.remove(a9)

    def a10():
        inpAntw = input("stare auf deutsch?")
        plusOneTotal()
        if inpAntw == "stehen":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_1_list.remove(a10)

    def a11():
        inpAntw = input("et auf deutsch?")
        plusOneTotal()
        if inpAntw == "und":
            plusOnePoint()
            print("+1 Punkte")
        elif inpAntw == "auch":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_1_list.remove(a11)

    def a12():
        inpAntw = input("clamare/clamat auf deutsch?")
        plusOneTotal()
        if inpAntw == "laut rufen":
            plusOnePoint()
            print("+1 Punkte")
        elif inpAntw == "schreien":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_1_list.remove(a12)

    def a13():
        inpAntw = input("ave! auf deutsch?")
        plusOneTotal()
        if inpAntw == "sei gegrüßt!":
            plusOnePoint()
            print("+1 Punkte")
        elif inpAntw == "sei gegrüßt":
            plusOnePoint()
            print("+1 Punkte")
        elif inpAntw == "hallo":
            plusOnePoint()
            print("+1 Punkte")
        elif inpAntw == "hallo!":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_1_list.remove(a13)

    def a14():
        inpAntw = input("gaudare/gaudet auf deutsch?")
        plusOneTotal()
        if inpAntw == "sich freuen":
            plusOnePoint()
            print("+1 Punkte")
        elif inpAntw == "freuen":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_1_list.remove(a14)

    def a15():
        inpAntw = input("salve! auf deutsch?")
        plusOneTotal()
        if inpAntw == "hallo":
            plusOnePoint()
            print("+1 Punkte")
        elif inpAntw == "sei gegrüßt!":
            plusOnePoint()
            print("+1 Punkte")
        elif inpAntw == "sei gegrüßt":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_1_list.remove(a15)

    def a16():
        inpAntw = input("salvete! auf deutsch?")
        plusOneTotal()
        if inpAntw == "seid gegrüßt!":
            plusOnePoint()
            print("+1 Punkte")
        elif inpAntw == "seid gegrüßt":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_1_list.remove(a16)

    def a17():
        inpAntw = input("subito auf deutsch?")
        plusOneTotal()
        if inpAntw == "plötzlich":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_1_list.remove(a17)

    def a18():
        inpAntw = input("servus auf deutsch?")
        plusOneTotal()
        if inpAntw == "sklave":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_1_list.remove(a18)

    def a19():
        inpAntw = input("adesse/adest auf deutsch?")
        plusOneTotal()
        if inpAntw == "da sein":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_1_list.remove(a19)

    def a20():
        inpAntw = input("rogare/rogat auf deutsch?")
        plusOneTotal()
        if inpAntw == "bitten":
            plusOnePoint()
            print("+1 Punkte")
        elif inpAntw == "erbitten":
            plusOnePoint()
            print("+1 Punkte")
        elif inpAntw == "fragen":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_1_list.remove(a20)

    def a21():
        inpAntw = input("ubi? auf deutsch?")
        plusOneTotal()
        if inpAntw == "wo":
            plusOnePoint()
            print("+1 Punkte")
        elif inpAntw == "wo?":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_1_list.remove(a21)

    def a22():
        inpAntw = input("ridere/ridet auf deutsch?")
        plusOneTotal()
        if inpAntw == "lachen":
            plusOnePoint()
            print("+1 Punkte")
        elif inpAntw == "auslachen":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_1_list.remove(a22)

    def a23():
        inpAntw = input("tum auf deutsch?")
        plusOneTotal()
        if inpAntw == "da":
            plusOnePoint()
            print("+1 Punkte")
        elif inpAntw == "damals":
            plusOnePoint()
            print("+1 Punkte")
        elif inpAntw == "darauf":
            plusOnePoint()
            print("+1 Punkte")
        elif inpAntw == "dann":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_1_list.remove(a23)    
    question_1_list = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21,
                       a22, a23]
    loopInt = 0
    while loopInt != 23:
        random.choice(question_1_list)()
        loopInt += 1

    global note1

    if result1 >= 22:
        note1 = 1
    elif int(result1) in range(17, 22):
        note1 = 2
    elif int(result1) in range(12, 17):
        note1 = 3
    elif int(result1) in range(8, 12):
        note1 = 4
    elif int(result1) in range(3, 8):
        note1 = 5
    elif int(result1) in range(2, 1):
        note1 = 6
    elif int(result1) == 0:
        note1 = 6

while True:
    befehl = input('\33[34m' + "Befehl: " + '\x1b[0m')
    if befehl == "abfrage 1":
        abfrage1()
    elif befehl == "beenden":
        exit("Programm beendet.")
    elif befehl == "punkte":  # gesamtpunktzahl auf lektion anpassen/ potenzielle note
        if result1 == 0:
            print(f"Du hast 0 von 0 Punkten. Das wäre eine {note1}.")
        elif result1 and total1 == 0:
            print(f"Beantworte ein paar Fragen, damit du ein paar Punkte erhälst.")
        else:
            print(f"Du hast {result1} von {total1} Punkten. Das wäre eine {note1}.")
    elif befehl == "note1":
        print(note1)
    elif befehl == "noten":
        print("kommt noch")
    elif befehl == "result1":
        print(result1)
    elif befehl == "total1":
        print(total1)
    else:
        print("\x1b[1;31m" + "Keine bekannte Ausgabe. Tippe " + "\x1b[1;32m" + "abfrage [NUMMER DER LEKTION]" +
              '\x1b[0m' + "," + "\x1b[1;32m" + " punkte" + "\x1b[1;31m" + " oder " + "\x1b[1;32m" + "beenden" +
              '\x1b[0m' "\x1b[1;31m" + " ein." + '\x1b[0m')