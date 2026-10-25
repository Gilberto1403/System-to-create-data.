import random
from datetime import date

with open('poblado/values/valoresProveedor.txt', 'a', encoding='utf8') as txtProveedor:
    #Metodo para obtener la direccion de cada linea del archivo txt
    def getDireccion():
        with open('poblado/data/proveedor/direccionProveedor.txt', 'r', encoding='utf8') as txtDireccion:
            direccion = txtDireccion.readline()
            return direccion
        
    id = 0
        
    with open('poblado/data/proveedor/nombreProveedor.txt', 'r', encoding='utf8') as txtNombre:
        for nombre in txtNombre:
            id += 1
            #strip() Elimina el salto de linea al final de la variable
            nombre = nombre.strip()
            #Convierte id a string
            strId = str(id)
            #write - Escribe en cada linea el string dado
            txtProveedor.write(strId)
            txtProveedor.write(',')
            txtProveedor.write(f"'{nombre}'")
            txtProveedor.write(',')

            #Genera un numero aleatorio de 10
            numero = random.randint(1, 9999999999)
            numero = str(numero)

            txtProveedor.write(f"'{numero}'")
            txtProveedor.write(',')

            #Llama al metodo anterior para obtener la direccion
            direccion = getDireccion()
            direccion = direccion.strip()

            #Elimina caracteres especiales de la variable nombre
            caracteres = "' &áéíóúÁÉÍÓÚ."
            for c in range(len(caracteres)):
                nombre = nombre.replace(caracteres[c], "")
            
            #Crea el correo a partir del nombre
            correo = nombre + f'@{nombre}.com'

            txtProveedor.write(f"'{direccion}'")
            txtProveedor.write(',')
            #Obtiene la fecha
            txtProveedor.write(f"'{date.today()}'")
            txtProveedor.write(',')
            #Salto de linea, para escribir el siguiente registro
            txtProveedor.write('\n')

    