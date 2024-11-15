

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

        },
    "Hill" : {

        },
    "Vigenere" : {

        }, 
}