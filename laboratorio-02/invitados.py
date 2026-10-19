
invitados = []

for numero in range(1, 6):
    nombre = input(f"Nombre del invitado {numero}: ").strip()
    invitados.append(nombre)

print("Cantidad de invitados:", len(invitados))
print("Invitados:", invitados)

