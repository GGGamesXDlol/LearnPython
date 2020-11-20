from sys import argv

script, user_name = argv
prompt = '> '

print(f"""Hola {user_name}, soy {script}.
Tres preguntas:
¿Ves a Vegetta777?
""")
Ver = input(prompt)

print("¿Estas suscrito?")
suscrito = input(prompt)

print("¿Te as unido?")
unido = input(prompt)

print(f"""Entoces {Ver} ves a Vegetta777, {suscrito} estas suscrito a Vegetta777, y {unido} estas unido al canal Vegetta777.""")
