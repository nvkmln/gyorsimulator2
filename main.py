import os, random
from helyszinek import gyomore, gyor, iskola

def vesztettel():
    global energia
    global penz
    if energia == 0 or energia < 0:
        energia == 0
        print("Vesztettel!")
        v = input("Szeretned Ujrakezdeni?\n1 - Igen\n2 - Nem\n")
        if v =="1":
            pass
        elif v == "2":
            exit
    if penz == 0 or penz < 0:
        penz == 0
        print("Vesztettel!")
        v = input("Szeretned Ujrakezdeni?\n1 - Igen\n2 - Nem\n")
        if v =="1":
            pass
        elif v == "2":
            exit
os.system("cls")
print("Gyor Simulator 2\n1 - Start\n2 - Kilepes")
v = input("Valasztas: ")

def main():
    global energia
    global penz
    global hely
    match v:
        case "1":
                energia = 100
                penz = 2500
                os.system("cls")
                print("Udv a Gyor Simulator 2-ben, ahol ugyanaz a celod, mint az elso kiadasban, hogy megvedd a csodas vonatjegyed Becsbe. Sok szerencset!")
                input("\nENTER")
                os.system("cls")
                energia = 100
                penz = 2500 #eleg egy zacsko dohanyra
                def game():
                    global energia
                    global penz
                    global hely
                    print(f'Energia: {energia}%', end='\t\t')
                    print(f'Egyenleg: {penz}Ft', end='\t\t')
                    hely = gyomore()
                    v = input("\nSzerinted kesik a vonatod?\n1 - Igen\n2 - Nem\n")
                    os.system("cls")
                    if v == "1" or v == "2":
                        print(f'Energia: {energia}%', end='\t\t')
                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                        v= input(f"\nSajnos a vonatod {random.randint(1,121)} percet kesik.\nMegvarod?\n1 - Igen\n2 - Nem\n")
                        if v == "1":
                            pass
                        elif v == "2":
                            os.system("cls")
                            energia = 0
                            penz = 0
                            vesztettel()
                    hely = gyor()
                    v = input("Hova szeretnel menni?")
                game()


main()