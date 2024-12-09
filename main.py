import os, random, time
from helyszinek import gyomore, gyor, iskola, dohanybolt, arkad
from actions import cigizes

def vesztettel():
    global energia
    global penz
    if energia == 0 or energia < 0:
        energia == 0
        print("Elfogyott minden energiad, meghaltal egy szivrohamban. Vesztettel!")
        v = input("Szeretned Ujrakezdeni?\n1 - Igen\n2 - Nem\n")
        if v =="1":
            main()
        elif v == "2":
            exit
    elif penz == 0 or penz < 0:
        print("Elfogyott minden penzed, nem vesznek fel munkaba, sajnos ujra kell kezdened az eleted.  Vesztettel!")
        v = input("Szeretned Ujrakezdeni?\n1 - Igen\n2 - Nem\n")
        if v =="1":
            main()
        elif v == "2":
            exit
os.system("cls")
print("Gyor Simulator 2\n1 - Start\n2 - Kilepes")
v = input("Valasztas: ")

def main():
    global energia
    global penz
    global hely
    global cigi
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
                            energia -= random.randint(1,5)
                        elif v == "2":
                            os.system("cls")
                            energia = 0
                            penz = 0
                            print("Hazamentel, mert konnyen feladod az almaid. Igy nem erdemled meg azt, hogy eljuss Becsbe.")
                            vesztettel()
                    os.system("cls")
                    print(f'Energia: {energia}%', end='\t\t')
                    print(f'Egyenleg: {penz}Ft', end='\t\t')
                    hely = gyor()
                    v = input("\nHova szeretnel menni? ")
                    if v == "1":
                        os.system("cls")
                        print(f'Energia: {energia}%', end='\t\t')
                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                        hely = iskola()
                        v = input("")
                        if v == "1":
                            pass
                        elif v == "2":
                            os.system("cls")
                            energia -= 40
                            vesztettel()
                        os.system("cls")
                        print(f'Energia: {energia}%', end='\t\t')
                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                        gyor()
                        v = input("\nHova szeretnel menni? ")
                    if v == "2":
                        os.system("cls")
                        energia -= random.randint(1,5)
                        print(f'Energia: {energia}%', end='\t\t')
                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                        hely = dohanybolt()
                        v = input("")
                        if v == "1" and penz > 1800:
                            penz -=1800
                            os.system("cls")
                            print(f'Energia: {energia}%', end='\t\t')
                            print(f'Egyenleg: {penz}Ft', end='\t\t')
                            v = input("\nA csoves kihozott neked egy Marlboro Touch fustszuros cigarettat. Adsz neki borravalot?\n1 - Igen(-300Ft)\n2 - Nem\n")
                        elif v == "2":
                            os.system("cls")
                            energia -= 15
                            print(f'Energia: {energia}%', end='\t\t')
                            print(f'Egyenleg: {penz}Ft', end='\t\t')
                            print("\nNem vettel cigit, pangani fogsz egesz nap.")
                            time.sleep(3)
                            vesztettel()
                            pass
                        elif v == "1" and penz <= 1800:
                            os.system("cls")
                            print(f'Energia: {energia}%', end='\t\t')
                            print(f'Egyenleg: {penz}Ft', end='\t\t')
                            print("\nNincs eleg fedezeted arra, hogy cigit vegyel, egesz nap pangani fogsz.")
                            time.sleep(2)
                            pass
                            if v == "1" and penz > 300:
                                penz -=300
                                os.system("cls")
                                print(f'Energia: {energia}%', end='\t\t')
                                print(f'Egyenleg: {penz}Ft', end='\t\t')
                                print("\nA csoves boldog lett, te pedig nyugodtan mehetsz iskolaba.(Felteve ha szeretnel)")
                                os.system("cls")
                                pass
                            else:
                                penz = 0
                                os.system("cls")
                                print(f'Energia: {energia}%', end='\t\t')
                                print(f'Egyenleg: {penz}Ft', end='\t\t')
                                print("\nA csoves elvette az osszes penzedet.")
                                time.sleep(2)
                                os.system("cls")
                                vesztettel()
                        os.system("cls")
                        print(f'Energia: {energia}%', end='\t\t')
                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                        hely = gyor()
                        v = input("\nHova szeretnel menni? ")
                    if v == "3":
                        os.system("cls")
                        print(f'Energia: {energia}%', end='\t\t')
                        print(f'Egyenleg: {penz}Ft', end='\t\t')
                        hely = arkad()
                        v = input("Hova szeretnel menni? ")


                game()


main()