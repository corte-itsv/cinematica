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
from .constantes import G


def calcular_lista_tiempo(tiempo_final: float, divisiones: int) -> list[float]:
    """Genera una lista de tiempos desde 0 hasta tiempo_final dividida en N intervalos.

    Args:
        tiempo_final (float): Tiempo de finalización.
        divisiones (int): Cantidad de divisiones de tiempo.

    Returns:
        list[float]: Lista con los instantes de tiempo.
    """
    dt = tiempo_final / divisiones

    tiempos = []

    for i in range(divisiones + 1):
        tiempos.append(i * dt)

    return tiempos


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
    if tiempo_final <= 0:
        raise ValueError("El tiempo final debe ser mayor a 0.")

    if divisiones <= 0:
        raise ValueError("La cantidad de divisiones debe ser mayor a 0.")

    tiempos = calcular_lista_tiempo(tiempo_final, divisiones)

    posiciones = []
    velocidades = []
    aceleraciones = []

    for t in tiempos:

        posicion = calcular_posicion_mru(posicion_inicial, velocidad, t)

        posiciones.append(posicion)
        velocidades.append(velocidad)
        aceleraciones.append(0)

    return {
        "t": tiempos,
        "x": posiciones,
        "v": velocidades,
        "a": aceleraciones
    }




# --- FUNCIONES DE MRUV ---

def calcular_posicion_mruv(
    posicion_inicial: float,
    velocidad_inicial: float,
    aceleracion: float,
    t: float,
) -> float:
    """Calcula la posición para un MRUV en un tiempo t."""
    return (posicion_inicial + velocidad_inicial * t + 0.5 * aceleracion * t ** 2 )


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
    if tiempo_final <= 0:
        raise ValueError("El tiempo final debe ser mayor a 0.")

    if divisiones <= 0:
        raise ValueError("La cantidad de divisiones debe ser mayor a 0.")

    tiempos = calcular_lista_tiempo(tiempo_final, divisiones)

    posiciones = []
    velocidades = []
    aceleraciones = []

    for t in tiempos:

        posicion = calcular_posicion_mruv(
            posicion_inicial,
            velocidad_inicial,
            aceleracion,
            t
        )

        velocidad = calcular_velocidad_mruv(
            velocidad_inicial,
            aceleracion,
            t
        )

        posiciones.append(posicion)
        velocidades.append(velocidad)
        aceleraciones.append(aceleracion)

    return {
        "t": tiempos,
        "x": posiciones,
        "v": velocidades,
        "a": aceleraciones
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
    angulo = math.radians(angulo)

    v0x = velocidad_inicial * math.cos(angulo)
    v0y = velocidad_inicial * math.sin(angulo)

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
    a = -0.5 * G
    b = velocidad_inicial_y
    c = altura_inicial

    delta = b ** 2 - 4 * a * c

    if delta < 0:
        raise ValueError("El discriminante es negativo.")

    t1 = (-b + math.sqrt(delta)) / (2 * a)
    t2 = (-b - math.sqrt(delta)) / (2 * a)

    return max(t1, t2)
    

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
    if divisiones <= 0:
        raise ValueError("La cantidad de divisiones debe ser mayor a 0.")

    v0x, v0y = obtener_componentes_velocidad(
        velocidad_inicial,
        angulo
    )

    tiempo_final = calcular_tiempo_vuelo(
        v0y,
        altura_inicial
    )

    tiempos = calcular_lista_tiempo(
        tiempo_final,
        divisiones
    )

    posiciones_x = []
    posiciones_y = []
    velocidades_x = []
    velocidades_y = []
    aceleraciones_x = []
    aceleraciones_y = []

    for t in tiempos:

        x = calcular_posicion_mru(
            0,
            v0x,
            t
        )

        y = calcular_posicion_mruv(
            altura_inicial,
            v0y,
            -G,
            t
        )

        vy = calcular_velocidad_mruv(
            v0y,
            -G,
            t
        )

        posiciones_x.append(x)
        posiciones_y.append(y)

        velocidades_x.append(v0x)
        velocidades_y.append(vy)

        aceleraciones_x.append(0)
        aceleraciones_y.append(-G)

    return {
        "t": tiempos,
        "x": posiciones_x,
        "y": posiciones_y,
        "vx": velocidades_x,
        "vy": velocidades_y,
        "ax": aceleraciones_x,
        "ay": aceleraciones_y,
    }
