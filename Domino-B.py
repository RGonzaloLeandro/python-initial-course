def cantidadFichas(max_value):
    fichas = []
    for i in range(0,max_value+1):
        for j in range(0,max_value+1):
            if [j,i] not in fichas:
                fichas.append([i,j])

    for ficha in fichas:
        print(str(ficha[0]) + '-' + str(ficha[1]))

    print('Cantidad de fichas: ' + str(len(fichas)))

n = int(input("Ingresá el máximo valor de ficha: "))
cantidadFichas(n) 