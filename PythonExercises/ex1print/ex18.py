def print_two(*args):
    arg1, arg2 = args
    print(f"El arg1 es igual a: {arg1}, y arg2 es igual a: {arg2}.")

def print_two_again(arg1, arg2):
    print(f"Lo mismo de arriba: El arg1 es igual a: {arg1}, y arg2 es igual a: {arg2}.")

def print_one(arg1):
    print(f"Lo mismo menos uno: arg1 es: {arg1}.")

def print_none():
    print("Intenta de nuevo no hay nada que ver aquí.")


print_two("tengo", "no se")
print_two_again("tengo", "no se")
print_one("cigüeñaaaaaaa")
print_none()
