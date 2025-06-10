# Solicitarla frase al usuario

frase = input("Ingresa una frase: ")
 
# Solicitar la palabra a ser reemplazar
palabra_a_reemplazar = input("Ingresa la palabra que quieres reemplazar: ")
 
# Solicitar la palabra nueva
palabra_nueva = input("Ingresa la nueva palabra: ")
 
# Reemplazar la palabra en la frase, utilizamos el metodo replace() que reemplaza una frase específica con otra frase específica.
frase_modificada = frase.replace(palabra_a_reemplazar, palabra_nueva)
 
# Mostrar la frase modificada
print("Frase modificada:", frase_modificada)
 