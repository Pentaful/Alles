import random  # liste von txt importieren

result1 = 0
result2 = 0
totalAnswered = 0
note1 = "GRADE_NOT_CALCULATED"
note2 = "GRADE_NOT_CALCULATED"

def abfrage1():
    def plusOnePoint():
        global result1
        result1 += 1

    def plusOneTotal():
        global totalAnswered
        totalAnswered += 1

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
    else:
        note1 = 6

def abfrage16():
    def plusOnePoint():
        global result2
        result2 += 1

    def plusOneTotal():
        global totalAnswered
        totalAnswered += 1

    def b1():
        inpAntw = input("senator auf deutsch?")
        plusOneTotal()
        if inpAntw == "senator":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_2_list.remove(b1)

    def b2():
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
        question_2_list.remove(b2)

    def b3():
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
        question_2_list.remove(b3)

    def b4():
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
        question_2_list.remove(b4)

    def b5():
        inpAntw = input("ibi auf deutsch?")
        plusOneTotal()
        if inpAntw == "dort":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_2_list.remove(b5)

    def b6():
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
        question_2_list.remove(b6)

    def b7():
        inpAntw = input("esse/est auf deutsch?")
        plusOneTotal()
        if inpAntw == "sein":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_2_list.remove(b7)

    def b8():
        inpAntw = input("hic auf deutsch?")
        plusOneTotal()
        if inpAntw == "hier":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_2_list.remove(b8)

    def b9():
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
        question_2_list.remove(b9)

    def b10():
        inpAntw = input("stare auf deutsch?")
        plusOneTotal()
        if inpAntw == "stehen":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_2_list.remove(b10)

    def b11():
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
        question_2_list.remove(b11)

    def b12():
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
        question_2_list.remove(b12)

    def b13():
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
        question_2_list.remove(b13)

    def b14():
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
        question_2_list.remove(b14)

    def b15():
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
        question_2_list.remove(b15)

    def b16():
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
        question_2_list.remove(b16)

    def b17():
        inpAntw = input("subito auf deutsch?")
        plusOneTotal()
        if inpAntw == "plötzlich":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_2_list.remove(b17)

    def b18():
        inpAntw = input("servus auf deutsch?")
        plusOneTotal()
        if inpAntw == "sklave":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_2_list.remove(b18)

    def b19():
        inpAntw = input("adesse/adest auf deutsch?")
        plusOneTotal()
        if inpAntw == "da sein":
            plusOnePoint()
            print("+1 Punkte")
        else:
            print("+0 Punkte")
        question_2_list.remove(b19)

    def b20():
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
        question_2_list.remove(b20)

    def b21():
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
        question_2_list.remove(b21)

    def b22():
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
        question_2_list.remove(b22)

    def b23():
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
        question_2_list.remove(b23)

    def b24():
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
        question_2_list.remove(b24)

    def b25():
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
        question_2_list.remove(b25)

    def b26():
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
        question_2_list.remove(b26)    
    question_2_list = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21,
                       b22, b23, b24, b25, b26]
    loopInt = 0
    while loopInt != 26:
        random.choice(question_2_list)()
        loopInt += 1

    global note2

    if result1 >= 22:
        note2 = 1
    elif int(result1) in range(17, 22):
        note2 = 2
    elif int(result1) in range(12, 17):
        note2 = 3
    elif int(result1) in range(8, 12):
        note2 = 4
    elif int(result1) in range(3, 8):
        note2 = 5
    elif int(result1) in range(2, 1):
        note2 = 6
    else:
        note2 = 6

while True:
    befehl = input("Befehl: ")
    if befehl == "abfrage":
        lektionAbfrage = int(input("Lektion?"))
        lektionAbfrage
        if lektionAbfrage == 1:
            abfrage1()
        elif lektionAbfrage == 16:
            abfrage16()
    elif befehl == "beenden":
        exit("Programm beendet.")
    elif befehl == "punkte":  # gesamtpunktzahl auf lektion anpassen/ potenzielle note
        punkteWelche = int(input("Lektion?"))
        if punkteWelche == 1:
            if result1 == 0 and totalAnswered != 0:
                print("Du hast 0 von ",totalAnswered," Punkten. Das wäre eine",note1,".")
            elif result1 and totalAnswered == 0:
                print("Beantworte ein paar Fragen, damit du ein paar Punkte erhälst.")
            else:
                print("Du hast",result1,"von " ,totalAnswered, " Punkten. Das wäre eine",note1,".")
        elif punkteWelche == 16:
            if result2 == 0 and totalAnswered != 0:
                print("Du hast 0 von ",totalAnswered," Punkten. Das wäre eine",note2,".")
            elif result2 and totalAnswered == 0:
                print("Beantworte ein paar Fragen, damit du ein paar Punkte erhälst.")
            else:
                print("Du hast",result2,"von " ,totalAnswered, " Punkten. Das wäre eine",note2,".")
    elif befehl == "note":
        noteLektion = int(input("Lektion?"))
        if lektionAbfrage == 1:
            print(note1)
        elif lektionAbfrage == 16:
            print(note2)
    elif befehl == "noten":
        print("kommt noch")
    elif befehl == "result1":
        print(result1)
    elif befehl == "totalAnswered":
        print(totalAnswered)
    elif befehl == "lektionen":
        print("Lektion 1 : \U00002714\U00002714\nLektion 2 : \nLektion 3 : \nLektion 4 : \nLektion 5 : \nLektion 6 : \nLektion 7 : \nLektion 8 : \nLektion 9 : \nLektion 10 : \nLektion 11 : \nLektion 12 : \nLektion 13 : \nLektion 14 : \nLektion 15 : \nLektion 16 : \U00002714\n\n\nLektionen mit einem \U00002714 heißen, dass sie in Arbeit sind. Mit \U00002714\U00002714 heißt es, dass sie fertig sind.")
    elif befehl == "help" or "hilfe":
        print("Liste der Commands: abfrage, note, noten (kommt noch), ")
    else:
        print( "Keine bekannte Ausgabe. Tippe 'help' oder 'hilfe' ein.")