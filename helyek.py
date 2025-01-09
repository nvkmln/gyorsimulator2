import random, os, time



def vesztettel():
    v = 0
    if perc >= 1380:
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
    

def ido(perc : int):
    ora = perc // 60
    perc = perc % 60
    return print(f"Ido: {ora:}:{perc:02}")
def ido2():
    return print("Ido: reszeg vagy xdd")

def statPrinteles(energia: int, penz: int):
    print(f"Energia:{energia}\t\tPenz: {penz}Ft", end="\t\t")


def gyomore(v: str):
    global energia
    global penz
    global ora
    global perc
    global menetido
    global workhours
    global cigi
    global nyelvtanulas
    cigi = False
    nyelvtanulas = False
    workhours = 0
    energia = 100
    penz = 2500
    perc = 402
    keses = int(random.randint(1,90))
    menetido = keses +26
    os.system("cls")
    statPrinteles(energia, penz)
    ido(perc)
    print("\nAhhoz, hogy eljuss Becsbe, eloszor el kell menj otthonrol Gyorbe, ezert Gyomoren kezdesz.")
    print(f"\nKésik a vonatod {keses} percet. Megvárod?")
    print("1 - Igen \t 2 - Nem")
    v = input("")
    match v:
        case '1':
            v = 0
            perc += menetido
            energia -= random.randint(1,15)
            ido(perc)
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
    ido(perc)
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
    ido(perc)
    print("\nHelyszin: Iskola(Lyedlick)")
    print(f"\nBiztosan be akarsz menni iskolaba?\n1 - Igen  \t  2 - Nem")
    v = input("")
    match v:
        case "1":
                if perc < 535:
                    v = 0
                    iskola2(v)
                else:
                    os.system("cls")
                    statPrinteles(energia,penz)
                    ido(perc)
                    print("\nHelyszin: Iskola(Lyedlick)")   
                    print("\nNem ertel be a masodik oradra sem!\nMar mindegy, beirtak hianyzonak egesz napra, inkabb setalj egyet a varosban.")
                    time.sleep(3)
                    v = 0
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
    global cigi
    os.system("cls")
    statPrinteles(energia,penz)
    ido(perc)
    print(f"\nHelyszin: Nemzeti Dohanybolt")
    print(f"\nMivel nem vagy meg 18 eves, valakit be kell kuldened a dohiba. Mit teszel?\n1 - Bekuldok egy csovest 2 - Nem veszek cigit(-25% energia)")
    v = input("")
    match v:
        case "1":
                if penz >= 1800:
                    penz -= 1800
                    cigi = True
                    os.system("cls")
                    statPrinteles(energia,penz)
                    ido(perc)
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
                            ido(perc)
                            print("\nElszivtatok a csovessel egy cigit, ettol jobb lett mindkettotok napja")
                            time.sleep(3)
                            gyor(v)
                        case "2":
                            os.system("cls")
                            statPrinteles(energia,penz)
                            ido(perc)
                            print(f"\nA csoves megkeselt, mert {random.randint(1,5)} napja pangott es nagyon vagyott egy bunpalcara.")
                            time.sleep(3)
                            energia = 0
                            vesztettel()
                else:
                    os.system("cls")
                    statPrinteles(energia,penz)
                    ido(perc)
                    print(f"\nNincs eleg fedezeted ahhoz, hogy cigit tudj venni.")
        case "2":
            energia -= 25
            os.system("cls")
            statPrinteles(energia,penz)
            ido(perc)
            print("\nNagyon fogsz ma pangani...")
            time.sleep(3)
            gyor(v)
        case default:
            v = 0
            dohi()
