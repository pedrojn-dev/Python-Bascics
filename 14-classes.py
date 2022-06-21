class Restaurant:

    def agregar_restaurant(self, nombre):
        self.nombre = nombre # Atributo
    
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')
    
# Instanciar la clase
restaurant = Restaurant()
restaurant.agregar_restaurant('Pizzeria Peru')
restaurant.mostrar_informacion()

restaurant2 = Restaurant()
restaurant2.agregar_restaurant('Hamburguesas Python')
restaurant2.mostrar_informacion()


# Mostrar la información
print(f'Nombre Restaurant: {restaurant.nombre}')
print(f'Nombre Restaurant: {restaurant2.nombre}')
