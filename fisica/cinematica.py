"""Cálculos cinemáticos para diferentes tipos de movimiento.

Este módulo contiene las funciones para calcular las trayectorias de:
- Movimiento Rectilíneo Uniforme (MRU)
- Movimiento Rectilíneo Uniformemente Variado (MRUV)
- Tiro Oblicuo (Movimiento parabólico)

Todos los cálculos y estructuras de datos se resuelven utilizando listas de Python,
la cantidad de divisiones y el módulo estándar 'math' para evitar dependencias de numpy.
"""

#importar librerias necesarias y modulo de constantes !

import math
import fisica.constantes as constantes

def calcular_lista_tiempo(tiempo_final: float, divisiones: int) -> list[float]:

    """Genera una lista de tiempos desde 0 hasta tiempo_final dividida en N intervalos.

    Args:
        tiempo_final (float): Tiempo de finalización.
        divisiones (int): Cantidad de divisiones de tiempo.

    Returns:
        list[float]: Lista con los instantes de tiempo.
    """

    lista_tiempos = []
    tiempo_div = tiempo_final / divisiones

    lista_tiempos.append(0)


    for division in range(divisiones): 
        tmp = tiempo_div * (division+1)
        lista_tiempos.append(tmp)

    return lista_tiempos


# --- FUNCIONES DE MRU ---

def calcular_posicion_mru(posicion_inicial: float, velocidad: float, t: float) -> float:

    """Calcula la posición para un MRU en un tiempo t."""

    posicion_x_tiempo = posicion_inicial + velocidad * (t - 0)
    return posicion_x_tiempo

def mru(
    posicion_inicial: float,
    velocidad: float,
    tiempo_final: float,
    divisiones: int,
) -> dict[str, list[float]]:
    """Calcula la posición, velocidad y aceleración para un MRU."""

    if tiempo_final <= 0 or divisiones <= 0:
        print("Divisiones o número de tiempo inválido.")
        return None

    lista_tiempos = calcular_lista_tiempo(tiempo_final, divisiones)

    dicc_mru = {
        "t": lista_tiempos,
        "x": [],
        "v": [],
        "a": []
    }

    for t in lista_tiempos:
        dicc_mru["v"].append(velocidad)
        dicc_mru["a"].append(0.0)
        dicc_mru["x"].append(calcular_posicion_mru(posicion_inicial, velocidad, t))

    return dicc_mru
        
            



# --- FUNCIONES DE MRUV ---

def calcular_posicion_mruv(posicion_inicial: float, velocidad_inicial: float, aceleracion: float, t: float) -> float:
    
    """Calcula la posición para un MRUV en un tiempo t."""

    posicion_final = posicion_inicial + velocidad_inicial * t + 0.5 * aceleracion * t * t
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
    if tiempo_final <= 0 or divisiones <= 0:
        print("Divisiones o número de tiempo inválido.")
        return None

    lista_tiempos = calcular_lista_tiempo(tiempo_final, divisiones)

    dicc_mruv = {
        "t": lista_tiempos,
        "x": [],
        "v": [],
        "a": []
    }


    for t in lista_tiempos:
        dicc_mruv["a"].append(aceleracion)
        
        v = calcular_velocidad_mruv(velocidad_inicial, aceleracion, t)
        dicc_mruv["v"].append(v)

        posicion = calcular_posicion_mruv(posicion_inicial, velocidad_inicial, aceleracion, t)
        dicc_mruv["x"].append(posicion)

    return dicc_mruv

    


# --- FUNCIONES DE TIRO OBLICUO ---

def obtener_componentes_velocidad(velocidad_inicial: float, angulo: float) -> tuple:
    """Calcula las componentes horizontal (x) y vertical (y) de la velocidad inicial.

    Args:
        velocidad_inicial (float): Magnitud de la velocidad inicial.
        angulo (float): Ángulo respecto a la horizontal en grados.

    Returns:
        tuple: (v0x, v0y) componentes de la velocidad inicial.
    """

    angulo_rad = math.radians(angulo)
    v0x = velocidad_inicial * math.cos(angulo_rad)
    v0y = velocidad_inicial * math.sin(angulo_rad)
    return v0x, v0y

def calcular_tiempo_vuelo(velocidad_inicial_y: float, altura_inicial: float) -> float:
    """Calcula el tiempo de vuelo de un tiro oblicuo hasta que vuelve a y = 0.

    Args:
        velocidad_inicial_y (float): Velocidad inicial vertical (v0y).
        altura_inicial (float): Altura inicial.

    Returns:
        float: Tiempo total de vuelo en segundos.

    Valida que el discriminante de la funcion cuadrática asociada sea positivo
    (2 Raices Reales Distintas)
    """

    

    gravedad = constantes.G

    g = abs(gravedad) 
    discriminante = velocidad_inicial_y**2 + 2 * g * altura_inicial

    if discriminante < 0:
            return None

    tiempo_vuelo = (velocidad_inicial_y + math.sqrt(max(0.0, discriminante))) / g
    return tiempo_vuelo

def tiro_oblicuo(
    velocidad_inicial: float,
    angulo: float,
    altura_inicial: float,
    divisiones: int,
) -> dict[str, list[float]]:
    """Calcula las variables de la trayectoria de un tiro oblicuo."""
    if divisiones <= 0:
        print("Divisiones o número de tiempo inválido.")
        return None

    velocidad_inicial_x, velocidad_inicial_y = obtener_componentes_velocidad(velocidad_inicial, angulo)
    tiempo_vuelo = calcular_tiempo_vuelo(velocidad_inicial_y, altura_inicial)

    if tiempo_vuelo is None or tiempo_vuelo <= 0:
        print("Divisiones o número de tiempo inválido.")
        return None

    lista_tiempos_vuelo = calcular_lista_tiempo(tiempo_vuelo, divisiones)
    gravedad = abs(constantes.G)

    dicc_oblicuo = {
        't': lista_tiempos_vuelo,
        'x': [],
        'y': [],
        'vx': [],
        'vy': [],
        'ax': [],
        'ay': []
    }

    # Iterar directamente sobre lista_tiempos_vuelo procesa los 11 elementos
    for t in lista_tiempos_vuelo:
        dicc_oblicuo['x'].append(velocidad_inicial_x * t)
        dicc_oblicuo['y'].append(calcular_posicion_mruv(altura_inicial, velocidad_inicial_y, -gravedad, t))
        dicc_oblicuo['vx'].append(velocidad_inicial_x)
        dicc_oblicuo['vy'].append(calcular_velocidad_mruv(velocidad_inicial_y, -gravedad, t))
        dicc_oblicuo['ax'].append(0.0)
        dicc_oblicuo['ay'].append(-gravedad)

    return dicc_oblicuo
        