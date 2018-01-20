import json

def ucitavanje_podataka(fajl):
    '''
    Funkcija za ucitavanje fajla.
    '''
    data = json.load(open(fajl, "r"))
    return data