
class Degree:
    def getDegree(self):
        print("I got a degree")


class Undergraduate(Degree):
    def getDegree(self):
        print("I am an Undergraduate")


class Postgraduate(Degree):
    def getDegree(self):
        print("I am a Postgraduate")


degree = Degree()
ug = Undergraduate()
pg = Postgraduate()

degree.getDegree()

ug.getDegree()

pg.getDegree()