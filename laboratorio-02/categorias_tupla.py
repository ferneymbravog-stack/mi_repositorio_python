
categorias = ("Hogar", "Tecnología", "Deportes", "Papelería")

print("Categorías disponibles:")
for numero, categoria in enumerate(categorias, start=1):
    print(numero, "-", categoria)

elegida = input("Categoría: ").strip()

if elegida in categorias:
    print("Categoría válida.")
else:
    print("Categoría no registrada.")

print("Cantidad de categorías disponibles:", len(categorias))

