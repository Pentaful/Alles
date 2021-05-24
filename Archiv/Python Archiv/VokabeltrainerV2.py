from random import shuffle
total1 = 0 
Lektion2 = {"hodie":"heute", "circus":"Zirkus" or "Rennbahn", "ludus":"Spiel" or "Wettkampf" or "Schule", "sunt":"sie sind" or "sind", "sed": "aber" or "sondern",
            "amicus":"Freund", "diu":"lange Zeit", "exspectare":"erwarten" or "warten", "tandem":"endlich" or "schließlich", "populus":"Volk", "etiam":"auch" or "sogar",
            "nunc":"jetzt" or "nun", "tacere":"schweigen", "porta":"Tor" ,"patere":"offenstehen" or "sich erschrecken", "equus": "Pferd", "accedere":"herbeikommen" or
            "hinzukommen","denique":"schließlich" or "zuletzt", "signum":"Merkmal" or "Zeichen", "dare":"geben", "currere":"eilen" or "laufen","surgere":"aufstehen",
            "vocare":"rufen" or "nennen", "victor":"Sieger", "ecce":"schau" or "schaut!" or "schaut" or "sieh da" or "sieh da!" or "seht da" or "seht da!",
            "praemium": "Belohnung" or "Lohn" or "Preis" or "Siegespreis"}

Lektion16 = {"is, ea, id":"dieser, diese, dieses" or "er, sie, es","nox,noctis":"Nacht", "multa nocte":"in tiefer Nacht", "somnum":"schlaf",
             "animadvertere,animadvero, animadverti": "bemerken" or "wahrnehmen", "surgere, surgo, surrexi": "aufstehen" or "sich erheben",
             "summus, a, um" :"der höchste" or "der letzte" or "der oberste", "pauci, ae, a": "wenige", "ea, quae": "das" or "was", "contendere, contendo, condendi":
             "eilen" or "sich anstrengen", "currere, curro, cucurri":"eilen" or "laufen", "arcessere, arcesso, arcessivi,":"herbeirufen" or "hohlen", "imperare, impero":
             "befehlen" or "herrschen" or "herrschen über", "claudere, claudo, clausi":"abschließen" or "einschließen", "primus, a, um":"der erste", "lux, lucix":"licht" or
             "Tageslicht", "prima luce":"bei Tageslicht", "profecto":"sicherlich" or "tatsächlich", "duo, duae, duo":"zwei", "stare, sto, steti":"stehen",
             "discedere, discedo, discessi":"auseinandergehen" or "weggehen", "convocare, convoco":"versammeln", "defendere, defendo, defendi":"verteitigen" or "abwehren" or
             "schützen", "insidiae, insidiarum":"auseinandergehen" or "weggehen", "insidias":"eine Falle stellen", "vitare, vito":"meiden" or "vermeiden",
             "monere, moneo, monui" : "ermahnen" or "(er)mahnen", "postulare, postulo" : "schlagen" or "vertreiben", "mittere, mitto, misi":"loslassen" or "(los)lassen" or
             "schicken" or "werfen", "restare, resto, restiti":"übrig bleiben" or "widerstand leisten", "dare, do, dedi":"geben", "institurere, instituo, institui":
             "beginnen" or "einrichten" or "unterrichten"}

def plusOneTotal():
    global total1
    total1 += 1

def Lektion2Abfrage():
    global bad2
    global good2
    good2 = 0 ; bad2 = 0
    going = True
    while going:
        print("Wenn du abbrechen willst, drücke Enter.") # reminder

        keys = list(Lektion2.keys()) # list wird durchmischt
        shuffle(keys)                  # list wird durchmischt

        good2 = bad2 = 0          # idk

        i = 0
        for k in keys:  # idk v2
            i += 1

            answer = input('%d von %d: %s => ' % (i, len(keys), k)).strip() # wtf

            if answer == '':    # answer = enter = ende
                going = False
                break
            elif answer == Lektion2[k]: # idk v1.1
                good2 += 1
                print("+1 Puntke")
                plusOneTotal()
            else:
                bad2 += 1
                print("+0 Punkte")
                plusOneTotal()

        print('Ergebnis : %d richtig, %d falsch' % (good2, bad2)) # wtf v2
        break

def Lektion16Abfrage():
    global good16
    going = True
    while going:
        print("Wenn du abbrechen willst, drücke Enter.") # reminder

        keys = list(Lektion16.keys()) # list wird durchmischt
        shuffle(keys)                  # list wird durchmischt

        good16 = bad16 = 0          # idk

        i = 0
        for k in keys:  # idk v2
            i += 1

            answer = input('%d von %d: %s => ' % (i, len(keys), k)).strip() # wtf

            if answer == '':    # answer = enter = ende
                going = False
                break
            elif answer == Lektion16[k]: # idk v1.1
                good16 += 1
                plusOneTotal()
            else:
                bad16 += 1
                plusOneTotal()

        print('Ergebnis : %d richtig, %d falsch' % (good16, bad16)) # wtf v2
        break
while True:
    befehl = input("Befehl: ")
    if befehl == "abfrage":
        lektionAbfrage = int(input("Lektion?"))
        if lektionAbfrage == 1:
            Lektion1Abfrage()
        elif lektionAbfrage == 2:
            Lektion2Abfrage()
        elif lektionAbfrage == 3:
            Lektion3Abfrage()
        elif lektionAbfrage == 4:
            Lektion4Abfrage()
        elif lektionAbfrage == 5:
            Lektion5Abfrage()
        elif lektionAbfrage == 6:
            Lektion6Abfrage()
        elif lektionAbfrage == 7:
            Lektion7Abfrage()
        elif lektionAbfrage == 8:
            Lektion8Abfrage()
        elif lektionAbfrage == 9:
            Lektion9Abfrage()
        elif lektionAbfrage == 10:
            Lektion10Abfrage()
        elif lektionAbfrage == 11:
            Lektion11Abfrage()
        elif lektionAbfrage == 12:
            Lektion12Abfrage()
        elif lektionAbfrage == 13:
            Lektion13Abfrage()
        elif lektionAbfrage == 14:
            Lektion14Abfrage()
        elif lektionAbfrage == 15:
            Lektion15Abfrage()
        elif lektionAbfrage == 16:
            Lektion16Abfrage()
        elif lektionAbfrage == 17:
            Lektion17Abfrage()
        elif lektionAbfrage == 18:
            Lektion18Abfrage()
        else:
            break
    elif befehl == "exit":
        exit("Programm beendet.")
    elif befehl == "good":
        print(good2)
    elif befehl == "bad":
        print(bad2)
    elif befehl == "verfügbar":
        print("Lektion 1 : \nLektion 2 : \U00002714\U00002714 \nLektion 3 : \nLektion 4 : \nLektion 5 : \nLektion 6 : \nLektion 7 : \nLektion 8 : \nLektion 9 : \nLektion 10 : \nLektion 11 : \nLektion 12 : \nLektion 13 : \nLektion 14 : \nLektion 15 : \nLektion 16 : \U00002714\U00002714\n\n\nLektionen mit einem \U00002714 heißen, dass sie in Arbeit sind. Mit \U00002714\U00002714 heißt es, dass sie fertig sind.")
    elif befehl == "total":
        print(total1)
    else:
        print( "Keine bekannte Ausgabe. Tippe abfrage, verfügbar oder exit ein.")