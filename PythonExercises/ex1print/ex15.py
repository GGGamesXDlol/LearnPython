from sys import argv

script, filename = argv

txt = open(filename)

print(f"Mira aquí esta tu hamburgesa: {filename}, se escondio con el nombre de {filename}.")
print("\n")
print(txt.read())
print("\n")

input("- ")
print("\n")

print(f"Ponle nombre a tu hamburguesa, dicen que si le pones nombre a lo que te comes sabe más rico :v.")
print("\n")
Nombre_falso = input("- ")
print("\n")
print(f"Espera no puedes ponerle {Nombre_falso} a tu hamburguesa, lo que me han dicho es falso, no puedes ponerle nombre a la comida, tienes que llamarle como se llama: {filename}.")
print("\n")
El_nombre = input("Nombre:- ")
print("\n")

print(f"Una pena se quedara con el nombre de: {filename}.")
print("\n")

txt_again = open(El_nombre)
print("\n")

print(txt_again.read())

input("¿Y bien? \n \n- ")
