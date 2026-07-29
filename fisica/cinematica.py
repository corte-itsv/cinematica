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
    lista_tiempos=[]
    for i in range(divisiones):
        tiempo_dividido=tiempo_final/divisiones
        t=tiempo_dividido*(i+1)
        lista_tiempos.append(t)
    return lista_tiempos


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
        a=0
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
    if divisiones > 0 and tiempo_final > 0:
        lista_tiempos=calcular_lista_tiempo(tiempo_final, divisiones)
        diccionario_mruv={"t":[lista_tiempos], 
                         "x":[],
                         "v":[],
                         "a":[]}
        for i in range (divisiones):
            t=lista_tiempos[i]
            a=aceleracion
            diccionario_mruv["a"].append(a)
            v=calcular_velocidad_mruv(velocidad_inicial, aceleracion, t)
            diccionario_mruv["v"].append(v)
            x=calcular_posicion_mruv(posicion_inicial, velocidad_inicial, aceleracion, t )
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
    v0x=velocidad_inicial*math.cos(angulo)
    v0y=velocidad_inicial*math.sin(angulo)
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
    velocidad_inicial_y=obtener_componentes_velocidad()[1]
    t_vuelo=(velocidad_inicial_y+math.sqrt(pow(velocidad_inicial_y,2)+2*constantes.G*altura_inicial))/constantes.G
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
    velocidad_inicial_x, velocidad_inicial_y = obtener_componentes_velocidad(velocidad_inicial, angulo)

    tiempo_final_vuelo=calcular_tiempo_vuelo(velocidad_inicial_y, altura_inicial)
    lista_tiempos=calcular_lista_tiempo(tiempo_final_vuelo, divisiones)

    diccionario_tiro_oblicuo={
        't': [lista_tiempos],
        'x': [],
        'y': [],
        'vx': [],
        'vy': [],
        'ax': [],
        'ay': [],
    }
    tiempo_dividido=tiempo_final_vuelo/divisiones
    for i in range(divisiones):
        t=lista_tiempos[i]
        x=velocidad_inicial_x*t
        diccionario_tiro_oblicuo['x'].append(x)
        y=altura_inicial+velocidad_inicial_y*t-0.5*constantes.G*t*t
        diccionario_tiro_oblicuo["y"].append(y)
        vx=velocidad_inicial_x
        diccionario_tiro_oblicuo["vx"].append(vx)
        vy=velocidad_inicial_y-constantes.G*t
        diccionario_tiro_oblicuo["vy"].append(vy)
        ax=0
        diccionario_tiro_oblicuo["ax"].append(ax)
        ay=-1*constantes.G
        diccionario_tiro_oblicuo["ay"].append(ay)
    return diccionario_tiro_oblicuo