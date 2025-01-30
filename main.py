import random

nezoter = []
def kiir_nezoter():
    print("Nézőtér\nF = felnőtt jegy; D = diák/nyugdíjas jegy; G = gyermek jegy; U = üres szék; T = folyosó")
    for i in range(len(nezoter)):
        print(i+1, nezoter[i])

def feltolt():
    for i in range(15):
        sor = []
        for i in range(0, 21):
            if i == 10:
                sor.append("T") # folyosó -> TILTOTT
            else:
                hely = random.choice(["F", "D", "G", "U"]) # Felnőtt, Diák, Gyerek, Ures
                sor.append(hely)
        nezoter.append(sor)
    kiir_nezoter()

def mellett(kell):
    for i in range(len(nezoter)):
        sor = nezoter[i]
        talaltures = 0
        for szek in sor:
            if szek == "U":
                talaltures += 1
            else:
                talaltures = 0
            
            if talaltures == kell:
                return i+1
    return 0

def vasarlas():
    print("Hány jegyet szeretne vásárolni? (2-5 között): ", end="")
    try:
        vasarolt = int(input())
    except:
        print("Kérem csak számokat adjon meg!")
        return vasarlas()
    if vasarolt < 2 or vasarolt > 5:
        print("Kérem 2 és 5 között legyen a jegyek száma!")
        return vasarlas()
    return vasarolt

def szekszamlalo():
    osszeg = 0
    ures = 0
    teljesaru = 0
    for sor in nezoter:
        for szek in sor:
            if szek == "U":
                ures += 1
            elif szek == "F":
                osszeg += 2500
                teljesaru +=1
            elif szek == "D":
                osszeg += 2100
            elif szek == "G":
                osszeg += 1300
    return [osszeg, ures, teljesaru]

def kihasznSzamolo(ures):
    return round(((300-ures) / 300)*100, 2)

def main():
    feltolt()
    vasarolt = vasarlas()
    talaltsor = mellett(vasarolt)

    if talaltsor == 0:
        print(f"Sajnos nincs olyan sor ahol {vasarolt}db szék egymás mellett szabad lenne.")
    else:
        print(f"A {talaltsor}. sorban van egymás mellett {vasarolt}db üres szék.")

    stat = szekszamlalo()

    print(f"A mozi bevétele erre az előadásra: {stat[0]}Ft")
    
    kihasznaltsag = kihasznSzamolo(stat[1])

    print(f"A terem kihasználtsága ezen az előadáson: {kihasznaltsag}%")

    print(f"{stat[2]}db teljes árú jegyet értékesítettek.")

main()