"""Cálculos cinemáticos para diferentes tipos de movimiento.

Este módulo contiene las funciones para calcular las trayectorias de:
- Movimiento Rectilíneo Uniforme (MRU)
- Movimiento Rectilíneo Uniformemente Variado (MRUV)
- Tiro Oblicuo (Movimiento parabólico)

Todos los cálculos y estructuras de datos se resuelven utilizando listas de Python,
la cantidad de divisiones y el módulo estándar 'math' para evitar dependencias de numpy.
"""

import math
import fisica.constantes as c


def calcular_lista_tiempo(tiempo_final: float, divisiones: int) -> list[float]:
    """Genera una lista de tiempos desde 0 hasta tiempo_final dividida en N intervalos.

    Args:
        tiempo_final (float): Tiempo de finalización.
        divisiones (int): Cantidad de divisiones de tiempo.

    Returns:
        list[float]: Lista con los instantes de tiempo.
    """
    dt = tiempo_final / divisiones
    t = []
    for i in range(divisiones + 1):
        t.append(i * dt)
    return t


# --- FUNCIONES DE MRU ---

def calcular_posicion_mru(posicion_inicial: float, velocidad: float, t: float) -> float:
    """Calcula la posición para un MRU en un tiempo t."""
    return posicion_inicial + velocidad * t

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
    # Validación de valores
    if tiempo_final < 0:
        print("El tiempo final no puede ser negativo.")
        return
    if divisiones <= 0:
        print("La cantidad de divisiones debe ser mayor que cero.")
        return

    t = calcular_lista_tiempo(tiempo_final, divisiones)

    x = []
    v = []
    a = []
    for ti in t:
        x.append(calcular_posicion_mru(posicion_inicial, velocidad, ti))
        v.append(velocidad)
        a.append(0.0)

    return {
        "t": t,
        "x": x,
        "v": v,
        "a": a,
    }


# --- FUNCIONES DE MRUV ---

def calcular_posicion_mruv(
    posicion_inicial: float,
    velocidad_inicial: float,
    aceleracion: float,
    t: float,
) -> float:
    """Calcula la posición para un MRUV en un tiempo t."""
    return posicion_inicial + velocidad_inicial * t + 0.5 * aceleracion * (t ** 2)


def calcular_velocidad_mruv(velocidad_inicial: float, aceleracion: float, t: float) -> float:
    """Calcula la velocidad para un MRUV en un tiempo t."""
    return velocidad_inicial + aceleracion * t


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
    # Validación de valores
    if tiempo_final < 0:
        print("El tiempo final no puede ser negativo.")
        return
    if divisiones <= 0:
        print("La cantidad de divisiones debe ser mayor que cero.")
        return

    t = calcular_lista_tiempo(tiempo_final, divisiones)

    x = []
    v = []
    a = []
    for ti in t:
        x.append(calcular_posicion_mruv(posicion_inicial, velocidad_inicial, aceleracion, ti))
        v.append(calcular_velocidad_mruv(velocidad_inicial, aceleracion, ti))
        a.append(-c.G)

    return {
        "t": t,
        "x": x,
        "v": v,
        "a": a,
    }


# --- FUNCIONES DE TIRO OBLICUO ---

def obtener_componentes_velocidad(velocidad_inicial: float, angulo: float) -> tuple:
    """Calcula las componentes horizontal (x) y vertical (y) de la velocidad inicial.

    Args:
        velocidad_inicial (float): Magnitud de la velocidad inicial.
        angulo (float): Ángulo respecto a la horizontal en grados.

    Returns:
        tuple: (v0x, v0y) componentes de la velocidad inicial.
    """
    theta = math.radians(angulo)
    v0x = velocidad_inicial * math.cos(theta)
    v0y = velocidad_inicial * math.sin(theta)
    return v0x, v0y


def calcular_tiempo_vuelo(velocidad_inicial_y: float, altura_inicial: float) -> float:
    """Calcula el tiempo de vuelo de un tiro oblicuo hasta que vuelve a y = 0.

    Args:
        velocidad_inicial_y (float): Velocidad inicial vertical (v0y).
        altura_inicial (float): Altura inicial.

    Returns:
        float: Tiempo total de vuelo en segundos.

    Valida 
    """
    discriminante = velocidad_inicial_y ** 2 + 2.0 * c.G * altura_inicial
    if discriminante < 0:
        print("No se puede calcular el tiempo de vuelo con estos parámetros.")
        return
    t_vuelo = (velocidad_inicial_y + math.sqrt(discriminante)) / c.G
    return t_vuelo


def tiro_oblicuo(
    velocidad_inicial: float,
    angulo: float,
    altura_inicial: float,
    divisiones: int,
) -> dict[str, list[float]]:
    """Calcula las variables de la trayectoria de un tiro oblicuo.

    El tiempo de vuelo se calcula automáticamente hasta que la altura vuelve a ser cero.
    El movimiento se modela como la composición de un MRU (eje X) y un MRUV (eje Y).

    Args:
        velocidad_inicial (float): Magnitud de la velocidad inicial (en m/s).
        angulo (float): Ángulo de disparo respecto a la horizontal (en grados).
        altura_inicial (float): Altura inicial desde la que se lanza el proyectil (en metros).
        divisiones (int): Cantidad de divisiones de tiempo para la simulación.

    Returns:
        dict[str, list[float]]: Un diccionario con las siguientes claves:
            - 't': Lista de tiempos de vuelo.
            - 'x': Lista de posiciones horizontales.
            - 'y': Lista de posiciones verticales (alturas).
            - 'vx': Lista de velocidad en el eje X (constante).
            - 'vy': Lista de velocidad en el eje Y.
            - 'ax': Lista de aceleración en el eje X (cero).
            - 'ay': Lista de aceleración en el eje Y (-G).
    """
    # Descomposición de la velocidad inicial
    v0x, v0y = obtener_componentes_velocidad(velocidad_inicial, angulo)

    # Cálculo del tiempo de vuelo
    t_vuelo = calcular_tiempo_vuelo(v0y, altura_inicial)

    if t_vuelo <= 0:
        print("El tiempo de vuelo calculado es cero o negativo. "
              "Asegúrese de tener una velocidad inicial o altura inicial que permita el vuelo.")
        return

    # Ejecución del movimiento horizontal (MRU)
    resultado_x = mru(
        posicion_inicial=0.0,
        velocidad=v0x,
        tiempo_final=t_vuelo,
        divisiones=divisiones
    )

    # Ejecución del movimiento vertical (MRUV)
    resultado_y = mruv(
        posicion_inicial=altura_inicial,
        velocidad_inicial=v0y,
        aceleracion=-c.G,
        tiempo_final=t_vuelo,
        divisiones=divisiones
    )

    return {
        "t": resultado_x["t"],
        "x": resultado_x["x"],
        "y": resultado_y["x"],
        "vx": resultado_x["v"],
        "vy": resultado_y["v"],
        "ax": resultado_x["a"],
        "ay": resultado_y["a"],
    }
