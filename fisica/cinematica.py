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
import constantes

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

    lista_tiempos = calcular_lista_tiempo(tiempo_final, divisiones)

    dicc_mru = {
        "t": [lista_tiempos],
        "x": [],
        "v": [],
        "a": []
    }

    for i in range(divisiones):

        t=lista_tiempos[i]

        v=velocidad
        dicc_mru["v"].append(v)

        x=calcular_posicion_mru(posicion_inicial, velocidad, t)
        dicc_mru["x"].append(x)
        
            



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

    if divisiones > 0 and tiempo_final > 0:
        lista_tiempos = calcular_lista_tiempo(tiempo_final, divisiones)
    
        dicc_mruv = {
                "t": [lista_tiempos],
                "x": [],
                "v": [],
                "a": []
            }

        for i in range(divisiones):
            t=lista_tiempos[i]

            a=aceleracion
            dicc_mruv["a"].append(a)

            v=calcular_velocidad_mruv(velocidad_inicial, aceleracion, t)
            dicc_mruv["v"].append(v)

            posicion = calcular_posicion_mruv(posicion_inicial, velocidad_inicial, aceleracion, t)
            dicc_mruv["x"].append(posicion)
        return dicc_mruv
    else:
        print("Divisiones o número de tiempo inválido.")

    


# --- FUNCIONES DE TIRO OBLICUO ---

def obtener_componentes_velocidad(velocidad_inicial: float, angulo: float) -> tuple:
    """Calcula las componentes horizontal (x) y vertical (y) de la velocidad inicial.

    Args:
        velocidad_inicial (float): Magnitud de la velocidad inicial.
        angulo (float): Ángulo respecto a la horizontal en grados.

    Returns:
        tuple: (v0x, v0y) componentes de la velocidad inicial.
    """

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

    gravedad = constantes.G
    velocidad_inicial_y = obtener_componentes_velocidad()[1]

    tiempo_vuelo = (velocidad_inicial_y + math.sqrt(math.pow(velocidad_inicial_y, 2) + 2 * gravedad * altura_inicial))/gravedad
    return tiempo_vuelo

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

    tiempo_vuelo = calcular_tiempo_vuelo(velocidad_inicial_y, altura_inicial)
    lista_tiempos_vuelo = calcular_lista_tiempo(tiempo_vuelo, divisiones)

    gravedad = constantes.G

    dicc_oblicuo = {
        't': [lista_tiempos_vuelo],
        'x': [],
        'y': [],
        'vx': [velocidad_inicial_x],
        'vy': [],
        'ax': [0],
        'ay': [-(gravedad)]
    }

    velocidad_inicial_x, velocidad_inicial_y = obtener_componentes_velocidad(velocidad_inicial, angulo)[1]

    for i in range(divisiones):
        tiempo_vuelo = lista_tiempos_vuelo[i+1]
        x = velocidad_inicial_x * tiempo_vuelo
        dicc_oblicuo['x'].append(x)

        y = calcular_posicion_mruv(altura_inicial, velocidad_inicial_y, -(gravedad), tiempo_vuelo)
        dicc_oblicuo['y'].append(y)

        vy = calcular_velocidad_mruv(velocidad_inicial_y, -(gravedad), tiempo_vuelo)
        dicc_oblicuo['vy'].append(vy)
        