import math
from Punkt import Punkt

punktKoncowy = Punkt(11, 0)
tmp=Punkt(11,0)
punktStartowy = Punkt(1, 0)
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
    if pkt.wsp_x + 1 < 20 and mapaPkt[pkt.wsp_x + 1][pkt.wsp_y].wart != 5 and czyNaLiscie(
            mapaPkt[pkt.wsp_x + 1][pkt.wsp_y]) is False:
        if potomek.rodzic_x is None:
            potomek.rodzic_x = pkt.wsp_x
            potomek.rodzic_y = pkt.wsp_y
            potomek.wsp_x = pkt.wsp_x + 1
            potomek.wsp_y = pkt.wsp_y
            potomek.koszt = obliczKoszt(potomek)
            listaOtwarta.append(potomek)
            print("rodzic "+ str(pkt.wsp_x) +"," +str(pkt.wsp_y) +"\tdol potomek " + str(potomek.rodzic_x) +","+ str(potomek.rodzic_y) +"\tkosz: "+ str(potomek.koszt))

    # lewa
    if pkt.wsp_y - 1 >= 0 and mapa[pkt.wsp_x][pkt.wsp_y - 1] != 5 and czyNaLiscie(
            mapaPkt[pkt.wsp_x][pkt.wsp_y - 1]) is False:
        if potomek.rodzic_x is None:
            potomek.rodzic_x = pkt.wsp_x
            potomek.rodzic_y = pkt.wsp_y
            potomek.wsp_x = pkt.wsp_x
            potomek.wsp_y = pkt.wsp_y - 1
            potomek.koszt = obliczKoszt(potomek)
            listaOtwarta.append(potomek)
            print("rodzic "+ str(pkt.wsp_x) +"," +str(pkt.wsp_y) +"\tlewa potomek " + str(potomek.rodzic_x)+"," + str(potomek.rodzic_y) +"\tkosz: "+ str(potomek.koszt))

    # gora
    if pkt.wsp_x - 1 >= 0 and mapaPkt[pkt.wsp_x - 1][pkt.wsp_y].wart != 5 and czyNaLiscie(
            mapaPkt[pkt.wsp_x - 1][pkt.wsp_y]) is False:
        if potomek.rodzic_x is None:
            potomek.rodzic_x = pkt.wsp_x
            potomek.rodzic_y = pkt.wsp_y
            potomek.wsp_x = pkt.wsp_x - 1
            potomek.wsp_y = pkt.wsp_y
            potomek.koszt = obliczKoszt(potomek)
            listaOtwarta.append(potomek)
            print("rodzic "+ str(pkt.wsp_x) +"," +str(pkt.wsp_y) +"\tgora potomek " + str(potomek.rodzic_x) +","+ str(potomek.rodzic_y) +"\tkoszt: "+ str(potomek.koszt))

    # prawa
    if pkt.wsp_y + 1 < 20 and mapa[pkt.wsp_x][pkt.wsp_y + 1] != 5 and czyNaLiscie(
            mapaPkt[pkt.wsp_x][pkt.wsp_y + 1]) is False:
        if potomek.rodzic_x is None:
            potomek.rodzic_x = pkt.wsp_x
            potomek.rodzic_y = pkt.wsp_y
            potomek.wsp_x = pkt.wsp_x
            potomek.wsp_y = pkt.wsp_y + 1
            potomek.koszt = obliczKoszt(potomek)
            listaOtwarta.append(potomek)
            print("rodzic "+ str(pkt.wsp_x) +"," +str(pkt.wsp_y) +"\tprawa potomek " + str(potomek.wsp_x)+"," + str(potomek.wsp_y) +"\tkoszt: "+ str(potomek.koszt))


def obliczKoszt(pkt):
    heur = heurystyka(pkt.wsp_x, pkt.wsp_y)

    koszt = 0
    wart = True
    while wart:
        if punktStartowy.wsp_x == pkt.wsp_x and punktStartowy.wsp_y == pkt.wsp_y:
            wart = False
            return koszt + heur
        else:
            pkt = mapaPkt[pkt.rodzic_x][pkt.rodzic_y]
            koszt += 1
    return koszt + heur


def czyNaLiscie(pkt):
    for i in range(listaZamknieta.__len__() - 1):
        if listaZamknieta[i].wsp_x == pkt.wsp_x and listaZamknieta[i].wsp_y == pkt.wsp_y:
            return True
    return False


def najmniejszyKoszt():
    # znalezienie punktu z najmniejszym kosztem
    punktNaj = listaOtwarta[listaOtwarta.__len__() - 1]
    for i in range(listaOtwarta.__len__() - 1, -1, -1):
        if listaOtwarta[i].koszt < punktNaj.koszt:
            punktNaj = listaOtwarta[i]
    return punktNaj


def doZamknietej():
    punktNaj: Punkt = najmniejszyKoszt()
    print("wynik funkcji doZamknie")
    wyswietl(listaOtwarta)
    for i in range(listaOtwarta.__len__() - 1):
        if listaOtwarta[i].wsp_x == punktNaj.wsp_x and listaOtwarta[i].wsp_y == punktNaj.wsp_y:
            del listaOtwarta[i]
    #wyswietl(listaOtwarta)
    print("koniec funkcji doZamknie")
    listaZamknieta.append(punktNaj)


def mapaKoncowa(pkt):

    while True:
        mapa[pkt.wsp_x][pkt.wsp_y] = 3
        pkt = mapaPkt[pkt.rodzic_x][pkt.rodzic_y]
        if punktStartowy.wsp_x == pkt.wsp_x and punktStartowy.wsp_y == pkt.wsp_y:
            break


def wyswietlMape():
    for i in mapa:
        print(i)
def wyswietl(lista):
    for i in lista:
        print("element listy zamknietej " + str(lista.wsp_x) + "," + str(lista.wsp_y))


def gwiazdka():
    wczytajMape('grid.txt')
    wczytajMapePkt()
    # wyswietlMape()
    listaZamknieta.append(punktStartowy)
    dodajOtwarta(listaZamknieta[0])
    mapa[punktStartowy.wsp_x][punktStartowy.wsp_y] = 3
    # indeks do iteracji po zamknietej liscie
    pom = 1

    while True:
        if listaOtwarta.__len__() == 0:
            print("nie mozna dotrzec do celu")

        doZamknietej()
        print("element listy zamknietej " + str(listaZamknieta[pom].wsp_x) + "," + str(listaZamknieta[pom].wsp_y))
        dodajOtwarta(listaZamknieta[pom])
        print("element listy otwartej " + str(listaOtwarta[pom-1].wsp_x)+","+str(listaOtwarta[pom-1].wsp_y))
        pom += 1
        if not czyNaLiscie(punktKoncowy):
            break
    mapaKoncowa(punktKoncowy)
  #  wyswietlMape()


gwiazdka()
