import math
from Punkt import Punkt

punktKoncowy = Punkt(0, 19)
punktStartowy = Punkt(19, 0)
listaZamknieta = []
listaOtwarta = []
mapa = []
mapaPkt = [[Punkt(x, y) for y in range(20)] for x in range(20)]


# wczytanie mapy z pliku
def wczytajMape(nazwaPliku):
    try:
        plik = open(nazwaPliku, 'r')
        for line in plik:
            mapa.append(line.split())
        plik.close()
    except FileNotFoundError as e:
        print("Nie ma takiego pliku")
        print(e)


def wczytajMapePkt():
    for i in range(20):
        for j in range(20):
            mapaPkt[i][j].wart = mapa[i][j]


def heurystyka(x, y):
    return math.sqrt(pow(x - punktKoncowy.wsp_x, 2) + pow(y - punktKoncowy.wsp_y, 2))


def dodajOtwarta(pkt):
    potomek = Punkt
    print("\npoczatek funkcji dodajOtwarta, ilość elementow otwarta:" + str(len(listaOtwarta)))
    # dol
    if pkt.wsp_x + 1 < 20 and mapaPkt[pkt.wsp_x + 1][pkt.wsp_y].wart != '5' and czyNaLiscie(
            mapaPkt[pkt.wsp_x + 1][pkt.wsp_y]) is False and mapaPkt[pkt.wsp_x + 1][pkt.wsp_y].rodzic_x is None:
        potomek = mapaPkt[pkt.wsp_x + 1][pkt.wsp_y]
        potomek.rodzic_x = pkt.wsp_x
        potomek.rodzic_y = pkt.wsp_y
        mapaPkt[pkt.wsp_x + 1][pkt.wsp_y] = potomek
        obliczKoszt(potomek)
        listaOtwarta.append(potomek)
        print("rodzic " + str(pkt.wsp_x) + "," + str(pkt.wsp_y) + "\tdol potomek " + str(
            potomek.wsp_x) + "," + str(potomek.wsp_y) + "\tkosz: " + str(potomek.koszt))
        potomek = Punkt

    # lewa
    if pkt.wsp_y - 1 >= 0 and mapaPkt[pkt.wsp_x][pkt.wsp_y - 1].wart != '5' and czyNaLiscie(
            mapaPkt[pkt.wsp_x][pkt.wsp_y - 1]) is False and mapaPkt[pkt.wsp_x][pkt.wsp_y - 1].rodzic_x is None:
        potomek = mapaPkt[pkt.wsp_x][pkt.wsp_y - 1]
        potomek.rodzic_x = pkt.wsp_x
        potomek.rodzic_y = pkt.wsp_y
        mapaPkt[pkt.wsp_x][pkt.wsp_y - 1] = potomek
        obliczKoszt(potomek)
        listaOtwarta.append(potomek)
        print("rodzic " + str(pkt.wsp_x) + "," + str(pkt.wsp_y) + "\tlewa potomek " + str(
            potomek.wsp_x) + "," + str(potomek.wsp_y) + "\tkosz: " + str(potomek.koszt))
        potomek = Punkt

    # góra
    if pkt.wsp_x - 1 >= 0 and mapaPkt[pkt.wsp_x - 1][pkt.wsp_y].wart != '5' and czyNaLiscie(
            mapaPkt[pkt.wsp_x - 1][pkt.wsp_y]) is False and mapaPkt[pkt.wsp_x - 1][pkt.wsp_y].rodzic_x is None:
        potomek = mapaPkt[pkt.wsp_x - 1][pkt.wsp_y]
        potomek.rodzic_x = pkt.wsp_x
        potomek.rodzic_y = pkt.wsp_y
        mapaPkt[pkt.wsp_x - 1][pkt.wsp_y] = potomek
        obliczKoszt(potomek)
        listaOtwarta.append(potomek)
        print("rodzic " + str(pkt.wsp_x) + "," + str(pkt.wsp_y) + "\tgora potomek " + str(
            potomek.wsp_x) + "," + str(potomek.wsp_y) + "\tkosz: " + str(potomek.koszt))
        potomek = Punkt

    # prawa
    if pkt.wsp_y + 1 < 20 and mapaPkt[pkt.wsp_x][pkt.wsp_y + 1].wart != '5' and czyNaLiscie(
            mapaPkt[pkt.wsp_x][pkt.wsp_y + 1]) is False and mapaPkt[pkt.wsp_x][pkt.wsp_y + 1].rodzic_x is None:
        potomek = mapaPkt[pkt.wsp_x][pkt.wsp_y + 1]
        potomek.rodzic_x = pkt.wsp_x
        potomek.rodzic_y = pkt.wsp_y
        mapaPkt[pkt.wsp_x][pkt.wsp_y + 1] = potomek
        obliczKoszt(potomek)
        listaOtwarta.append(potomek)
        print("rodzic " + str(pkt.wsp_x) + "," + str(pkt.wsp_y) + "\tprawa potomek " + str(
            potomek.wsp_x) + "," + str(potomek.wsp_y) + "\tkosz: " + str(potomek.koszt))
        potomek = Punkt

    for i in listaOtwarta:
        print("Oywarta pkt: " + str(i.wsp_x) + " " + str(i.wsp_y))
    print("\nkoniec funkcji dodajOtwarta \n")


