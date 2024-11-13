def desplazamiento_encrypt(value: str) -> str:
    value = value.upper()
    possible_values = list()

    for key in range(1,26):
        new_value = ''
        for char in value:
            n_char = ord(char)
            if n_char == 32: continue
            new_value += chr(((n_char - 65 - key) % 26) + 65)
        possible_values.append((str(new_value), str(key)))

    return possible_values

def afin_encrypt(value: str) -> str:

    def inverso(num: int) -> int:
        for inv in range(0,26):
            if (num*inv) % 26 == 1:
                return inv

    value = value.upper()
    possible_values = list()

    for key_a in range(1,25):
        if key_a % 2 == 0 or key_a == 13: continue
        for key_b in range(1,25):
            new_value = ''
            for char in value:
                n_char = ord(char)
                if n_char == 32: continue
                new_value += chr(((key_a * (n_char - 65 - key_b)) % 26) + 65)
            
            possible_values.append((str(new_value), str(inverso(key_a)), str(key_b)))

    return possible_values



methods = {
    "Desplazamiento": desplazamiento_encrypt,
    "Afin": afin_encrypt
    }



#####################################
#####       ONLY FOR DEBUG      #####
#####################################

def main() -> None:
    from pprint import pprint

    while True:
        print(  "\n#####################################" + 
                "\n\n" +
                "SISTEMA DE DESENCRIPTADO" + 
                "\n\n" +
                "1. desplazamiento (Desplazamiento)" + 
                "\n" +
                "2. Afin" + 
                "\n" +
                "3. RSA" + 
                "\n" +
                "0. Salir" + 
                "\n"  )
        
        user_input = int(input("Seleccione el tipo de encriptado: "))
        
        while user_input not in {0,1,2,3}:
            user_input = int(input("Seleccione un valor valido: "))
            
        print("\n#####################################")

        if user_input == 0:
            break
        if user_input == 1:
            print("\nENCRIPTADO desplazamiento")
            value = desplazamiento_encrypt(input("\nTexto a desencriptar: "))
            pprint(value)
        if user_input == 2:
            print("\nENCRIPTADO AFIN")
            value = afin_encrypt(input("\nTexto a desencriptar: "))
            pprint(value)
        if user_input == 3:
            pass
