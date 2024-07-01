

def validar_int(prompt):
    value = input(prompt)
    while not value.isnumeric():
        print("Error! dato invalido")
        value = input(prompt)
    return int(value)


def validar_str(prompt):
    value = input(prompt)
    while value.isnumeric():
        print("Error! dato invalido")
        value = input(prompt)
    return value

def opciones(cantidad, prompt):
    value = input(prompt)
    while not value.isnumeric() or int(value) not in range(1, cantidad+1):
        print("Error! dato invalido")
        value = input(prompt)
    return int(value)

def validar_asiento(mapa):
    letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    value = input("Ingrese el numero y letra de asiento: ")
    while len(value) <= 0 or not value[:-1].isnumeric() or value[-1].isnumeric():
        print("Error! dato invalido")
        value = input("Ingrese el numero y letra de asiento: ")
    while value[-1] not in letras or int(value[:-1]) < 0 or int(int(value[:-1]) > len(mapa)):
        print("Error! dato invalido")
        value = input("Ingrese el numero y letra de asiento: ")

    for idx1, asientos in enumerate(mapa):
        for idx2, asiento in enumerate(asientos):
            if asiento == [value]:
                mapa[idx1][idx2] = [f"{value}-O"]
                print("Se ha comprado el boleto con exito!")
                return value
            
            elif asiento == [f"{value}-O"]:
                print("El asiento ya esta ocupado...")
                break
    
    return value
    
        
            