def obliczKoszt(pkt):
    heur = heurystyka(pkt.wsp_x, pkt.wsp_y)
    print("heurystyka: " + str(heur))
    koszt = 0
    pom = pkt
    wart = True
    while wart:
        pom = mapaPkt[pom.rodzic_x][pom.rodzic_y]
        koszt += 1
        if punktStartowy.wsp_x == pom.wsp_x and punktStartowy.wsp_y == pom.wsp_y:
            wart = False

    pkt.koszt = koszt + heur


def czyNaLiscie(pkt):
    for i in listaZamknieta:
        if i.wsp_x == pkt.wsp_x and i.wsp_y == pkt.wsp_y:
            return True
    return False


def najmniejszyKoszt():
    try:
        naj = listaOtwarta[len(listaOtwarta) - 1]
        for i in listaOtwarta:
            if naj.koszt > i.koszt:
                naj = i
        return naj
    except IndexError as e:
        print("poza zakresem")


def doZamknietej():
    punktNaj = najmniejszyKoszt()
    print("\nwynik funkcji doZamknie")
    for i in range(listaOtwarta.__len__() - 1, -1, -1):
        if listaOtwarta[i].wsp_x == punktNaj.wsp_x and listaOtwarta[i].wsp_y == punktNaj.wsp_y:
            del listaOtwarta[i]
    # wyswietl(listaOtwarta)
    listaZamknieta.append(punktNaj)
    for i in listaZamknieta:
        print("Zamknieta pkt: " + str(i.wsp_x) + " " + str(i.wsp_y))
    print("koniec funkcji doZamknie")


def mapaKoncowa():
    pkt = mapaPkt[punktKoncowy.wsp_x][punktKoncowy.wsp_y]
    print("mapaKoncowa")
    wart = True
    while wart:
        mapa[pkt.wsp_x][pkt.wsp_y] = '3'
        pkt = mapaPkt[pkt.rodzic_x][pkt.rodzic_y]
        if punktStartowy.wsp_x == pkt.wsp_x and punktStartowy.wsp_y == pkt.wsp_y:
            wart = False


def wyswietlMape():
    for i in mapa:
        print(i)


def wyswietlZ():
    for i in listaZamknieta:
        print("element listy zamknietej " + str(i.wsp_x) + "," + str(i.wsp_y))


def gwiazdka():
    wczytajMape('grid.txt')
    wczytajMapePkt()
    # wyswietlMape()
    listaZamknieta.append(punktStartowy)
    dodajOtwarta(listaZamknieta[0])
    print("pierwze element")
    for i in listaOtwarta:
        print("element listy otwartej " + str(i.wsp_x) + "," + str(i.wsp_y))
    wyswietlZ()
    mapa[punktStartowy.wsp_x][punktStartowy.wsp_y] = '3'
    mapa[punktKoncowy.wsp_x][punktKoncowy.wsp_y] = '3'
    # indeks do iteracji po zamknietej liscie
    pom = 1

    while True:
        if listaOtwarta.__len__() == 0:
            print("nie mozna dotrzec do celu")
        print("\n\nIteracja: " + str(pom))

        doZamknietej()

        dodajOtwarta(listaZamknieta[pom])

        for i in listaOtwarta:
            print("element listy otwartej " + str(i.wsp_x) + "," + str(i.wsp_y))

        pom += 1
        if czyNaLiscie(punktKoncowy):
            break
    mapaKoncowa()
    wyswietlMape()


gwiazdka()
