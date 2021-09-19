def suma(a, b):
    s = a + b
    return s #para que sirve linea en este caso del ejemplo?... El resultado de la funcion se almacena en la variable s pero no se usa nunca esa variable... cuando el control vuelve al flujo principal del programa, la variable s deja de existir.

z = suma(3, 4)
print("3 + 4 =", z)

x = int(input("Ingrese el primer sumando: "))
y = int(input("Ingrese el segundo sumando: "))
z = suma(x, y)
print("x + y =", z)