#Escribir una función que chequee los siguientes usuarios y contraseñas:
#Usuario: Juan
#Contraseña: 12345_
#Usuario: Pablo
#Contraseña: xDcFvGbHn
#La función debe recibir como parámetros el usuario y la contraseña, y debe devolver el valor True o False.

def chkpassword (u,p):
    if u == "Juan" and p == "12345_":
        resultado = True
    elif u == "Pablo" and p == "xDcFvGbHn":
        resultado = True
    
    else:
        resultado = False
    return resultado


usuario = input("Usuario?")
password = input("Password?")

validacion = chkpassword(usuario, password)
print(validacion)


        