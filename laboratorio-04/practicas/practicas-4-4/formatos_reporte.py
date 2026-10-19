class ReporteTexto:
    def generar(self, datos):
        return "Datos del reporte: " + ", ".join(str(dato) for dato in datos)


class ReporteResumen:
    def generar(self, datos):
        return f"El reporte contiene {len(datos)} registros."


datos = ["Teclado", "Mouse", "Monitor"]
reportes = [ReporteTexto(), ReporteResumen()]

for reporte in reportes:
    print(reporte.generar(datos))

