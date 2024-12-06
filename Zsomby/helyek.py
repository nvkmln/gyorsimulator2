import random, os

def gyomore(v: str):
    print("\nAhhoz, hogy eljuss Becsbe, eloszor el kell menj otthonrol Gyorbe, ezert Gyomoren kezdesz.")
    print(f"\nKésik a vonatod {random.randint(1, 120)} percet. Megvárod?")
    print("1 - Igen \t 2 - Nem")
    v = input("")
    match v:
        case '1':
            gyor()
        case '2':
            Vesztettel()
        case default:
            gyomore(v)

def gyor():
    os.system('cls')
    print("\nHelyszin: Gyor, Vasutallomas\n1 - Iskola(Lyedlick)\n2 - Dohanybolt\n3 - Arkad\n4 - Baross ut\n6 - Becsi vonat")
    
