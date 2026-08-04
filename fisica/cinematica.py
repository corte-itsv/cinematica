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
import fisica.constantes  as constantes

def calcular_lista_tiempo(tiempo_final: float, divisiones: int) -> list[float]:
    """Genera una lista de tiempos desde 0 hasta tiempo_final dividida en N intervalos.

    Args:
        tiempo_final (float): Tiempo de finalización.
        divisiones (int): Cantidad de divisiones de tiempo.

    Returns:
        list[float]: Lista con los instantes de tiempo.
    """
    if divisiones <= 0:
        return [0.0]

    if tiempo_final == 0:
        return [0.0] * (divisiones + 1)

    paso = tiempo_final / divisiones
    return [paso * i for i in range(divisiones + 1)]


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
    if tiempo_final < 0 or divisiones <= 0:
        return None

    lista_tiempos = calcular_lista_tiempo(tiempo_final, divisiones)
    diccionario_mru = {
        "t": lista_tiempos,
        "x": [],
        "v": [],
        "a": [],
    }

    for t in lista_tiempos:
        v = velocidad
        diccionario_mru["v"].append(v)

        x = calcular_posicion_mru(posicion_inicial, v, t)
        diccionario_mru["x"].append(x)

        a = 0.0
        diccionario_mru["a"].append(a)

    return diccionario_mru
        
        


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
    if tiempo_final <= 0 or divisiones <= 0:
        return None

    lista_tiempos = calcular_lista_tiempo(tiempo_final, divisiones)
    diccionario_mruv = {
        "t": lista_tiempos,
        "x": [],
        "v": [],
        "a": [],
    }

    for t in lista_tiempos:
        a = -constantes.G
        diccionario_mruv["a"].append(a)

        v = calcular_velocidad_mruv(velocidad_inicial, aceleracion, t)
        diccionario_mruv["v"].append(v)

        x = calcular_posicion_mruv(posicion_inicial, velocidad_inicial, aceleracion, t)
        diccionario_mruv["x"].append(x)

    return diccionario_mruv
        




# --- FUNCIONES DE TIRO OBLICUO ---

def obtener_componentes_velocidad(velocidad_inicial: float, angulo: float) -> tuple:
    """Calcula las componentes horizontal (x) y vertical (y) de la velocidad inicial.

    Args:
        velocidad_inicial (float): Magnitud de la velocidad inicial.
        angulo (float): Ángulo respecto a la horizontal en grados.

    Returns:
        tuple: (v0x, v0y) componentes de la velocidad inicial.
    """
     #como la velocidad en x es constante (mru) se puede decir q siempre es igual a velocidad inicial
    angulo_rad = math.radians(angulo)
    v0x=velocidad_inicial*math.cos(angulo_rad)
    v0y=velocidad_inicial*math.sin(angulo_rad)
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
    
    discriminante = pow(velocidad_inicial_y, 2) + 2 * constantes.G * altura_inicial

    if discriminante < 0:
        return None

    t_vuelo = (velocidad_inicial_y + math.sqrt(discriminante)) / constantes.G
    if t_vuelo <= 0:
        return None

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
    if divisiones <= 0:
        return None

    velocidad_inicial_x, velocidad_inicial_y = obtener_componentes_velocidad(velocidad_inicial, angulo)

    tiempo_final_vuelo = calcular_tiempo_vuelo(velocidad_inicial_y, altura_inicial)
    if tiempo_final_vuelo is None:
        return None

    lista_tiempos = calcular_lista_tiempo(tiempo_final_vuelo, divisiones)

    diccionario_tiro_oblicuo = {
        't': lista_tiempos,
        'x': [],
        'y': [],
        'vx': [],
        'vy': [],
        'ax': [],
        'ay': [],
    }
    
    for t in lista_tiempos:
        x = velocidad_inicial_x * t
        diccionario_tiro_oblicuo['x'].append(x)
        
        y = altura_inicial + velocidad_inicial_y * t - 0.5 * constantes.G * t * t
        diccionario_tiro_oblicuo['y'].append(y)
        
        vx = velocidad_inicial_x
        diccionario_tiro_oblicuo['vx'].append(vx)
        
        vy = velocidad_inicial_y - constantes.G * t
        diccionario_tiro_oblicuo['vy'].append(vy)
        
        ax = 0.0
        diccionario_tiro_oblicuo['ax'].append(ax)
        
        ay = -1.0 * constantes.G
        diccionario_tiro_oblicuo['ay'].append(ay)
        
    return diccionario_tiro_oblicuo