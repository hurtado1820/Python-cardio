import random

def juego(jugador,maquina):  
    if maquina == jugador:
        print("----Empate----\n")
        return(0,0)
    elif (maquina==1 and jugador==2) or (maquina==2 and jugador==3) or (maquina==3 and jugador==1):
        print("----Punto para el jugador----\n")
        return(1,0)
    elif (maquina==1 and jugador==3) or (maquina==2 and jugador==1) or (maquina==3 and jugador==2):
        print("----Punto para el computador----\n")
        return(0,1)
                    
        
def run():
    puntos_jugador = 0
    puntos_maquina = 0
    contador = 0
    while contador<3:
        jugador = int(input('''Selecciona una opcion:
        1. Piedra
        2. Papel
        3. Tijera\n'''))
        if jugador !=1 and jugador !=2 and jugador!=3:
            print("Selecciona una opcion valida\n")
            run()
        else:
            maquina = random.randint(1,3)  
            print("El computador elige la opcion: ",maquina,"\n")
            ganados_jugador,ganados_maquina=juego(jugador,maquina)
            puntos_jugador += ganados_jugador
            puntos_maquina += ganados_maquina
        if ganados_maquina != ganados_jugador:     
            contador += 1    
    if puntos_jugador == 2:
        print("\n----Gana el jugador 🥳----")
    elif puntos_maquina == 2:  
        print("\n----Gana el computador 🥳----")
    else:
        print("\n----Es un empate 😱----")      


if __name__ == '__main__':
    run()