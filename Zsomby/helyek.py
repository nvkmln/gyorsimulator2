import random, os, time

energia = 100
penz = 2500
ora = 6
perc = 42
def main():
    global energia
    global penz
    global ora
    global perc
    os.system('cls')
    print("Gyor simulator 2")
    print("\n1 - Start \t 2 - Kilepes")
    v = input("")
    match v:
        case '1':
            os.system('cls')
            print("Udv a Gyor Simulator 2-ben, ahol ugyanaz a celod, mint az elso kiadasban, hogy megvedd a csodas vonatjegyed Becsbe. Sok szerencset!")
            input("\nENTER")
            v = 0
            gyomore(v)
        case '2':
            pass
        case default:
            main()


def vesztettel():
    if ora >= 23:
        os.system("cls")
        print(f"Nem erted el az utolso vonatot Becsbe \nVesztettel!")
        time.sleep(3)
        main()
    if energia <= 0:
        os.system("cls")
        print(f"\nMeghaltal.\nVesztettel!")
        time.sleep(3)
        main()

def ido(ora: int, perc: int):
    ido = f"{ora}:{perc}"
    if perc > 60:
        ora += 1
        perc = perc % 60
        ido = f"{ora}:{perc}"
    elif perc == 60:
        ora += 1
        perc = 0
        ido = f"{ora}:{perc}0"
    elif perc > 0 and perc < 10:
        ido = f"{ora}:0{perc}"
    elif perc == 0:
        ido = f"{ora}:0{perc}"
    return print(ido)

def statPrinteles(energia: int, penz: int):
    print(f"Energia:{energia}\t\tPenz: {penz}Ft", end="\t\t")


def gyomore(v: str):
    global energia
    global penz
    global ora
    global perc
    energia = 100
    penz = 2500
    ora = 6
    perc = 42
    os.system("cls")
    statPrinteles(energia, penz)
    ido(ora, perc)
    keses = random.randint(1,120)
    print("\nAhhoz, hogy eljuss Becsbe, eloszor el kell menj otthonrol Gyorbe, ezert Gyomoren kezdesz.")
    print(f"\nKésik a vonatod {keses} percet. Megvárod?")
    print("1 - Igen \t 2 - Nem")
    v = input("")
    match v:
        case '1':
            v = 0
            perc += 26
            perc += keses
            energia -= random.randint(1,15)
            ido(ora, perc)
            gyor(v)
        case '2':
            print("Ha nem akarsz jatszani minek nyitottad meg?")
            exit
        case default:
            gyomore(v)


def gyor(v : str):
    vesztettel()
    global energia
    global penz
    global ora
    global perc
    os.system("cls")
    statPrinteles(energia,penz)
    ido(ora,perc)
    print("\nHelyszin: Gyor, Vasutallomas\n1 - Iskola(Lyedlick)\n2 - Dohanybolt\n3 - Arkad\n4 - Baross ut\n6 - Becsi vonat")
    v = input("")
    match v:
        case "1":
            iskola(v)
        case "2":
            dohi(v)
        case default:
            gyor(v)
    
def iskola(v : str):
    vesztettel()
    global energia
    global penz
    global ora
    global perc
    os.system("cls")
    statPrinteles(energia,penz)
    ido(ora,perc)
    print("\nHelyszin: Iskola(Lyedlick)")
    print(f"\nBiztosan be akarsz menni iskolaba?\n1 - Igen  \t  2 - Nem")
    v = input("")
    match v:
        case "1":
            energia -= random.randint(1,15)
            ora += 7
            perc += 20
            gyor(v)
        case "2":
            gyor(v)
        case default:
            iskola(v)
def dohi(v : str):
    global energia
    global penz
    global ora
    global perc
    os.system("cls")
    statPrinteles(energia,penz)
    ido(ora,perc)
    print(f"\nHelyszin: Nemzeti Dohanybolt")
    print(f"\nMivel nem vagy meg 18 eves, valakit be kell kuldened a dohiba. Mit teszel?\n1 - Bekuldok egy csovest 2 - Nem veszek cigit(-25% energia)")
    v = input("")
    match v:
        case "1":
                if penz >= 1800:
                    penz -= 1800
                    os.system("cls")
                    statPrinteles(energia,penz)
                    ido(ora,perc)
                    print(f"\nA csoves kihozott neked egy doboz Kek Sophiane-t")
                    print(f"\nFizetsegul adsz neki egy szalat?\n1 - Igen  \t  2 - Nem")
                    v  = input("")
                    match v:
                        case "1":
                            if energia <=85:
                                energia += 15
                            perc += 10
                            os.system("cls")
                            statPrinteles(energia,penz)
                            ido(ora,perc)
                            print("\nElszivtatok a csovessel egy cigit, ettol jobb lett mindkettotok napja")
                            time.sleep(3)
                            gyor(v)
                        case "2":
                            os.system("cls")
                            statPrinteles(energia,penz)
                            ido(ora,perc)
                            print(f"\nA csoves megkeselt, mert {random.randint(1,5)} napja pangott es nagyon vagyott egy bunpalcara.")
                            time.sleep(3)
                            energia = 0
                            vesztettel()
                else:
                    os.system("cls")
                    statPrinteles(energia,penz)
                    ido(ora,perc)
                    print(f"\nNincs eleg fedezeted ahhoz, hogy cigit tudj venni.")
        case "2":
            energia -= 25
            os.system("cls")
            statPrinteles(energia,penz)
            ido(ora,perc)
            print("\nNagyon fogsz ma pangani...")
            time.sleep(3)
            gyor(v)

main()