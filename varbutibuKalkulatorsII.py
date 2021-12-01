#Varbutibu kalkulators
# Autors: Oskar A.
# Datums: 03.11.2021 V2V
from datetime import date
import math

today = date.today()
print("Šodienas datums:","[",today,"]")
print ("Autors: Oskar A.")
txt = ('\033[94m{}\033[0m'.format("[Varbutibu kalkulators]"))
INF = txt.center(65)
print(INF)

def statistiska():

    valueM = int(input("notikumu skaits:"))

    if valueM > 0:
        print()
    else:
        print("\033[91mJusu pirmais skailtlis nevar but negativs, meginiet velreiz")
        exit(0)

    valueK = int(input("eksperimentu skaits:"))

    p = valueM/valueK;

    if valueK > 0:
        print()
    else:
        print("\033[91mJusu otrais skailtlis nevar but negativs, meginiet velreiz")
        exit(0)


    print("\033[94m{}\033[0m".format("--------------------------------"))
    value_1 = p*100
    print("Tas bus " + format(value_1,",.2f")+"%"+" statistiskā varbūtība")
    print("\033[94m{}\033[0m".format("--------------------------------"))


def geometriksa():

    value_radiuss = int(input("Kada radius un tilpumi:"))

    if value_radiuss > 0:
        print()
    else:
        print("\033[91mJusu pirmais skailtlis nevar but negativs, meginiet velreiz")
        exit(0)

    value_malas = int(input("kada malas garumu:"))

    if value_malas > 0:
        print()
    else:
        print("\033[91mJusu otrais skailtlis nevar but negativs, meginiet velreiz")
        exit(0)

    Pi = math.pi

    square = (math.pow(value_malas, 2)) / ((math.pow(value_radiuss, 2))) * Pi

    value_1 = square * 100
    print("\033[94m{}\033[0m".format("--------------------------------"))
    print("varbūtība ir " + format( value_1, ",.2f")+"%")
    if value_1>100:
        print("Varbūtība nekad nevar pārsniegt skaitli 1 (jeb 100%)")
    print("\033[94m{}\033[0m".format("--------------------------------"))


def klasiska():

    labveligo = float (input("labvēlīgo notikumu skaits:"))

    if labveligo > 0:
        print()
    else:
        print("\033[91mJusu pirmais skailtlis nevar but negativs, meginiet velreiz")
        exit(0)


    kopskaits = float (input("visu notikumu kopskaits:"))

    if kopskaits > 0:
        print()
    else:
        print("\033[91mJusu otrais skailtlis nevar but negativs, meginiet velreiz")
        exit(0)

    klasiska = labveligo/kopskaits

    print("\033[94m{}\033[0m".format("--------------------------------"))
    print("varbūtība ir =" + format( klasiska, ",.2f")+"%")
    print("\033[94m{}\033[0m".format("--------------------------------"))



def calc(first, second):
    A = first/second
    varbutiba = A*100
    print("\033[94m{}\033[0m".format("--------------------------------"))
    print("\033[1;97mvarbūtība ir = " + format(varbutiba, ",.2f") + '%')
    print("\033[94m{}\033[0m".format("--------------------------------"))
    return A


def lottery():
    print("\033[91mPirmais spēlētājs")
    print("\033[93m")
    first = int(input("Enter first number:"))
    second = int(input("Enter second number:"))
    print("\033[93m")
    print("\033[91mOtrais spēlētājs")
    print("\033[93m")
    first1 = int(input("Enter again first number:"))
    second2 = int(input("Enter again second number:"))

    pirma = calc(first, second)
    otra = calc(first1, second2)

    if pirma > otra:
        print("Pirma kom. ir Visveiksmigaks " + " [ " + str(first) + " ] " + "  " + " [ " + str(second) + " ] " )
    else:
        print("Otra kom. ir Visveiksmigaks: " + " [ " + str(first1) + " ] " + "  " + " [ " + str(second2) + " ] " )






if __name__ == '__main__':
        choice = input("Kada veida varbutibas aprekini Tev sodien padoma? \n"
                   "Ievadi burtu:\n"
                    "-K klasiska metode n no n\n"
                   "-G geometriksa varbutiba\n"
                   "-S statiska varbutiba k m reizes\n"
                   "\033[92m-L Loterejas kalkulatos\n")
        if choice.lower() == 'k':
            klasiska()
        if choice.lower() == 'g':
            geometriksa()
        if choice.lower() == 's':
            statistiska()
        if choice.lower() == 'L':
            calc()
        while True:
            lottery()
            restart = input("do you want again?").lower()
            if restart == "y":
                lottery()
            else:
                exit(0)
        else:
            exit(0)