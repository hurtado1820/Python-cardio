def area():
    base = float(input("Ingrese el valor de la base: "))
    altura = float(input("Ingrese el valor de la altura: "))
    valor = ((base*altura)/2)
    print("El area del triangulo es: ",valor, " unidades cuadradas")


def tipo():
    longitudes = input(" Ingrese el valor de los tres lados del triangulo separados por un espacio: ")
    lados = longitudes.split()
    if lados[0] == lados[1] == lados[2]:
        print("Es un triangulo equilatero")
    elif lados[0] == lados[1] or lados[1] == lados[2] or lados[2] == lados[0]:
        print("Es un triangulo isosceles")
    elif lados[0] != lados[1] != lados[2]:
        print("Es un triangulo escaleno")    

def run():
    opcion = int(input('''Seleccione una opcion:
    1. Obtener tipo de triangulo
    2. Obtener area triangulo\n'''))
    if opcion == 1:
        tipo()
    elif opcion == 2:
        area()
    else:
        print("Selecciona una opcion correcta\n")
        run()        
    

if __name__ == '__main__':
    run()
    


