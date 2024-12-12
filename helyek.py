import random, os, time


def vesztettel():
    v = 0
    if ora >= 23:
        os.system("cls")
        print(f"Nem erted el az utolso vonatot Becsbe.\nVisszakuldott az elet Gyomorere!")
        time.sleep(3)
        gyomore(v)
    if energia <= 0:
        os.system("cls")
        print(f"\nMeghaltal.\nVisszakuldott az elet Gyomorere!")
        time.sleep(3)
        gyomore(v)
    if penz <=0:
        os.system("cls")
        print(f"\nElfogyott minden penzed.\nVisszakuldott az elet Gyomorere!")
        gyomore(v)
    

def ido(ora: int, perc: int):
    ido = f"{ora}:{perc}"
    if perc > 60:
        ora += perc //60
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
    global menetido
    energia = 100
    penz = 25000
    ora = 6
    perc = 42
    keses = int(random.randint(1,120))
    menetido = keses +26
    os.system("cls")
    statPrinteles(energia, penz)
    ido(ora, perc)
    print("\nAhhoz, hogy eljuss Becsbe, eloszor el kell menj otthonrol Gyorbe, ezert Gyomoren kezdesz.")
    print(f"\nKésik a vonatod {keses} percet. Megvárod?")
    print("1 - Igen \t 2 - Nem")
    v = input("")
    match v:
        case '1':
            v = 0
            perc += menetido
            energia -= random.randint(1,15)
            ido(ora, perc)
            statPrinteles(energia,penz)
            gyor(v)
        case '2':
            os.system("cls")
            print("Ilyen konnyen feladod az almaidat?")
            time.sleep(3)
            vege()
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
    print("\nHelyszin: Gyor, Vasutallomas\n1 - Iskola(Lyedlick)\n2 - Dohanybolt\n3 - Arkad\n4 - Baross ut\n5 - Becsi vonat")
    v = input("")
    match v:
        case "1":
            v = "0"
            iskola(v)
        case "2":
            v = "0"
            dohi(v)
        case "3":
            v = "0"
            energia -=15
            perc += 15
            vesztettel()
            arkad(v)
        case "4":
            v = "0"
            energia -= 5
            perc += 8
            vesztettel()
            barossut(v)
        case "5":
            v = "0"
            becsivonat(v)
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
            perc = 20
            ido(ora,perc)
            gyor(v)
            vesztettel()
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
                            if energia <85:
                                energia += 15
                            elif energia > 85:
                                energia = 100
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
def arkad(v : str):
    global energia
    global penz
    global ora
    global perc
    workhours = 0
    os.system("cls")
    statPrinteles(energia,penz)
    ido(ora,perc)
    print(f"\nHelyszin: Arkad")
    print(f"\n1 - KFC\n2 - WC-s nenizes\n3 - Media Markt\n4 - Kimesz cigizni\n5 - Vissza")
    v = input("")
    match v:
        case "1":
            if penz > 2300:
                if energia < 75:
                    energia +=25
                elif energia >= 75:
                    energia = 100
                else:
                    pass
                v= "0"
                os.system("cls")
                penz -= 2300
                perc += 25
                vesztettel()
                statPrinteles(energia,penz)
                ido(ora,perc)
                print(f"\nEttel egy Grander menut, emellett talalkoztal a haverjaiddal, beszelgettetek egy jot.")
                time.sleep(3)
                arkad(v)
            else:
                v = "0"
                os.system("cls")
                statPrinteles(energia,penz)
                ido(ora,perc)
                print(f"\nNincsen eleg fedezeted az etkezeshez.")
                time.sleep(3)
                arkad(v)
        case "2":
            if workhours < 6:
                    v = 0
                    energia -=5
                    pluszpenz = random.randint(1,10)*50
                    penz += pluszpenz
                    workhours += 1
                    ora += 1
                    os.system("cls")
                    statPrinteles(energia,penz)
                    ido(ora,perc)
                    print(f"\nDolgoztal 1 orat wcs nenikent es {pluszpenz} Ft-ot kerestel.")
                    time.sleep(3)
                    arkad(v)
            else:
                    v = 0
                    os.system("cls")
                    statPrinteles(energia,penz)
                    ido(ora,perc)
                    print(f"\nMa mar dolgoztal eleget. Pihenj egy kicsit!")
                    time.sleep(3)
                    arkad(v)
        case "3":
            if workhours < 6:
                    v = 0
                    energia -=0
                    pluszpenz = 3500
                    penz += pluszpenz
                    workhours += 1
                    ora += 1
                    jackpot = random.randint(1,100)
                    os.system("cls")
                    if jackpot <= 30:
                        os.system("cls")
                        v = 0
                        penz += 500000
                        ora += 1
                        statPrinteles(energia,penz)
                        ido(ora,perc)
                        print(f"\nGratulalok! Te soztad ra a legtobb emberre az eladhatatlan cuccokat!\nFogadd szeretettel a bonuszodat!")
                        time.sleep(5)
                        arkad(v)
                    else:
                        pass
                    statPrinteles(energia,penz)
                    ido(ora,perc)
                    print(f"\nDolgoztal 1 orat a Media Markt-ban es {pluszpenz} Ft-ot kerestel.")
                    time.sleep(3)
                    arkad(v)
            else:
                    v = 0
                    os.system("cls")
                    statPrinteles(energia,penz)
                    ido(ora,perc)
                    print(f"\nMa mar dolgoztal eleget. Pihenj egy kicsit!")
                    time.sleep(3)
                    arkad(v)
        case "5":
            v = "0"
            energia -=15
            perc +=15
            vesztettel()
            gyor(v)
        case default:
            v = "0"
            arkad(v)
def barossut(v : str):
    global energia
    global penz
    global ora
    global perc
    os.system("cls")
    statPrinteles(energia,penz)
    ido(ora,perc)
    print(f"\nHelyszin: Baross ut")
    print(f"\n1 - Eneklos csavo\n2 - Kocsma\n3 - Adventi vasar\n4 - Kukazas\n5 - Vissza")
    v = input("")
def becsivonat(v : str):
    global energia
    global penz
    global ora
    global perc
    os.system("cls")
    if penz >= 15000:
        penz -= 15000
        statPrinteles(energia,penz)
        ido(ora,perc)
        print(f"\nHelyszin: Vasutallomas, Belfoldi Jegypenztar")
        print(f"\nGratulalok! Elerted az almodat, sok sikert kivanunk!")
        time.sleep(3)
        vege()
    else:
        v = 0
        statPrinteles(energia,penz)
        ido(ora,perc)
        print("\nNincs eleg penzed a vonatjegyre, dolgoznod kell meg!")
        time.sleep(2)
        gyor(v)

def vege():
    os.system("cls")
    print("Kettest megeri?")
    time.sleep(5)

