class Mobitel:
    def ispis(self):
        print("GSM mreža")


class Samsung(Mobitel):
    def ispis(self):
        print("Samsung Smartphone")


def main():
    objekt1 = Samsung()
    objekt1.ispis()


if __name__ == '__main__':
    main()


