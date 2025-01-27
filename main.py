import random
#sorok: 10 - folyoso - 10 
nezoter = []
vasarolt = 0
talaltsor = 0
def kiir_nezoter():
    for i in range(len(nezoter)-1):
        print(i+1, nezoter[i])

def feltolt():
    for i in range(16):
        sor = []
        for i in range(0, 21):
            if i == 10:
                sor.append("T") # folyosó -> TILTOTT
            else:
                hely = random.choice(["F", "D", "G", "U"]) # Felnőtt, Diák, Gyerek, Ures
                sor.append(hely)
        nezoter.append(sor)
    kiir_nezoter()

def mellett():
    kell = vasarolt
    for i in range(len(nezoter)-1):
        sor = nezoter[i]
        talaltures = 0
        print("sor", i)
        for szek in sor:
            
            if szek == "U":
                talaltures += 1
            else:
                talaltures = 0
            if talaltures == kell:
                return i
                
            
            

def vasarlas():
    print("Hány jegyet szeretne vásárolni? (2-5 között): ")
    vasarolt = int(input())
    if vasarolt < 2 or vasarolt > 5:
        vasarlas()
    

def main():
    feltolt()
    vasarlas()
    print(mellett())

main()