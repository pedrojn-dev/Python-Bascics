class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre # Atributo
        self.categoria = categoria
        self.precio = precio # Default: Public, PROTECTED, PRIVATE

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoría: { self.categoria }, Precio: { self.precio }')
    
    # GETTERS Y SETTERS - GET = Obtiene un valor, SET = Agrega un valor
    def get_precio(self):
        print(self.precio)

    def set_precio(self, precio):
        self.precio = precio


# Crear una clase hijo de Restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio, piscina):
        super().__init__(nombre, categoria, precio)
        self.piscina = piscina

    # Reescribir un método (debe llamarse igual)
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoría: { self.categoria }, Precio: { self.precio }, Piscina: {self.piscina}')

    # Agregar un método que solo exista en hotel
    def get_piscina(self):
        return self.piscina

hotel = Hotel('Hotel POO', '5 Estrellas', 200, 'Si')
hotel.mostrar_informacion()
piscina = hotel.get_piscina()
print(piscina)