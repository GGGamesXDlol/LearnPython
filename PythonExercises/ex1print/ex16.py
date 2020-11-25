from sys import argv

script, filename = argv

print(f"-Vamos a borrar una cosa, no es importante se llama {filename}.")
print("-No, no borres eso tengo cosas importantes ahí.")
print("-No te preocupes si no quieres borrarlo precesiona CTRL-C (^C).")
print("Si quieres hacerlo presiona ENTER.")

input("?")

print("Abriendo archivo para destruir su contenido...")
target = open(filename, 'w')
print("El archivo se borrará en 5 segundos, es mentira la hará ahora.")
target.truncate()

print("Ahora escribe lo que quieras que se escriba en 3 lineas:")

linea1 = input("linea 1:")
linea2 = input("linea 2:")
linea3 = input("linea 3:")

print("escribiendo...")

target.write(linea1)
target.write("\n")
target.write(linea2)
target.write("\n")
target.write(linea3)
target.write("\n")

print("Listop.")
print("Cerrando...")
target.close()
