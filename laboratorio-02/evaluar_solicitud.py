
edad = int(input("Edad: "))
inscrito = input("¿Está inscrito? (si/no): ").strip().lower() == "si"
documentos = int(input("Número de documentos entregados: "))

cumple_edad = edad >= 16
cumple_documentos = documentos >= 3

if cumple_edad and inscrito and cumple_documentos:
    print("La solicitud cumple todos los requisitos.")
else:
    print("La solicitud NO cumple los requisitos. Faltan:")
    if not cumple_edad:
        print("- Edad mínima de 16 años.")
    if not inscrito:
        print("- Estar inscrito.")
    if not cumple_documentos:
        print("- Entregar al menos 3 documentos.")

