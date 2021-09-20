def promediar(a,b,c):
    resultado = (a + b + c)/3
    return resultado

nota_1 = int(input("Primera nota?"))
nota_2 = int(input("Segunda nota?"))
nota_3 = int(input("Tercera nota?"))

print("El promedio es:", promediar(nota_1, nota_2, nota_3))
