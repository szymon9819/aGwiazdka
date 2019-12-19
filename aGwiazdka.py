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
    # dol
    if pkt.wsp_x + 1 < 20 and mapaPkt[pkt.wsp_x + 1][pkt.wsp_y].wart != '5' and czyNaLiscie(
            mapaPkt[pkt.wsp_x + 1][pkt.wsp_y]) is False and mapaPkt[pkt.wsp_x + 1][pkt.wsp_y].rodzic_x is None:
        potomek = mapaPkt[pkt.wsp_x + 1][pkt.wsp_y]
        potomek.rodzic_x = pkt.wsp_x
        potomek.rodzic_y = pkt.wsp_y
        mapaPkt[pkt.wsp_x + 1][pkt.wsp_y] = potomek
        obliczKoszt(potomek)
        listaOtwarta.append(potomek)
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
        potomek = Punkt


def obliczKoszt(pkt):
    heur = heurystyka(pkt.wsp_x, pkt.wsp_y)
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
    for i in range(listaOtwarta.__len__() - 1, -1, -1):
        if listaOtwarta[i].wsp_x == punktNaj.wsp_x and listaOtwarta[i].wsp_y == punktNaj.wsp_y:
            del listaOtwarta[i]
    listaZamknieta.append(punktNaj)


def mapaKoncowa():
    pkt = mapaPkt[punktKoncowy.wsp_x][punktKoncowy.wsp_y]
    wart = True
    while wart:
        mapa[pkt.wsp_x][pkt.wsp_y] = '3'
        pkt = mapaPkt[pkt.rodzic_x][pkt.rodzic_y]
        if punktStartowy.wsp_x == pkt.wsp_x and punktStartowy.wsp_y == pkt.wsp_y:
            wart = False


def wyswietlMape():
    for i in mapa:
        print(i)


def gwiazdka():
    wczytajMape('grid.txt')
    wczytajMapePkt()
    # wyswietlMape()
    listaZamknieta.append(punktStartowy)
    dodajOtwarta(listaZamknieta[0])

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
        pom += 1
        if czyNaLiscie(punktKoncowy):
            break
    mapaKoncowa()
    wyswietlMape()


gwiazdka()
