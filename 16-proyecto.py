import os

CARPETA = 'contactos/' # Carpeta de Contactos
EXTENSION = '.txt' # Extensión de archivos

#Contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    # Revisa si la carpeta eiste o no
    crear_directorio()

    #Muestra el menú de opciones
    mostrar_menu()

    # Preguntar al usuario la acción a realizar

    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opción: \r\n')
        opcion = int(opcion)

        #Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opción no válida, intente de nuevo')

def eliminar_contacto():
    nombre = input('Seleccione el Contacto que desea eliminar: \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION )
        print('\r\nEliminado Correctamente')
    except expression as identifier:
        print('No existe ese contacto')
    
    # Reiniciar la app


def buscar_contacto():
    nombre = input('Seleccione el Contacto que desea buscar: \r\n')

    try:
        with open (CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Información del Contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')
        print(IOError)
    
    # Reiniciar la app
    app()

def mostrar_contactos():
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                # Imprime los contenidos
                print(linea.rstrip())
            #Imprime un separador entre contactos
            print('\r\n')

def editar_contacto():
    print('Escribe el nombre del contacto a editar')
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n')

    #Revisar si el archivo ya existe antes de edtarlo
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:

            # Resto de los campos
            nombre_contacto = input('Agrega el Nuevo Nombre: \r\n')
            telefono_contacto = input('Agrega el Nuevo Teléfono:\r\n')
            categoria_contacto = input('Agrega la Nuevo Categoría:\r\n')

            # instanciar
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoría: ' + contacto.categoria + '\r\n')

            # Renombrar el archivo
            os.rename(CARPETA + nombre_anterior + EXTENSION, 
            CARPETA + nombre_contacto + EXTENSION)

            #Mostrar mensaje de éxito
            print('\r\n Contacto creado Correctamente \r\n')
    else:
        print('Ese contacto no existe')
    # Reiniciar la app
    app()

def agregar_contacto():
    print('Escribe los datos para agregar el nuevo Contacto')
    nombre_contacto = input('Nombre del Contacto:\r\n')

    #Revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre_contacto)

    if not existe:

        with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:

            # Resto de los campos
            telefono_contacto = input('Agrega el Teléfono:\r\n')
            categoria_contacto = input('Categoria Contacto:\r\n')

            #Instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            # Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Teléfono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoría: ' + contacto.categoria + '\r\n')

            # Mostrar un mensaje de éxito
            print('\r\n Contacto creado Correctamente \r\n')

    else:
        print('Ese contacto ya existe')

    # Reiniciar la app
    app()


def mostrar_menu():
    print('Seleccione del Menú lo que desea hacer:')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contactos')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')

def crear_directorio():
    if not os.path.exists('contactos/'):
        # crear la carpeta
        os.makedirs('contactos/')


def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()