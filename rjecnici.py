# kreiranje rječnika
automobili = {
  "brand": "Dacia",
  "model": "Sandero",
  "godina": 2015
}
print(automobili)
# kreiranje rječnika pomoću konstruktora dict()
automobili2 = dict(brand="Hyundai", model="i10", godina="2016")
print("\n", automobili2)

# dodavanje elementa u rječnik
automobili2["motor"] = "diesel"
print("\n Rječnik nakon dodavanja elementa: ", automobili2)

# broj elemenata (parova ključ - vrijednost) za rječnik automobili2
print("\n Broj elemenata rječnika automobili2:", len(automobili2))

# pristup elementu rječnika automobili
print("\n", automobili['brand'])

# provjera da li je ključ prisutan u rječniku
if 'motor' in automobili2:
    print("\n Rječnik automobili2 sadrži vrijednost: ", automobili2['motor'])
else:
    print("\n Rječnik automobili2 nema odgovarajući element")

# provjera da li je ključ prisutan pomoću iznimka
try:
    print("\n Rječnik automobili2 sadrži vrijednost: ", automobili2['mijenjač'])
except KeyError:
    print("\n Rječnik automobili2 nema element mijenjač.")

# provjera da li je ključ prisutan u rječniku pomoću metode get()
provjera = automobili2.get('težina', None)
if provjera is None:
    print("\n Nema elementa težina")

# provjera da li je ključ prisutan u rječniku pomoću metode get()
print("\n", automobili2.get('težina', 'Nije pronađeno'))

# iteracija nad svim parovima ključ - vrijednost rječnika pomoću keys() metode
print()
for key in automobili2.keys():
    value = automobili2[key]
    print(key, ":", value)

# iteracija nad svim parovima ključ - vrijednost rječnika pomoću items() metode
print()
for key, value in automobili.items():
    print(key, ":", value)

# uklanjanje pojedinog elementa
print("\n", automobili2.pop('motor'))

print("\n Broj elemenata rječnika automobili2 nakon uklanjanja:", len(automobili2))

# unos novog elementa u rječnik
automobili2.update({"težina": "950"})

print("\n Ispis nakon unosa elementa: ", automobili2)

# uklanjanje pojedinog elementa rječnika
del automobili2['težina']
print("\n Ispis nakon naredbe del: ", automobili2)


