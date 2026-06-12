class father:
    def property(self):
        print("father have property")

    def business(self):
        print("father have business")

class son(father):
    def study(self):
        print("love study")

class doughter(father):
    def dance(self):
        print("love dancing")

class grand_son(son, doughter):
    def gamming(self):
        print("love gamming")

g = grand_son()
g.business()
g.dance()
g.property()
g.study()
g.gamming()

    