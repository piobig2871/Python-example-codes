class DzialaniaArytmetyczne:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def _znak(self):
        return 'NaN'

    def __str__(self):
        return "({} {} {})".format(self.a, self._znak, self.b)



    def to_dict(self):
        a = self.a
        if isinstance(a, DzialaniaArytmetyczne):
            a = a.to_dict()
        b = self.b
        if isinstance(b, DzialaniaArytmetyczne):
            b = b.to_dict()
        return {self._znak: [a, b]}


class Dodaj(DzialaniaArytmetyczne):

    def wykonaj(self):
        a = self.a
        if isinstance(a, DzialaniaArytmetyczne):
            a = a.wykonaj()
        b = self.b
        if isinstance(b, DzialaniaArytmetyczne):
            b = b.wykonaj()
        return a + b

    @property
    def _znak(self):
        return '+'


class Mnozenie(DzialaniaArytmetyczne):

    def wykonaj(self):
        a = self.a
        if isinstance(a, DzialaniaArytmetyczne):
            a = a.wykonaj()
        b = self.b
        if isinstance(b, DzialaniaArytmetyczne):
            b = b.wykonaj()
        return a * b

    @property
    def _znak(self):
        return '*'

class Dzielenie(DzialaniaArytmetyczne):

    def wykonaj(self):
        a = self.a
        if isinstance(a, DzialaniaArytmetyczne):
            a = a.wykonaj()
        b = self.b
        if isinstance(b, DzialaniaArytmetyczne):
            b = b.wykonaj()
        return a / b

    @property
    def _znak(self):
        return '/'

class Odejmowanie(DzialaniaArytmetyczne):

    def wykonaj(self):
        a = self.a
        if isinstance(a, DzialaniaArytmetyczne):
            a = a.wykonaj()
        b = self.b
        if isinstance(b, DzialaniaArytmetyczne):
            b = b.wykonaj()
        return a - b

    @property
    def _znak(self):
        return '-'

a = Dodaj(3,5)
print a.wykonaj()
b = Dodaj(Mnozenie(3, 3333), Dodaj(3, 4))
print 'b', b
b = Dodaj(4, Mnozenie(3, 553333))
print 'b', b
c = Odejmowanie(333, Odejmowanie(4,5))
print c.wykonaj()
d = Mnozenie(3,5)
print d.wykonaj()
print a.__str__()
print b.__str__()
print c.__str__()
print a.to_dict()
