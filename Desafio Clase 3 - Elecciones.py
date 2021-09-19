# Desafio 3 - Elecciones

total_votos = int(input())
recuento = {}
#candidatos = []

if total_votos >= 0 and total_votos <= 100:

    for x in range(total_votos):
        voto = input()
        recuento[voto] = recuento.get(voto, 0) + 1
        #if not voto in candidatos:
        #    candidatos.append(voto)

    votos_posible_ganador = 0

    #clave_cand = ""

    for clave_cand in recuento:
        if recuento[clave_cand] > votos_posible_ganador:
            votos_posible_ganador = recuento[clave_cand]
            ganador = clave_cand
      
    print("Ganador:", ganador)




