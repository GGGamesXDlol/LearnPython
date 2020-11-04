Ufos = 140
Naves = 300
Gente_en_cola = 1200
Pasajeros_de_ufos = 20
Pasajeros_de_naves = Gente_en_cola - 700 - Naves
Conductores_disponibles = Ufos - Pasajeros_de_ufos
Voladores_disponibles = Pasajeros_de_naves - Naves
Naves_ocupadas = Voladores_disponibles + Naves
Ufos_ocupados = Conductores_disponibles + Ufos


print("Hola gtrqjska (nombre de alienijena (mujer)) hay " Naves_ocupadas " creo que no nos alcanzan sitios quedan porque quedan " Gente_en_cola " personas esperando.")
print("No pasa nada jejsfegre (nombre de alienijena (hombre)) iremos otro día de vijaje.")
print("ok nos vemos en una semana gtrqjska")