def arkad(v : str):
    global energia
    global penz
    global ora
    global perc
    global workhours
    os.system("cls")
    statPrinteles(energia,penz)
    ido(perc)
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
                ido(perc)
                print(f"\nEttel egy Grander menut, emellett talalkoztal a haverjaiddal, beszelgettetek egy jot.")
                time.sleep(3)
                arkad(v)
            else:
                v = "0"
                os.system("cls")
                statPrinteles(energia,penz)
                ido(perc)
                print(f"\nNincsen eleg fedezeted az etkezeshez.")
                time.sleep(3)
                arkad(v)
        case "2":
            workhours += 1
            if workhours <= 6:
                    v = 0
                    energia -=5
                    pluszpenz = random.randint(1,10)*50
                    penz += pluszpenz
                    perc += 60
                    os.system("cls")
                    statPrinteles(energia,penz)
                    ido(perc)
                    print(f"\nDolgoztal 1 orat wcs nenikent es {pluszpenz} Ft-ot kerestel.")
                    time.sleep(3)
                    vesztettel()
                    arkad(v)
            else:
                    v = 0
                    os.system("cls")
                    statPrinteles(energia,penz)
                    ido(perc)
                    print(f"\nMa mar dolgoztal eleget. Pihenj egy kicsit!")
                    time.sleep(3)
                    arkad(v)
        case "3":
            workhours += 1
            jackpot = random.randint(1,100)
            if workhours <= 6:
                    if jackpot <= 30:
                        os.system("cls")
                        v = 0
                        penz += 500000
                        perc += 60
                        statPrinteles(energia,penz)
                        ido(perc)
                        print(f"\nGratulalok! Te soztad ra a legtobb emberre az eladhatatlan cuccokat!\nFogadd orommel a bonuszodat!")
                        time.sleep(5)
                        arkad(v)
                    else:
                        v = 0
                        energia -=15
                        pluszpenz = 3500
                        penz += pluszpenz
                        perc += 60
                        os.system("cls")
                        statPrinteles(energia,penz)
                        ido(perc)
                        print(f"\nDolgoztal 1 orat a Media Markt-ban es {pluszpenz} Ft-ot kerestel.")
                        time.sleep(3)
                        vesztettel()
                        arkad(v)
            else:
                    v = 0
                    os.system("cls")
                    statPrinteles(energia,penz)
                    ido(perc)
                    print(f"\nMa mar dolgoztal eleget. Pihenj egy kicsit!")
                    time.sleep(3)
                    arkad(v)
        case "4":
            v = 0
            os.system("cls")
            if energia <=70 and cigi == True:
                energia = 100
                perc += 10
                statPrinteles(energia,penz)
                ido(perc)
                print(f"\nElszivtal egy cigit, feltoltodtel.\nIrany dolgozni!")
                time.sleep(3)
                arkad(v)
            elif energia > 70:
                statPrinteles(energia,penz)
                ido(perc)
                print(f"\nTulsagosan sok energiad van, hogy cigizz.\nMenj el dolgozni!")
                time.sleep(3)
                arkad(v)
            else:
                statPrinteles(energia,penz)
                ido(perc)
                print(f"\nNincsen cigid! Menj el es vegyel a dohiban!")
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
    ido(perc)
    print(f"\nHelyszin: Baross ut")
    print(f"\n1 - Eneklos csavo\n2 - Kocsma\n3 - Adventi vasar\n4 - Kukazas\n5 - Vissza")
    v = input("")
    match v:
        case  "1":
            v = 0
            os.system("cls")
            energia = 100
            perc += 3
            statPrinteles(energia,penz)
            ido(perc)
            print(f"\nHelyszin: Baross ut")
            print(f"\nTalalkoztal az eneklos csavoval, aki jobb kedvre deritett. :)")
            time.sleep(3)
            barossut(v)
        case "2":
            os.system("cls")
            statPrinteles(energia,penz)
            ido(perc)
            print
            (f"\nHelyszin: Yolo Pub")
            print(f"\nIszol egy sort?\n1 - Igen  \t  2 - Nem")
            v = input("")
            match v:
                case "1":
                    penz = 0
                    perc += 1380
                    os.system("cls")
                    statPrinteles(energia,penz)
                    ido2()
                    print(f"\nHelyszin: Yolo Pub")   
                    print("Sajnos elittad minden penzedet, reszeg vagy, azt sem tudod mennyi az ido.")
                    time.sleep(5)
                    vesztettel()          
                case "2":
                    v = 0
                    os.system("cls")
                    statPrinteles(energia,penz)
                    ido(perc)       
                    print(f"\nMa nem iszol, nem dol ossze a vilag. Majd talan legkozelebb.")
                    time.sleep(5)
                    barossut(v)
        case "3":
            os.system("cls")
            perc = 1380
            statPrinteles(energia,penz)
            ido(perc)
            print(f"\nHelyszin: Adventi vasar")
            print(f"Elvesztel az adventi vasarban, elfeledkeztel mennyi az ido!")
            time.sleep(5)
            vesztettel()    
        case "4":
            elfognak = random.randint(1,100)
            if elfognak <= 45:
                        os.system("cls")
                        statPrinteles(energia,penz)
                        ido(perc)
                        print(f"\nHelyszin: Baross ut")
                        print(f"\nEszrevettek a rendorok, hogy a kukakban turkalsz, ezert bevittek a bortonbe.")
                        energia = 0
                        time.sleep(5)
                        vesztettel()
            else:
                v = 0
                uvegek = random.randint(1,9)
                pluszpenz = uvegek * 50
                penz += pluszpenz
                os.system("cls")
                statPrinteles(energia,penz)
                ido(perc)
                print(f"\nHelyszin: Baross ut")
                print(f"\nSikeresen kukaztal {uvegek} db uveget ezert kerestel {pluszpenz} Ft-ot.")
                time.sleep(3)
                barossut(v)
        case "5":
            energia -= 5
            perc += 8
            v = 0
            gyor(v)
        case default:
            v = 0
            barossut(v)

