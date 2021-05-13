def run():
    lim_inf = float(input('Ingrese un valor de limite inferior: '))
    lim_sup = float(input('Ingrese un valor de limite superior: '))
    while True:
        num = float(input('Ingrese un numero de comparacion: '))
        print(num)
        if lim_inf < num and lim_sup > num:
            return False
                       

if __name__ == '__main__':
    run()