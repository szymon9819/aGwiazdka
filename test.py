import math

from Punkt import Punkt

punktKoncowy = Punkt(2, 2)
punktStartowy = Punkt(0, 0)


def podajWsp():
    try:
        print("Podaj wspolrzedne punktu startowego z przedzialu 0-19")
        x = int(input())
        y = int(input())
        if (0 <= x < 20) and (0 <= y < 20):
            punktStartowy.wsp_x = x
            punktStartowy.wsp_y = y
            print("Podaj wspolrzedne punktu koncowego z przedzialu 0-19")
            x = int(input())
            y = int(input())
            if (0 <= x < 20) and (0 <= y < 20):
                punktKoncowy.wsp_x = x
                punktKoncowy.wsp_y = y
            else:
                print("Nie podano wartosci z podanego przedziału...")
                podajWsp()

        else:
            print("Nie podano wartosci z podanego przedziału...")
            podajWsp()
    except ValueError as e:
        print("Nie zostały podane liczby")
        print(e)


def obliczKoszt(pkt: Punkt):
    koszt = 0
    wart = True
    while wart:
        if punktStartowy.wsp_x == pkt.wsp_x and punktStartowy.wsp_y == pkt.wsp_y:
            wart = False
            return koszt
        else:
            print(pkt)
            print('1 \n')
            pkt = mapaPkt[pkt.rodzic_x][pkt.rodzic_y]
            print(pkt)
            koszt += 1
    print("koszt pkt", str(pkt.wsp_x) + str(pkt.wsp_y) + " " + koszt + heur)
    return koszt


test1 = Punkt(2, 0)
test1.rodzic_x = 1
test1.rodzic_y = 0

test2 = Punkt(3, 0)
test2.rodzic_x = test1.wsp_x
test2.rodzic_y = 0

test3 = Punkt(4, 0)
test3.rodzic_x = test2.wsp_x
test3.rodzic_y = 0

test4 = Punkt(5, 0)
test4.rodzic_x = test3.wsp_x
test4.rodzic_y = 0
test4 = test2
tab = []
tab.append(test1)
tab.append(test2)
tab.append(test3)
tab.append(test4)
for o in tab:
    print(o)
