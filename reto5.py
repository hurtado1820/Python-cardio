def run():
    lim_inf = float(input('Ingrese un valor de limite inferior: '))
    lim_sup = float(input('Ingrese un valor de limite superior: '))
    while True:
        num = float(input('Ingrese un numero de comparacion: '))
        if lim_inf < num and lim_sup > num:
            print(num)
            return False
        else:
            print(num)               


if __name__ == '__main__':
    run()