def becsivonat(v : str):
    global energia
    global penz
    global ora
    global perc
    os.system("cls")
    if penz >= 15000:
        penz -= 15000
        statPrinteles(energia,penz)
        ido(perc)
        print(f"\nHelyszin: Vasutallomas, Belfoldi Jegypenztar")
        print(f"\nGratulalok! Elerted az almodat, sok sikert kivanunk!")
        time.sleep(3)
        vege()
    else:
        v = 0
        statPrinteles(energia,penz)
        ido(perc)
        print("\nNincs eleg penzed a vonatjegyre, dolgoznod kell meg!")
        time.sleep(2)
        gyor(v)



def iskola2(v : str):
    global penz
    global energia
    global cigi
    global nyelvtanulas
    global perc
    os.system("cls")
    if perc > 535 and perc < 540:
        statPrinteles(energia, penz)
        ido(perc)
        print("\nHelyszin: Iskola(Lyedlick)")
        print(f"Felirtak a portan, mert elkestel az elso oradrol!")
        time.sleep(3)
        os.system("cls")
        print(f"\nA masodik orad nemet. Betegseg miatt Csicsay Tanarur helyettesit, mert kivaloan tud nemetul.\nKaptal egy otost, mert nagyon jol dolgoztal az oran!")
        nyelvtanulas = True
        perc = 580
        pass
    if perc < 480:
        perc = 481
    if perc > 480 and perc < 525:
        statPrinteles(energia, penz)
        ido(perc)
        print("\nHelyszin: Iskola(Lyedlick)")
        print(f"Beertel az elso oradra, igaz kestel egy kicsit.")
        time.sleep(3)
        os.system("cls")
        statPrinteles(energia, penz)
        ido(perc)
        print("\nHelyszin: Iskola(Lyedlick)")
        print(f"\nAz elso orad matek. Kastal Tanarno beirt egy egyest, mert nem volt meg a hazid.\nEzert otthon biztosan kapsz!")
        perc = 525
        time.sleep(2)
        print("SZUNET")
        time.sleep(2)
        os.system("cls")
        statPrinteles(energia, penz)
        ido(perc)
        perc = random.randint(535,580)
        time.sleep(2)
        os.system("cls")
        statPrinteles(energia, penz)
        ido(perc)
        print("\nHelyszin: Iskola(Lyedlick)")
        print(f"\nA masodik orad nemet. Betegseg miatt Csicsay Tanarur helyettesit, mert kivaloan tud nemetul.\nKaptal egy otost, mert nagyon jol dolgoztal az oran!")
        nyelvtanulas = True
        perc = random.randint(590,635)
        time.sleep(3)
        print("SZUNET")
        perc = random.randint(650,695)
        time.sleep(3)
        os.system("cls")
        statPrinteles(energia, penz)
        ido(perc)
        print("\nHelyszin: Iskola(Lyedlick)")
        print(f"\nA harmadik orad tortenelem. Nem figyeltel semmit ,mert vegig telefonoztal.\nKozben a padod 1.5 metert arreb mozdult amit sem te, sem a tanarur nem vett eszre.")
        nyelvtanulas = True
        perc = random.randint(650,695)
        time.sleep(3)
        print("SZUNET")
        perc = 695
        time.sleep(3)
        os.system("cls")
        statPrinteles(energia, penz)
        ido(perc)
        print("\nHelyszin: Iskola(Lyedlick)")
        print(f"\nA negyedik orad jon, a fizika. A tanarno megkeri, hogy demonstrald a kiserletet az alkohol egeserol.")
        perc = random.randint(705,750)
        time.sleep(3)




def vege():
    os.system("cls")
    print("Kettest megeri?")
    time.sleep(5)

