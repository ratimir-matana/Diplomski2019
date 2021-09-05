# Primjer jednostrukog nasljeđivanja

class Igrac:
    def __init__(self, ime, godine):
        self.ime = ime
        self.godine = godine

    def display(self):
        print('ime : ', self.ime)
        print('godine : ', self.godine)


class Nogometas(Igrac):
    def __init__(self, id, ime, godine, fit):
        self.id = id
        Igrac.__init__(self, ime, godine)
        self.fit = fit

    def display(self):
        print('id : ', self.id)
        Igrac.display(self)
        print('fit : ', self.fit)


def main():
    n1 = Nogometas(11, 'Rivaldo', 27, 75.50)
    print('Nogometas informacije : ')
    n1.display()


if __name__ == '__main__':
    main()
