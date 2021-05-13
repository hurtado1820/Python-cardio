def conversor(num):
    if num == 1:
        val_ingresado = float(input("Ingrese el valor en millas: "))
        kilometros = val_ingresado * 1.609344
        print(val_ingresado," millas equivalen a ",kilometros," kilometros")
    if num == 2:
        val_ingresado = float(input("Ingrese el valor en kilometros: "))
        millas = val_ingresado / 1.609344
        print(val_ingresado," kilometros equivalen a ",millas," millas")


def run():
    opcion = int(input('''Selecciona una opcion:
    1. Convertir millas a kilometros
    2. Convertir kilometros a millas\n'''))
    if opcion == 1 or opcion == 2:
        conversor(opcion)
    else:
        print("Elige una opcion valida\n")
        run()                        


if __name__ == '__main__':
    run()