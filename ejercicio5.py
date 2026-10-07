class NodoMCU:
    def __init__(self, nombre, is_hero):
        self.nombre = nombre
        self.is_hero = is_hero  # True: Héroe, False: Villano
        self.izq = None
        self.der = None

def insertar(raiz, nombre, is_hero):
    if raiz is None:
        return NodoMCU(nombre, is_hero)
    if nombre < raiz.nombre:
        raiz.izq = insertar(raiz.izq, nombre, is_hero)
    else:
        raiz.der = insertar(raiz.der, nombre, is_hero)
    return raiz

def inorden_villanos(raiz):
    if raiz is not None:
        inorden_villanos(raiz.izq)
        if not raiz.is_hero:
            print(raiz.nombre)
        inorden_villanos(raiz.der)

def heroes_con_c(raiz):
    if raiz is not None:
        heroes_con_c(raiz.izq)
        if raiz.is_hero and raiz.nombre.startswith('C'):
            print(raiz.nombre)
        heroes_con_c(raiz.der)

def contar_heroes(raiz):
    if raiz is None:
        return 0
    cuenta = 1 if raiz.is_hero else 0
    return cuenta + contar_heroes(raiz.izq) + contar_heroes(raiz.der)

def busqueda_proximidad(raiz, texto):
    if raiz is not None:
        if texto.lower() in raiz.nombre.lower():
            return raiz
        izq = busqueda_proximidad(raiz.izq, texto)
        if izq: return izq
        return busqueda_proximidad(raiz.der, texto)
    return None

def corregir_doctor_strange(raiz):
    nodo = busqueda_proximidad(raiz, "Doctor")
    if nodo:
        nodo.nombre = "Doctor Strange"
        return True
    return False

def descendente_heroes(raiz):
    if raiz is not None:
        descendente_heroes(raiz.der)
        if raiz.is_hero:
            print(raiz.nombre)
        descendente_heroes(raiz.izq)

def generar_bosque(raiz, arbol_heroes, arbol_villanos):
    if raiz is not None:
        if raiz.is_hero:
            arbol_heroes = insertar(arbol_heroes, raiz.nombre, True)
        else:
            arbol_villanos = insertar(arbol_villanos, raiz.nombre, False)
        arbol_heroes, arbol_villanos = generar_bosque(raiz.izq, arbol_heroes, arbol_villanos)
        arbol_heroes, arbol_villanos = generar_bosque(raiz.der, arbol_heroes, arbol_villanos)
    return arbol_heroes, arbol_villanos

def contar_nodos(raiz):
    if raiz is None:
        return 0
    return 1 + contar_nodos(raiz.izq) + contar_nodos(raiz.der)

def inorden_simple(raiz):
    if raiz is not None:
        inorden_simple(raiz.izq)
        print(raiz.nombre)
        inorden_simple(raiz.der)

if __name__ == "__main__":
    raiz_mcu = None
    datos_mcu = [
        ("Iron Man", True), ("Thanos", False), ("Captain America", True),
        ("Loki", False), ("Thor", True), ("Doctor", True),
        ("Black Widow", True), ("Ultron", False), ("Captain Marvel", True),
        ("Hela", False), ("Spider-Man", True)
    ]

    for nombre, is_hero in datos_mcu:
        raiz_mcu = insertar(raiz_mcu, nombre, is_hero)

    print("--- b. Villanos en orden alfabético ---")
    inorden_villanos(raiz_mcu)

    print("\n--- c. Superhéroes que empiezan con C ---")
    heroes_con_c(raiz_mcu)

    print(f"\n--- d. Cantidad de superhéroes: {contar_heroes(raiz_mcu)} ---")

    print("\n--- e. Corrigiendo 'Doctor' a 'Doctor Strange' ---")
    corregir_doctor_strange(raiz_mcu)
    print("Corrección aplicada.")
    
    print("\n--- f. Superhéroes en orden descendente ---")
    descendente_heroes(raiz_mcu)

    print("\n--- g. Generando bosque ---")
    arbol_heroes, arbol_villanos = generar_bosque(raiz_mcu, None, None)
    print(f"Nodos Héroes: {contar_nodos(arbol_heroes)} | Nodos Villanos: {contar_nodos(arbol_villanos)}")
