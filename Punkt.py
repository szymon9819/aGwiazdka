class Punkt:
    wsp_x = None
    wsp_y = None
    wart = None
    koszt = None

    rodzic_x = None
    rodzic_y = None

    def __init__(self, x, y):
        self.wsp_x = x
        self.wsp_y = y

    def __str__(self):
        return ('(' + str(self.wsp_x) + ',' + str(self.wsp_y) + ')'+'\n')
