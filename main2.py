import os, random
from helyszinek import gyomore, gyor, iskola
def vesztettel():
    print("Vesztettel!")
    v = input("Szeretned Ujrakezdeni?\n1 - Igen\n2 - Nem\n")
    if v =="1":
        pass
    elif v == "2":
        exit
def main():
    global energia
    global penz
    global hely

    def jatek():
        global energia
        global penz
        global hely
        os.system("cls")
        print("Gyor Simulator 2\n1 - Start\n2 - Kilepes")
        v = input("Valasztas: ")
        energia = 100
        penz = 2500
        match v:
            case "1":
                os.system("cls")
                hely = gyomore()
                v= input(f"Sajnos a vonatod {random.randint(1,121)} percet kesik.\nMegvarod?\n1 - Igen\n2 - Nem\n")
                if v == "1":
                    pass
                elif v =="2":
                    os.system("cls")
                    print("Hazamentel, mert konnyen feladod az almaid. Igy nem erdemled meg azt, hogy eljuss Becsbe.")
                    vesztettel()
            case "2":
                exit
        print(f'Energia: {energia}%', end='\t\t')
        print(f'Egyenleg: {penz}Ft', end='\t\t')
        hely = gyor()
        v = input()
        if v == 1:
            iskola()
            v = input()
            if v == "1":
                energia -= 40
    jatek()
main()