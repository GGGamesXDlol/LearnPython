from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copiando archivos azules, rojos, amarillos... El caso que estamos copiando de {from_file} a {to_file}.")

in_file = open(from_file)
indata = in_file.read()

print(f"El archivo pesa untotal totalisimo apocaliptico eclosinadictico (eso creo que no existe) de {len(indata)} bytes.")

print(f"Pero la verdadera pregunta es... ¿Existe? Chan chan chaaaaaaaaaaaaaaaaaan; Comprobemoslo: {exists(to_file)}.")
print("Si lees esto es que existe, pulsa ENTER para continuar, si quieres parar pulsa CTRL-C (^C).")
input("?")

out_file = open(to_file, 'w')
out_file.write(indata)

print("Listop, cerrando")

out_file.close()
in_file.close()
