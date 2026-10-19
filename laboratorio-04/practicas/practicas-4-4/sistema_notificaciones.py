class Notificacion:
    def enviar(self, mensaje):
        raise NotImplementedError("Cada notificación debe implementar enviar.")


class NotificacionCorreo(Notificacion):
    def enviar(self, mensaje):
        return f"Correo enviado: {mensaje}"


class NotificacionConsola(Notificacion):
    def enviar(self, mensaje):
        return f"Consola: {mensaje}"


notificaciones = [NotificacionCorreo(), NotificacionConsola()]

for notificacion in notificaciones:
    print(notificacion.enviar("El inventario fue actualizado."))

