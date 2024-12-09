import random, os

energia = 100
penz = 2500
ora = 6
perc = 42

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
                os.system("cls")
                statPrinteles(energia,penz)
                ido(ora,perc)
                print(f"\nA csoves kihozott neked egy doboz Kek Sophiane-t")
                print(f"\nFizetsegul adsz neki egy szalat?\n1 - Igen  \t  2 - Nem")
                v  = input("")
        case "2":
            energia -= 25
            os.system("cls")
            statPrinteles(energia,penz)
            ido(ora,perc)
            print("Nagyon fogsz ma pangani.")
            gyor(v)