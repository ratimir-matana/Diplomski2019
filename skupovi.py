# deklaracija seta nogometasi uz funkciju set() koja prima listu elemenata
nogometasi = set(['Mirko', 'Pero', 'Ivan', 'Marko'])

# ispis sadržaja skupa nogometasi
print("\n Nogometasi: ", nogometasi)

# dodavanje jedne vrijednosti u set
nogometasi.add('Romario')

# provjera trenutnog sadržaja skupa
print("\nNogometasi nakon dodavanja: ", nogometasi)

# deklaracija skupa rukometasi
rukometasi = {'Horvat', 'Gojun', 'Duvnjak'}

# ispis trenutnog sadržaja skupa
print("\n Rukometasi: ", rukometasi)

# dodavanje više(strukih) vrijednosti u skup
nogometasi.update(['Bergkamp', 'Overmars', 'Cocu'])

# provjera trenutnog sadržaja skupa
print("\n Nogometaši nakon višestrukog dodavanja: ", nogometasi)

# dodavanje vrijednosti iz seta rukometasi
nogometasi.update(rukometasi)

# provjera trenutnog sadržaja skupa
print("\n Nogometaši nakon dodavanja rukometasa: ", nogometasi)

# micanje vrijednosti Pero iz seta
nogometasi.discard('Pero')

# provjera trenutnog sadržaja skupa
print("\n Nogometaši nakon izbacivanja Pere: ", nogometasi)

# sve vrijednosti koje se nalaze u setu rukometasi i u setu nogometasi
s3 = nogometasi.intersection(rukometasi)

# ispis intersekcije
print("\n Rezultat intersekcije nogometaša i rukometaša: ", s3)

# vrijednosti koje su u setu nogometasi, a koje nisu u setu rukometasi
s4 = nogometasi.difference(rukometasi)

# ispis razlike
print("\n Rezultat razlike nogometaša i rukometaša: ", s4)

# sve elemente koji nisu prisutni u setu nogometasi i rukometasi
s5 = nogometasi.symmetric_difference(rukometasi)

# ispis simetrične razlike
print("\n Rezultat simetrične razlike nogometaša i rukometaša: ", s5)
