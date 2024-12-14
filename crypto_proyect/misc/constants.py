

crypto_methods = [
    "Desplazamiento", 
    "Afin", 
    "RSA",
    "Multiplicativo",
    "Sustitucion",
    "Permutacion",
    "Hill",
    "Vigenere"
]

def inverse_list():
    l = list(set([x if x%2 == 1 and x!= 13 else "-1" for x in range(1,26)]))
    l.remove("-1")
    return [str(x) for x in l]

crypto_methods_info = {
    "Desplazamiento" :  
        {
            "num": 1,
            "name": ["a"],
            "type": ["int"],
            "range": [str(x) for x in range(1,26)],
            "formula": "(x + a) mod 26",
        }, 
    "Afin" : {
            "num": 2,
            "name": ["a", "b"],
            "type": ["int"],
            "range": [inverse_list(), [str(x) for x in range(1,26)]],
            "formula": "(ax + b) mod 26",
        }, 
    "RSA" : {
            "num": 3,
            "name": ["a"],
            "type": ["int"],
            #! Algunos primos tales que q != p. Se podría hacer una lista mayor.
            "range": [["2", "3", "79", "97", "101", "199", "227", "229", "349", "367"], ["11", "19", "41", "43", "113", "223", "251","311", "401", "419"]],
            "formula": "x**a mod n",

        },
    "Multiplicativo" :  
        {
            "num": 1,
            "name": ["a"],
            "type": ["int"],
            "range": [str(x) for x in range(1,26)],
            "formula": "ax mod 26",
        },
    "Sustitucion" : {

        },
    "Permutacion" : {
            "num": 5,
            "name": ["a", "b"],
            "type": ["int"],
            "range": [str(x) for x in range(1,26)],
            "formula": "ax mod 26",

        },
    "Hill" : {

        },
    "Vigenere" : {

        }, 
}