import random, os
from helyek import gyomore

def ido(ora: int, perc: int):
    ido = f"{ora}:{perc}"
    if perc > 60:
        ora += 1
        perc = perc % 60
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
    global ora
    global perc
    print(f"Energia:{energia}\t\tPenz: {penz}Ft", end="\t\t")

def main():
    global energia
    global penz
    energia = 100
    penz = 2500
    ora = 9
    perc = 0
    os.system('cls')
    print("Gyor simulator 2")
    print("\n1 - Start \t 2 - Kilepes")
    v = input("")
    match v:
        case '1':
            os.system('cls')
            print("Udv a Gyor Simulator 2-ben, ahol ugyanaz a celod, mint az elso kiadasban, hogy megvedd a csodas vonatjegyed Becsbe. Sok szerencset!")
            input("\nENTER")
            os.system('cls')
            statPrinteles(energia, penz)
            ido(ora, perc)
            v = 0
            gyomore(v)
        case '2':
            pass
        case default:
            main()

main()


