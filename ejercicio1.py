def hanoi(n_discos,t_inicial,t_auxiliar,t_final):

    if n_discos==1:
        print(f"movimiento disco 1 de Torre {t_inicial} a Torre {t_final}")
    else:
        hanoi(n_discos-1,t_inicial,t_final,t_auxiliar)
        print(f"movimiento disco {n_discos} de Torre {t_inicial} a Torre {t_final}")
        hanoi(n_discos-1,t_auxiliar,t_inicial,t_final)

def n_movimientos(discos):
    return (2**discos)-1

discos=int(input("Ingrese el número de discos:"))

hanoi(discos,"A","B","C")
print(f"El numero de discos es:{n_movimientos(discos)}")


