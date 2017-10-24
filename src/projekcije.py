film = dict(kljuc = "vrednost", kljuc2 = "vrednost2")

print(film)

for kljuc in film:
    #print(kljuc)
    #print(film.keys())
    #print(film[kljuc])
    if kljuc in film.keys():
        print(film[kljuc])
    else:
        print("whatever")
