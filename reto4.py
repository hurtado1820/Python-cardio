import math

def cilindro():
    radio = float(input('\nIngrese el valor del radio: '))
    altura = float(input('Ingrese el valor de la altura: '))
    vol_cilindro = math.pi * (radio**2) * altura
    print('El volumen del cilindro es: ',vol_cilindro,'unidades cubicas')

def cubo():
    lado = float(input('\nIngresa el valor del lado del cubo: '))
    print('El volumen del cubo es: ',lado**3,'unidades cubicas')

def esfera():
    radio = float(input('\nIngresa el valor del radio de la esfera: '))
    vol_esfera = (4/3) * math.pi * (radio**3)
    print('El volumen de la esfera es: ',vol_esfera,'unidades cubicas')

def cono():
    radio = float(input('\nIngrese el valor del radio: '))
    altura = float(input('Ingrese el valor de la altura: '))
    vol_cono = (math.pi * (radio**2) * altura)/3
    print('El volumen del cono es: ',vol_cono,'unidades cubicas')
    

def run():
    opcion = int(input('''Elige la figura geometrica a la cual calcular el volumen:
    1. Cilindro
    2. Cubo
    3. Esfera
    4. Cono\n'''))
    if opcion == 1:
        cilindro()
    elif opcion == 2:
        cubo()
    elif opcion == 3:
        esfera()
    elif opcion == 4:
        cono()
    else:
        print("Elige una opcion correcta\n")
        run()                


if __name__ == '__main__':
    run()