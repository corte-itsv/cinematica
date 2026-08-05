"""Cálculos cinemáticos para diferentes tipos de movimiento.

Este módulo contiene las funciones para calcular las trayectorias de:
- Movimiento Rectilíneo Uniforme (MRU)
- Movimiento Rectilíneo Uniformemente Variado (MRUV)
- Tiro Oblicuo (Movimiento parabólico)

Todos los cálculos y estructuras de datos se resuelven utilizando listas de Python,
la cantidad de divisiones y el módulo estándar 'math' para evitar dependencias de numpy.
"""

import math
import fisica.constantes as constantes

def calcular_lista_tiempo(tiempo_final: float, divisiones: int) -> list[float]:
    """Genera una lista de tiempos desde 0 hasta tiempo_final dividida en N intervalos."""
    lista_tiempos = []
    tiempo_div = tiempo_final / divisiones

    for division in range(divisiones): 
        tmp = tiempo_div * (division + 1)
        lista_tiempos.append(tmp)

    return lista_tiempos


# --- FUNCIONES DE MRU ---

def calcular_posicion_mru(posicion_inicial: float, velocidad: float, t: float) -> float:
    """Calcula la posición para un MRU en un tiempo t."""
    posicion_x_tiempo = posicion_inicial + velocidad * t
    return posicion_x_tiempo

def mru(
    posicion_inicial: float,
    velocidad: float,
    tiempo_final: float,
    divisiones: int,
) -> dict[str, list[float]]:
    """Calcula la posición, velocidad y aceleración para un MRU."""
    lista_tiempos = calcular_lista_tiempo(tiempo_final, divisiones)

    dicc_mru = {
        "t": lista_tiempos,
        "x": [],
        "v": [],
        "a": [0.0] * divisiones
    }

    for i in range(divisiones):
        t = lista_tiempos[i]

        dicc_mru["v"].append(velocidad)

        x = calcular_posicion_mru(posicion_inicial, velocidad, t)
        dicc_mru["x"].append(x)

    return dicc_mru


# --- FUNCIONES DE MRUV ---

def calcular_posicion_mruv(posicion_inicial: float, velocidad_inicial: float, aceleracion: float, t: float) -> float:
    """Calcula la posición para un MRUV en un tiempo t."""
    posicion_final = posicion_inicial + velocidad_inicial * t + 0.5 * aceleracion * (t ** 2)
    return posicion_final

def calcular_velocidad_mruv(velocidad_inicial: float, aceleracion: float, t: float) -> float:
    """Calcula la velocidad para un MRUV en un tiempo t."""
    v = velocidad_inicial + aceleracion * t
    return v

def mruv(
    posicion_inicial: float,
    velocidad_inicial: float,
    aceleracion: float,
    tiempo_final: float,
    divisiones: int,
) -> dict[str, list[float]]:
    """Calcula la posición, velocidad y aceleración para un MRUV."""
    lista_tiempos = calcular_lista_tiempo(tiempo_final, divisiones)

    dicc_mruv = {
        "t": lista_tiempos,
        "x": [],
        "v": [],
        "a": []
    }

    for i in range(divisiones):
        t = lista_tiempos[i]

        dicc_mruv["a"].append(aceleracion)

        v = calcular_velocidad_mruv(velocidad_inicial, aceleracion, t)
        dicc_mruv["v"].append(v)

        posicion = calcular_posicion_mruv(posicion_inicial, velocidad_inicial, aceleracion, t)
        dicc_mruv["x"].append(posicion)

    return dicc_mruv


# --- FUNCIONES DE TIRO OBLICUO ---

def obtener_componentes_velocidad(velocidad_inicial: float, angulo: float) -> tuple[float, float]:
    """Calcula las componentes horizontal (x) y vertical (y) de la velocidad inicial."""
    angulo_rad = math.radians(angulo)
    v0x = velocidad_inicial * math.cos(angulo_rad)
    v0y = velocidad_inicial * math.sin(angulo_rad)
    return v0x, v0y

def calcular_tiempo_vuelo(velocidad_inicial_y: float, altura_inicial: float) -> float:
    """Calcula el tiempo de vuelo de un tiro oblicuo hasta que vuelve a y = 0."""
    gravedad = constantes.G
    tiempo_vuelo = (velocidad_inicial_y + math.sqrt(velocidad_inicial_y**2 + 2 * gravedad * altura_inicial)) / gravedad
    return tiempo_vuelo

def tiro_oblicuo(
    velocidad_inicial: float,
    angulo: float,
    altura_inicial: float,
    divisiones: int,
) -> dict[str, list[float]]:
    """Calcula las variables de la trayectoria de un tiro oblicuo."""
    velocidad_inicial_x, velocidad_inicial_y = obtener_componentes_velocidad(velocidad_inicial, angulo)

    tiempo_vuelo = calcular_tiempo_vuelo(velocidad_inicial_y, altura_inicial)
    lista_tiempos_vuelo = calcular_lista_tiempo(tiempo_vuelo, divisiones)

    gravedad = constantes.G

    dicc_oblicuo = {
        't': lista_tiempos_vuelo,
        'x': [],
        'y': [],
        'vx': [velocidad_inicial_x] * divisiones,
        'vy': [],
        'ax': [0.0] * divisiones,
        'ay': [-gravedad] * divisiones
    }

    for i in range(divisiones):
        t = lista_tiempos_vuelo[i]

        x = velocidad_inicial_x * t
        dicc_oblicuo['x'].append(x)

        y = calcular_posicion_mruv(altura_inicial, velocidad_inicial_y, -gravedad, t)
        dicc_oblicuo['y'].append(y)

        vy = calcular_velocidad_mruv(velocidad_inicial_y, -gravedad, t)
        dicc_oblicuo['vy'].append(vy)

    return dicc_oblicuo