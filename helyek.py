import random, os, time



def vesztettel():
    v = 0
    if perc >= 1380:
        os.system("cls" if os.name =="nt" else "clear")
        print(f"Nem erted el az utolso vonatot Becsbe.\nVisszakuldott az elet Gyomorere!")
        time.sleep(3)
        gyomore(v)
    if energia <= 0:
        os.system("cls" if os.name =="nt" else "clear")
        print(f"\nMeghaltal.\nVisszakuldott az elet Gyomorere!")
        time.sleep(3)
        gyomore(v)
    if penz <=0:
        os.system("cls" if os.name =="nt" else "clear")
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
    keses = int(random.randint(1,95))
    menetido = keses +26
    os.system("cls" if os.name =="nt" else "clear")
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
            os.system("cls" if os.name =="nt" else "clear")
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
    os.system("cls" if os.name =="nt" else "clear")
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
    os.system("cls" if os.name =="nt" else "clear")
    statPrinteles(energia,penz)
    ido(perc)
    print("\nHelyszin: Iskola(Lyedlick)")
    print(f"\nBiztosan be akarsz menni iskolaba?\n1 - Igen  \t  2 - Nem")
    v = input("")
    match v:
        case "1":
                if perc < 525:
                    v = 0
                    iskola2(v)
                elif perc >= 860:
                    os.system("cls" if os.name =="nt" else "clear")
                    statPrinteles(energia,penz)
                    ido(perc)
                    print("\nHelyszin: Iskola(Lyedlick)")   
                    print("\nMar vege a sulinak, legkozelebb reggel gyere be!")
                    time.sleep(3)
                    v = 0
                    gyor(v)             
                else:
                    os.system("cls" if os.name =="nt" else "clear")
                    statPrinteles(energia,penz)
                    ido(perc)
                    print("\nHelyszin: Iskola(Lyedlick)")   
                    print("\nNem ertel be az elso oradra!\nMar mindegy, beirtak hianyzonak egesz napra, inkabb setalj egyet a varosban.")
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
    os.system("cls" if os.name =="nt" else "clear")
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
                    os.system("cls" if os.name =="nt" else "clear")
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
                            os.system("cls" if os.name =="nt" else "clear")
                            statPrinteles(energia,penz)
                            ido(perc)
                            print("\nElszivtatok a csovessel egy cigit, ettol jobb lett mindkettotok napja")
                            time.sleep(3)
                            gyor(v)
                        case "2":
                            os.system("cls" if os.name =="nt" else "clear")
                            statPrinteles(energia,penz)
                            ido(perc)
                            print(f"\nA csoves megkeselt, mert {random.randint(1,5)} napja pangott es nagyon vagyott egy bunpalcara.")
                            time.sleep(3)
                            energia = 0
                            vesztettel()
                else:
                    os.system("cls" if os.name =="nt" else "clear")
                    statPrinteles(energia,penz)
                    ido(perc)
                    print(f"\nNincs eleg fedezeted ahhoz, hogy cigit tudj venni.")
        case "2":
            energia -= 25
            os.system("cls" if os.name =="nt" else "clear")
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
    os.system("cls" if os.name =="nt" else "clear")
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
                os.system("cls" if os.name =="nt" else "clear")
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
                os.system("cls" if os.name =="nt" else "clear")
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
                    os.system("cls" if os.name =="nt" else "clear")
                    statPrinteles(energia,penz)
                    ido(perc)
                    print(f"\nDolgoztal 1 orat wcs nenikent es {pluszpenz} Ft-ot kerestel.")
                    time.sleep(3)
                    vesztettel()
                    arkad(v)
            else:
                    v = 0
                    os.system("cls" if os.name =="nt" else "clear")
                    statPrinteles(energia,penz)
                    ido(perc)
                    print(f"\nMa mar dolgoztal eleget. Pihenj egy kicsit!")
                    time.sleep(3)
                    arkad(v)
        case "3":
            workhours += 1
            jackpot = random.randint(0,100)
            if workhours <= 6:
                    if jackpot <= 30:
                        os.system("cls" if os.name =="nt" else "clear")
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
                        os.system("cls" if os.name =="nt" else "clear")
                        statPrinteles(energia,penz)
                        ido(perc)
                        print(f"\nDolgoztal 1 orat a Media Markt-ban es {pluszpenz} Ft-ot kerestel.")
                        time.sleep(3)
                        vesztettel()
                        arkad(v)
            else:
                    v = 0
                    os.system("cls" if os.name =="nt" else "clear")
                    statPrinteles(energia,penz)
                    ido(perc)
                    print(f"\nMa mar dolgoztal eleget. Pihenj egy kicsit!")
                    time.sleep(3)
                    arkad(v)
        case "4":
            v = 0
            os.system("cls" if os.name =="nt" else "clear")
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
    os.system("cls" if os.name =="nt" else "clear")
    statPrinteles(energia,penz)
    ido(perc)
    print(f"\nHelyszin: Baross ut")
    print(f"\n1 - Eneklos csavo\n2 - Kocsma\n3 - Adventi vasar\n4 - Kukazas\n5 - Vissza")
    v = input("")
    match v:
        case  "1":
            v = 0
            os.system("cls" if os.name =="nt" else "clear")
            energia = 100
            perc += 3
            statPrinteles(energia,penz)
            ido(perc)
            print(f"\nHelyszin: Baross ut")
            print(f"\nTalalkoztal az eneklos csavoval, aki jobb kedvre deritett. :)")
            time.sleep(3)
            barossut(v)
        case "2":
            os.system("cls" if os.name =="nt" else "clear")
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
                    os.system("cls" if os.name =="nt" else "clear")
                    statPrinteles(energia,penz)
                    ido2()
                    print(f"\nHelyszin: Yolo Pub")   
                    print("Sajnos elittad minden penzedet, reszeg vagy, azt sem tudod mennyi az ido.")
                    time.sleep(5)
                    vesztettel()          
                case "2":
                    v = 0
                    os.system("cls" if os.name =="nt" else "clear")
                    statPrinteles(energia,penz)
                    ido(perc)       
                    print(f"\nMa nem iszol, nem dol ossze a vilag. Majd talan legkozelebb.")
                    time.sleep(5)
                    barossut(v)
        case "3":
            os.system("cls" if os.name =="nt" else "clear")
            perc = 1380
            statPrinteles(energia,penz)
            ido(perc)
            print(f"\nHelyszin: Adventi vasar")
            print(f"Elvesztel az adventi vasarban, elfeledkeztel mennyi az ido!")
            time.sleep(5)
            vesztettel()    
        case "4":
            elfognak = random.randint(0,100)
            if elfognak <= 45:
                        os.system("cls" if os.name =="nt" else "clear")
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
                os.system("cls" if os.name =="nt" else "clear")
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
    os.system("cls" if os.name =="nt" else "clear")
    if penz >= 15000 and nyelvtanulas == True:
        penz -= 15000
        statPrinteles(energia,penz)
        ido(perc)
        print(f"\nHelyszin: Vasutallomas, Belfoldi Jegypenztar")
        print(f"\nGratulalok! Elerted az almodat, sok sikert kivanunk!")
        time.sleep(3)
        vege()
    elif nyelvtanulas != True and penz <15000:
        v = 0
        statPrinteles(energia,penz)
        ido(perc)
        print("\nSe nemetul nem tudsz, se penzed sincs. Megis mit szeretnel?")
        time.sleep(2)
        gyor(v)
    elif nyelvtanulas != True:
                v = 0
                statPrinteles(energia,penz)
                ido(perc)
                print("\nNem tudsz nemetul!\nHa iskolaba jarsz, ott megtanulsz!")
                time.sleep(2)
                gyor(v)
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
    os.system("cls" if os.name =="nt" else "clear")
    if perc < 480:
        perc = random.randint(480,485)
    if perc > 480 and perc < 525:
        statPrinteles(energia, penz)
        ido(perc)
        print("\nHelyszin: Iskola(Lyedlick)")
        print(f"Becsengettek, bemesz az elso oradra, igaz kestel egy kicsit.")
        time.sleep(3.5)
        os.system("cls" if os.name =="nt" else "clear")
        statPrinteles(energia, penz)
        ido(perc)
        print("\nHelyszin: Iskola(Lyedlick)")
        print(f"\nAz elso orad matek. Kastal Erika tanarno beirt egy egyest, mert nem volt meg a hazid.\nEzert otthon biztosan kapsz!")
        szunet(random.randint(525,535))
        energia -= 15
        perc = random.randint(535,580)
        os.system("cls" if os.name =="nt" else "clear")
        statPrinteles(energia,penz)
        ido(perc)
        print("\nHelyszin: Iskola(Lyedlick)")
        print(f"\nA masodik orad nemet. Betegseg miatt Csicsay Imre tanar ur helyettesit, mert kivaloan tud nemetul.\nKaptal egy otost, mert nagyon jol dolgoztal az oran!")
        nyelvtanulas = True
        szunet(random.randint(580,590))
        energia = 100
        perc = random.randint(590,635)
        os.system("cls" if os.name =="nt" else "clear")
        statPrinteles(energia, penz)
        ido(perc)
        print("\nHelyszin: Iskola(Lyedlick)")
        print(f"\nA harmadik orad tortenelem. Nem figyeltel semmit ,mert vegig telefonoztal.\nKozben a padod 1.5 metert arreb mozdult amit sem te, sem Somjai Laszlo tanar ur nem vett eszre.")
        szunet(random.randint(635,650))
        energia -=5
        perc = random.randint(650,695)
        os.system("cls" if os.name =="nt" else "clear")
        statPrinteles(energia, penz)
        ido(perc)
        print("\nHelyszin: Iskola(Lyedlick)")
        print(f"\nA negyedik orad jon, a fizika. \nAgoston Anett tanarno az alkohol egesevel szeretne kiserletezni, de rajott, hogy otthon hagyta az etil-alkoholt.")
        time.sleep(5)
        os.system("cls" if os.name =="nt" else "clear")
        statPrinteles(energia,penz)
        ido(perc)
        print("\nA haverokkal terveztek este bulizni, igy van nalad 3dl a nagypapa keritesszagatojabol.")
        v = input("\n1 - Felajanlom kiserleti celokra a nedut. \t\t 2 - Inkabb csendben maradok. \t\t 3 - Kimegyek mosdoba.\nMit teszel?")
        match v:
            case "1":
                    leszid = random.randint(0,100)
                    os.system("cls" if os.name =="nt" else "clear")
                    statPrinteles(energia,penz)
                    ido(perc)
                    print("\nHelyszin: Iskola(Lyedlick)")
                    if leszid <= 30:
                        print("\nA tanarno nagyon nem orult neki, elkuldott az igazgatoi irodaba, mert alkoholt hoztal be az iskolaba!\nEdesanyad a nyakadat kitekeri, foleg a matek egyes utan!")
                        time.sleep(7)
                        energia = 0
                        vesztettel()
                    else:
                        print("\nA tanarnonek nagyon bejott az otlet, szoval a palinkabol egy kicsit meggyujtottal az asztalon!")
                        time.sleep(3)
                        pass
            case "2":
                    os.system("cls" if os.name =="nt" else "clear")
                    statPrinteles(energia,penz)
                    ido(perc)
                    print("\nHelyszin: Iskola(Lyedlick)")  
                    print("\nTalalekony voltal es meglattad a kezfertotlenitot az ablakban. A kiserlet folytatodott tovabb, bar nem volt akkora durranas, mint az etil-alkohol.")          
                    time.sleep(7)
                    pass
            case "3":
                    os.system("cls" if os.name =="nt" else "clear")
                    statPrinteles(energia,penz)
                    ido(perc)
                    print("\nHelyszin: Iskola(Lyedlick)")
                    print("\nA tanarno nem orul neki, de ismer teged, igy kienged.\nEzzel viszont elvontad a figyelmet a kiserletrol, teljesen elfelejtette. Az ora folytatodik a szokott rendjen.")
                    pass
            case default:
                    os.system("cls" if os.name =="nt" else "clear")
                    statPrinteles(energia,penz)
                    ido(perc)
                    print("\nHelyszin: Iskola(Lyedlick)")
                    print("Valami baj van...Mi FOLYIK itt?")
                    time.sleep(2)
                    os.system("cls" if os.name =="nt" else "clear")
                    statPrinteles(energia,penz)
                    ido(perc)
                    print("\nHelyszin: Iskola(Lyedlick)")
                    print("JAJ NE! Bevizeltel! Leegetted magad az egesz osztaly elott!(secret ending)")
                    time.sleep(7)
                    vege()
        szunet(random.randint(695,705))
        energia -= 10
        perc = random.randint(705,750)
        os.system("cls" if os.name =="nt" else "clear")
        statPrinteles(energia,penz)
        ido(perc)
        print("\nHelyszin: Iskola(Lyedlick)")
        print("\n5-6. orad programozas Csicsay tanar urral.\nGyakorlo feladatokat csinaltatok, mert most tanultatok a szotarakat.")
        time.sleep(7)
        perc = 745
        os.system("cls" if os.name =="nt" else "clear")
        statPrinteles(energia,penz)
        ido(perc)
        print("\nHelyszin: Iskola(Lyedlick)")
        time.sleep(1)
        print("\nMegszolalt a jelzocsengo.\nCSI: SZUNET!")
        time.sleep(1)
        print("\nA Tanar ur elengedett 5 perccel elobb szunetre.")
        time.sleep(5)
        szunet(random.randint(740,760))
        energia += 5
        perc = random.randint(760,805)
        os.system("cls" if os.name =="nt" else "clear")
        statPrinteles(energia,penz)
        ido(perc)
        print("\nHelyszin: Iskola(Lyedlick)")
        print("\nJon a masodik programozas. Elkezdted magadtol megoldani a feladatokat.")
        time.sleep(5)
        print("\nHat... valamit nagyon elrontottal, mert a szamitogep langra kapott.\nIlyen rossz kodot irtal volna? Shit happens")
        time.sleep(7)
        perc = 800
        os.system("cls" if os.name =="nt" else "clear")
        statPrinteles(energia,penz)
        ido(perc)
        print("\nHelyszin: Iskola(Lyedlick)")
        time.sleep(1)
        print("\nIsmet jelzocsengo.\nCSI: Menjunk haza!")
        time.sleep(4)
        print("\nA Tanar ur elengedett 5 perccel elobb szunetre.")
        time.sleep(5)
        szunet(random.randint(800,815))
        os.system("cls" if os.name =="nt" else "clear")
        energia = 100
        perc = random.randint(815,860)
        statPrinteles(energia,penz)
        ido(perc)
        print("\nHelyszin: Iskola(Lyedlick)")
        print("\nSajnos te meg nem mehettel haza. Utolso orad irodalom Reger Daniel tanar urral")
        time.sleep(7)
        os.system("cls" if os.name =="nt" else "clear")
        statPrinteles(energia,penz)
        ido(perc)
        print("\nHelyszin: Iskola(Lyedlick)")
        print("\nFeleles kovetkezik.")
        v = input("\n 1 - Igen\t\t 2 - Nem\nTanultal?")
        match v:
            case "1":
                    os.system("cls" if os.name =="nt" else "clear")
                    statPrinteles(energia,penz)
                    ido(perc)
                    print("\nHelyszin: Iskola(Lyedlick)")
                    print("\nA tanar ur teged szolitott fel, es mivel tanultal kaptal egy otost!\nLehet anyukad megsem lesz merges.")
                    time.sleep(7)
                    pass
            case "2":
                    os.system("cls" if os.name =="nt" else "clear")
                    statPrinteles(energia,penz)
                    ido(perc)
                    print("\nHelyszin: Iskola(Lyedlick)")
                    print("\nHat.. porul jartal, Te felelsz. A rossz jegyeid es nem tanulasod eredmenye egy egyes. A mai nap a masodik.\nSzerintem itt az ideje megszokni Becsbe!")
                    time.sleep(7)
                    pass
        perc = 860
        energia -= 10
        os.system("cls" if os.name =="nt" else "clear")
        statPrinteles(energia,penz)
        ido(perc)
        print("\nHelyszin: Iskola(Lyedlick)")
        print("\nMegszabadultal az iskolabol!")
        v = "0"
        gyor(0)



def szunet(perc : int):
        time.sleep(5)
        os.system("cls" if os.name =="nt" else "clear")
        statPrinteles(energia, penz)
        ido(perc)
        print("SZUNET")
        time.sleep(3.5)


def vege():
    os.system("cls" if os.name =="nt" else "clear")
    print("Kettest megeri?")
    time.sleep(5)

