class User:
    def __init__(self, nombre, apellido, telefono, correo, pais, comentario, code):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.pais = pais
        self.comentario = comentario
        self.code = code

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "telefono": self.telefono,
            "correo": self.correo,
            "pais": self.pais,
            "comentario": self.comentario,
            "code": self.code  # Asumimos que self.code es una cadena de texto
        }