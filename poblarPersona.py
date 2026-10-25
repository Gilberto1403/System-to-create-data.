import random
#Abre el archivo txt en modo append (al final de la cadena)
#Carga el archivo en el objeto especificado despues del as
with open('poblado/values/valoresPersona.txt', 'a', encoding='utf8') as txtPersona:
    id = 0

    #Abre el archivo txt en modo de solo lectura
    with open('poblado/data/persona/nombrePersona.txt', 'r', encoding='utf8') as txtNombre:
        #Recorre el archivo txt linea por linea. Almacena el valor de la linea en "nombre"
        for nombre in txtNombre:
            #strip() quita el salto de linea al final de variable. Al recuperar la linea del archivo txt, la recupera junto con todo y salto de linea
            nombre = nombre.strip()

            with open('poblado/data/persona/apellidoPersona.txt', 'r', encoding='utf8') as txtApellido:
                #Recorre el archivo txt linea por linea. Almacena el valor de la linea en "apellido"
                for apellido in txtApellido:
                    apellido = apellido.strip()
                    with open('poblado/data/persona/direccionPersona.txt', 'r', encoding='utf8') as txtDireccion:
                        #Recorre el archivo txt linea por linea. Almacena el valor de la linea en "direccion"
                        for direccion in txtDireccion:
                            direccion = direccion.strip()

                            #Incrementa el id
                            id += 1
                            strId = str(id)

                            #--------------------Escribe una linea (registro) en el archivo txt
                            txtPersona.write(strId)
                            txtPersona.write(',')
                            txtPersona.write(f"'{nombre}'")
                            txtPersona.write(',')
                            txtPersona.write(f"'{apellido}'")
                            txtPersona.write(',')
                            txtPersona.write(f"'{direccion}'")
                            txtPersona.write(',')

                            numero = random.randint(1, 9999999999)
                            numero = str(numero)

                            txtPersona.write(f"'{numero}'")
                            txtPersona.write(',')

                            correo = nombre + apellido + strId + '@gmail.com'

                            txtPersona.write(f"'{correo}'")
                            txtPersona.write('\n')


