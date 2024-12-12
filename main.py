from helyek import gyomore
import os

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
            print("Udv a Gyor Simulator 2-ben, ahol ugyanaz a celod, mint az elso kiadasban, hogy megvedd a csodas vonatjegyed a Becsbe tarto szerelvenyre. Sok szerencset!")
            input("\nENTER")
            v = 0
            gyomore(v)
        case '2':
            os.system("cls")
            print("Ha nem akarsz jatszani minek nyitottad meg?")
            pass
        case default:
            main()

main()

