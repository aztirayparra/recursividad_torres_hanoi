contador=0
def hanoi(n_discos,t_inicial,t_auxiliar,t_final):
    global contador

    if n_discos==1:
        contador+=1
        print(f"movimiento {contador}: disco 1 de Torre {t_inicial} a Torre {t_final}")
    else:
        hanoi(n_discos-1,t_inicial,t_final,t_auxiliar)
        contador += 1
        print(f"movimiento {contador}: disco {n_discos} de Torre {t_inicial} a Torre {t_final}")
        hanoi(n_discos-1,t_auxiliar,t_inicial,t_final)
    

def n_movimientos(discos):
    return (2**discos)-1
while True:
    try:
        discos=int(input("Ingrese el número de discos:"))
    except ValueError:
        print("Se debe ingresar un valor numerico")
    if discos==0:
            print("No hay discos, así que no se puede realizar algún proceso, intenta de nuevo")
    elif discos>20:
            print("La cantidad de discos es demasiada, intenta con un valor más pequeño(1-20)")
    else:
        torrei=input("ingrese el nombre de la torre inicial: ") or "A"
        torreaux=input("ingrese el nombre de la torre auxiliar: ") or "B"
        torref=input("ingrese el nombre de la torre final: ") or"c"
        break
 
hanoi(discos,torrei,torreaux,torref)
print(f"El numero de movimientos es:{n_movimientos(discos)}")




