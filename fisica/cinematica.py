"""Cálculos cinemáticos para diferentes tipos de movimiento.

Este módulo contiene las funciones para calcular las trayectorias de:
- Movimiento Rectilíneo Uniforme (MRU)
- Movimiento Rectilíneo Uniformemente Variado (MRUV)
- Tiro Oblicuo (Movimiento parabólico)

Todos los cálculos y estructuras de datos se resuelven utilizando listas de Python,
la cantidad de divisiones y el módulo estándar 'math' para evitar dependencias de numpy.
"""

#importar librerias necesarias y modulo de constantes !


def calcular_lista_tiempo(tiempo_final: float, divisiones: int) -> list[float]:
    """Genera una lista de tiempos desde 0 hasta tiempo_final dividida en N intervalos.

    Args:
        tiempo_final (float): Tiempo de finalización.
        divisiones (int): Cantidad de divisiones de tiempo.

    Returns:
        list[float]: Lista con los instantes de tiempo.
    """
    paso = tiempo_final / divisiones
    tiempos = []

    for i in range(divisiones + 1):
        tiempos.append(i * paso)

    return tiempos

# --- FUNCIONES DE MRU ---

def calcular_posicion_mru(posicion_inicial: float, velocidad: float, t: float) -> float:
    """Calcula la posición para un MRU en un tiempo t."""
    posicion=posicion_inicial+velocidad*t
    return posicion

def mru(
    posicion_inicial: float,
    velocidad: float,
    tiempo_final: float,
    divisiones: int,
) -> dict[str, list[float]]:
    """Calcula la posición, velocidad y aceleración para un MRU.

    Args:
        posicion_inicial (float): Posición inicial del móvil (en metros).
        velocidad (float): Velocidad constante del móvil (en m/s).
        tiempo_final (float): Tiempo de finalización del movimiento (en segundos).
        divisiones (int): Cantidad de divisiones de tiempo para la simulación.

    Returns:
        dict[str, list[float]]: Un diccionario con las siguientes claves:
            - 't': Lista de tiempos.
            - 'x': Lista de posiciones en función del tiempo.
            - 'v': Lista de velocidades en función del tiempo.
            - 'a': Lista de aceleraciones en función del tiempo.

    Valida que el tiempo final sea positivo y que la cantidad de divisiones sea mayor a cero
    """
    lista_tiempos=calcular_lista_tiempo(tiempo_final, divisiones)
    diccionario_mru={"t":[lista_tiempos], 
                     "x":[],
                     "v":[],
                     "a":[]}

    for i in range(divisiones):
        t=lista_tiempos[i]
        v=velocidad
        diccionario_mru["v"].append(v)
        
        x=calcular_posicion_mru(posicion_inicial,v,t)
        diccionario_mru["x"].append(x)
        

# --- FUNCIONES DE MRUV ---


def calcular_posicion_mruv(
    posicion_inicial: float,
    velocidad_inicial: float,
    aceleracion: float,
    t: float,
) -> float:
    """Calcula la posición para un MRUV en un tiempo t."""
    posicion=posicion_inicial+velocidad_inicial*t+0.5*aceleracion*t*t
    return posicion


def calcular_velocidad_mruv(velocidad_inicial: float, aceleracion: float, t: float) -> float:
    """Calcula la velocidad para un MRUV en un tiempo t."""
    velocidad=velocidad_inicial+aceleracion*t
    return velocidad


def mruv(
    posicion_inicial: float,
    velocidad_inicial: float,
    aceleracion: float,
    tiempo_final: float,
    divisiones: int,
) -> dict[str, list[float]]:
    """Calcula la posición, velocidad y aceleración para un MRUV.


    Args:
        posicion_inicial (float): Posición inicial del móvil (en metros).
        velocidad_inicial (float): Velocidad inicial del móvil (en m/s).
        aceleracion (float): Aceleración constante del móvil (en m/s^2).
        tiempo_final (float): Tiempo de finalización del movimiento (en segundos).
        divisiones (int): Cantidad de divisiones de tiempo para la simulación.


    Returns:
        dict[str, list[float]]: Un diccionario con las siguientes claves:
            - 't': Lista de tiempos.
            - 'x': Lista de posiciones en función del tiempo.
            - 'v': Lista de velocidades en función del tiempo.
            - 'a': Lista de aceleraciones en función del tiempo.


    Valida que el tiempo final sea positivo y que la cantidad de divisiones sea mayor a cero
    """
    lista_tiempos=calcular_lista_tiempo(tiempo_final, divisiones)
    diccionario_mruv={"t":[lista_tiempos],
                         "x":[],
                         "v":[],
                         "a":[aceleracion]}
    for i in range (divisiones):
        t=lista_tiempos[i]
        v=calcular_velocidad_mruv(velocidad_inicial, aceleracion, t)
        diccionario_mruv["v"].append(v)
        x=calcular_posicion_mruv(posicion_inicial, velocidad_inicial, aceleracion, t )
        diccionario_mruv["x"].append(x)


