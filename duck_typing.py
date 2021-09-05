class Kolokvij:
    def pokreni(self):
        print("Prvi kolokvij")
        print("Drugi kolokvij")


class Seminar:
    def pokreni(self):
        print("Python")
        print("Java")
        print("MatLab")
        print("Javascript")


class Ispit:
    def pisanje(self, potpis):
        potpis.pokreni()


def main():
    potpis = Kolokvij()
    isp1 = Ispit()
    isp1.pisanje(potpis)


if __name__ == '__main__':
    main()

