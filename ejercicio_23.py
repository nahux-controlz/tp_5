class NodoCriatura:
    def __init__(self, nombre, derrotado_por=None):
        self.nombre = nombre
        self.derrotado_por = derrotado_por
        self.descripcion = ""
        self.izq = None
        self.der = None

def insertar_criatura(raiz, nombre, derrotado_por):
    if raiz is None:
        return NodoCriatura(nombre, derrotado_por)
    if nombre < raiz.nombre:
        raiz.izq = insertar_criatura(raiz.izq, nombre, derrotado_por)
    else:
        raiz.der = insertar_criatura(raiz.der, nombre, derrotado_por)
    return raiz

def inorden_criaturas(raiz):
    if raiz is not None:
        inorden_criaturas(raiz.izq)
        print(f"Criatura: {raiz.nombre} | Derrotada por: {raiz.derrotado_por}")
        inorden_criaturas(raiz.der)

def buscar_criatura(raiz, nombre):
    if raiz is None or raiz.nombre == nombre:
        return raiz
    if nombre < raiz.nombre:
        return buscar_criatura(raiz.izq, nombre)
    return buscar_criatura(raiz.der, nombre)

def cargar_descripcion(raiz, nombre_criatura, descripcion):
    nodo = buscar_criatura(raiz, nombre_criatura)
    if nodo:
        nodo.descripcion = descripcion

def mostrar_info_criatura(raiz, nombre_criatura):
    nodo = buscar_criatura(raiz, nombre_criatura)
    if nodo:
        print(f"Nombre: {nodo.nombre}")
        print(f"Derrotada por: {nodo.derrotado_por}")
        print(f"Descripción: {nodo.descripcion}")
    else:
        print("Criatura no encontrada.")

def contar_derrotas(raiz, conteo_heroes):
    if raiz is not None:
        if raiz.derrotado_por and raiz.derrotado_por != "-":
            conteo_heroes[raiz.derrotado_por] = conteo_heroes.get(raiz.derrotado_por, 0) + 1
        contar_derrotas(raiz.izq, conteo_heroes)
        contar_derrotas(raiz.der, conteo_heroes)

def top_3_heroes(raiz):
    conteo_heroes = {}
    contar_derrotas(raiz, conteo_heroes)
    ordenados = sorted(conteo_heroes.items(), key=lambda x: x[1], reverse=True)
    return ordenados[:3]

if __name__ == "__main__":
    raiz_criaturas = None
    datos = [
        ("Águila del Cáucaso", "-"), ("Aves del Estínfalo", "-"),
        ("Quimera", "Belerofonte"), ("Talos", "Medea"),
        ("Hidra de Lerna", "Heracles"), ("Sirenas", "-"),
        ("León de Nemea", "Heracles"), ("Pitón", "Apolo"),
        ("Esfinge", "Edipo"), ("Cierva de Cerinea", "-"),
        ("Dragón de la Cólquida", "-"), ("Basilisco", "-"),
        ("Cerbero", "-"), ("Jabalí de Erimanto", "-")
    ]

    for criatura, heroe in datos:
        raiz_criaturas = insertar_criatura(raiz_criaturas, criatura, heroe)

    print("--- a. Listado inorden de las criaturas ---")
    inorden_criaturas(raiz_criaturas)

    print("\n--- b. Cargando descripción a Talos ---")
    cargar_descripcion(raiz_criaturas, "Talos", "Autómata gigante de bronce que protegía la isla de Creta.")
    print("Descripción cargada exitosamente.")

    print("\n--- c. Mostrar información de Talos ---")
    mostrar_info_criatura(raiz_criaturas, "Talos")

    print("\n--- d. Top 3 Héroes que derrotaron más criaturas ---")
    top_heroes = top_3_heroes(raiz_criaturas)
    for i, (heroe, cantidad) in enumerate(top_heroes, start=1):
        print(f"{i}. {heroe}: {cantidad} criaturas derrotadas")
