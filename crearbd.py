!/usr/bin/env python3

#Seleccionamos las rutas
import os
print("Introduce un directorio válido")
#Permitimos que el usuario introduzca la ruta por pantalla
ruta = input()
#Comprobamos que la ruta existe
if os.path.isdir(ruta) == False:
    print ("El directorio no existe")
else:
    #Contamos el número de archivos del directorio, si es 0 mostramos un mensaje de error
    #https://stackoverflow.com/questions/27694713/count-files-in-folder-by-python-programming    
    num_archivos = len([f for f in os.listdir(ruta) if os.path.isfile(os.path.join(ruta, f))])
    
    if num_archivos  == 0:
        print("No hay ningún archivo en ese directorio")
    else:
        print("Selecciona el dato que quieres buscar")
        print("Nombre, apellidos o ambos")
        datosabuscar = input()
        if datosabuscar:
            print("Buscando elementos que coincidan con los campos introducidos...")
        else:
            print("Debes introducir los datos")
