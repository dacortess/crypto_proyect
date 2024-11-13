def desplazamiento_encrypt(value: str) -> str:
    from random import randint

    key = randint(1,25)
    value = value.upper()
    new_value = ''

    for char in value:
        n_char = ord(char)
        if n_char == 32: continue
        new_value += chr(((n_char - 65 + key) % 26) + 65)

    return new_value, f"a = {key}"

def afin_encrypt(value: str) -> str:
    from random import randint

    key_a = randint(1,25)
    while key_a == 13: key_a = randint(1,25)

    key_b = randint(1,25)
    
    value = value.upper()
    new_value = ''

    for char in value:
        n_char = ord(char)
        if key_a % 2 == 0 or key_a == 13: continue
        if n_char == 13: continue
        new_value += chr((((key_a * (n_char - 65)) + key_b) % 26) + 65)

    return new_value, f" a = {key_a}, b = {key_b}"



methods = {
    "Desplazamiento": desplazamiento_encrypt,
    "Afin": afin_encrypt
    }



#####################################
#####       ONLY FOR DEBUG      #####
#####################################

def main() -> None:

    while True:
        print(  "\n#####################################" + 
                "\n\n" +
                "SISTEMA DE ENCRIPTADO" + 
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
            value, key = desplazamiento_encrypt(input("\nTexto a encriptar: "))
            print(value)
            print(key) if input("\n¿Mostrar la llave? [Y/n]: ") in {'Y', 'y'} else None
        if user_input == 2:
            print("\nENCRIPTADO AFIN")
            value, keys = afin_encrypt(input("\nTexto a encriptar: "))
            print(value)
            print(keys) if input("\n¿Mostrar las llaves? [Y/n]: ") in {'Y', 'y'} else None
        if user_input == 3:
            pass
