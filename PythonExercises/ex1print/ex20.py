from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print(f"Hora de ir inspeccionar este burrito con el nombre de {input_file}.\n")

print_all(current_file)

print("Ya lo vimos desde afuera hacia adentro, ahora rebobinemos.")

rewind(current_file)

print("Veamos que dice en su defensa:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
