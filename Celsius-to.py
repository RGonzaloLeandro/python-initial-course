#CREAR
#Una función que convierta grados Celsius a grados Farenheit
#Una función que convierta grados Celsius a grados Kelvin
#uario debe ingresar una temperatura en grados Celsius y el programa debe mostrar las conversiones a Farenheit y Kelvin utilizando las funciones. Si la temperatura ingresada es inferior al cero absoluto, el programa debe mostrar un mensaje de advertencia.

# Celsius a Farenheit: F = 1.8 * C + 32
# Celsius a Kelvin: 0°K = -273.15°C

def CtoF(x):
    f = round((1.8 * x + 32), 2)
    k = round(((f + 459.67)/1.8), 2)
    print(x, "°C = ", f, "°F" )
    print(x, "°C = ", k, "°K" )

c = float(input("Ingrese °C a convertir: "))
CtoF(c)