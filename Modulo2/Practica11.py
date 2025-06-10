#verifica usuario y contraseña
usuario = input("Ingrese un usuario: ")
contrasena = input("Ingrese un contraseña: ")

if usuario == "admin" and contrasena == "1234":
    print("Acceso concedido")

else:
    print("Acceso denegado")