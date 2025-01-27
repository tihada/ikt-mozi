import random
#sorok: 10 - folyoso - 10 
ulohelyek = []
def nezoter():
    for sor in ulohelyek:
        print(sor)

def feltolt():
    for i in range(15):
        sor = []
        for i in range(0, 21):
            if i == 10:
                sor.append("T") # folyosó -> TILTOTT
            else:
                hely = random.choice(["F", "D", "G", "U"]) # Felnőtt, Diák, Gyerek, Ures
                sor.append(hely)
        ulohelyek.append(sor)
    nezoter()
    

def main():
    feltolt()

main()