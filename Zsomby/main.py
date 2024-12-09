import random, os
from helyek import gyomore



def main():
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


main()
