def add(a, b):
    print(f"sumando {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"restando {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"multiplicando {a} * {b}")
    return a * b


def divide(a, b):
    print(f"dividiendo {a} / {b}")
    return a / b

print("""Me pregunto 4 cosas:
¿Cuánto iq tengo?
¿Qué tan ágil soy?
¿Soy bueno jugando?
Y...
¿Qué tan simpático soy?
""")

ágil = add(2, 4)
simpático = subtract(10, 3)
iq = multiply(1000, 3)
jugando = divide(20, 2)

print(f"Segun los resultados de este test tengo {ágil} en agilidad, tengo {simpático} en simpaticidad, tengo {iq} de IQ y tengo un {jugando} en mi manera de jugar.")
print("." * 20)
print("Estoy orgulloso de mi mismo :v.")
