StarWars = {"id": 0,
            "ime": "Star Wars",
            "zanr": "sci-fi"
            }

HarryPotter = {"id": 1,
            "ime": "Harry Potter",
            "zanr": "fantasy"
            }

HarryPotterProjekcija = {"id": 0,
                         "datum": "30.10.2017",
                         "vreme": "21:00",
                         "duzina": 120,
                         "film": HarryPotter,
                         "sala": "A1",
                         "obrisana": False,
                         "brojSlobodnihMesta": 200,
                         "brojUkupnihMesta": 250
                         }

projekcije = [HarryPotterProjekcija]
filmovi = [StarWars, HarryPotter]

def unosProjekcije():
    print("Unos nove projekcije: ")
    datum = input("Unesite datum projkecije u formatu dd.mm.yyyy: ")
    vreme = input("Unesite vreme projkecije u formatu hh.mm: ")
    duzina = input("Unesite duzinu trajanja projkecije u minutima: ")
    film = input("Unesite ime filma: ").title()
    filmVarName = film.title().replace(" ", "").replace("'", "")
    zanr = input("Unesite zanr filma: ")
    sala = input("Unesite salu projekcije: ")
    brojSlobodnihMesta = input("Unesite broj slobodnih mesta: ")
    brojUkupnihMesta = input("Unesite broj ukupnih mesta: ")
    globals()[filmVarName] = {"id": len(filmovi), "ime": film, "zanr": zanr}
    filmovi.append(globals()[filmVarName])
    globals()[filmVarName + "Projekcija"] = {"id": len(projekcije), "datum": datum, "vreme": vreme, "duzina": duzina, "film": filmVarName, "obrisana": False, "brojSlobodnihMesta": brojSlobodnihMesta, "brojUkupnihMesta": brojUkupnihMesta} 
    projekcije.append(globals()[filmVarName + "Projekcija"])
    



    


    
