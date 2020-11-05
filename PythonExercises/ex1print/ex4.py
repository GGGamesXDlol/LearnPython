Ufos = 140
Naves = 300
Gente_en_cola_naves = 1200
Gente_en_cola_ufos = Ufos - Naves
Pasajeros_de_ufos = 20
Pasajeros_de_naves = Gente_en_cola_naves - 700 - Naves
Conductores_disponibles = Ufos - Pasajeros_de_ufos
Voladores_disponibles = Pasajeros_de_naves - Naves
Naves_ocupadas = Voladores_disponibles + Naves
Ufos_ocupados = Conductores_disponibles + Ufos


print("Hola gtrqjskA (nombre de alienijena (mujer)) hay", Naves_ocupadas, "naves ocupadas creo que no nos alcanzan sitios quedan porque quedan", Gente_en_cola_naves, "personas esperando.")
print("\n")
print("No pasa nada jejsfegrE (nombre de alienijena (hombre)) iremos otro día de viaje.")
print("\n")
print("ok nos vemos en una semana gtrqjskA.")
print("\n")
print('"Una semana despues"')
print("\n")
print("Hola jejsfegrE creo que hoy iremos en ufo porque solo hay", Gente_en_cola_ufos, "personas esperando para ufos.")
print("\n")
print("[jejsfegrE] Pues si porque hay", Conductores_disponibles, "ufos libres para ir a Despretidfd (Roma de los aliens).")
print("\n")
print("[gtrqjskA] ¡Pues nos vamos a Despretidfd de viaje!")
