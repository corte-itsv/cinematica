import math

G = 9.81

def calcular_lista_tiempo(tiempo_final: float, divisiones: int) -> list[float]:
    """Genera una lista de tiempos desde 0 hasta tiempo_final dividida en N intervalos."""
    if tiempo_final <= 0 or divisiones <= 0:
        raise ValueError("El tiempo final debe ser positivo y las divisiones mayores a cero.")
    paso = tiempo_final / divisiones
    return [i * paso for i in range(divisiones + 1)]


def calcular_posicion_mru(posicion_inicial: float, velocidad: float, t: float) -> float:
    """Calcula la posición para un MRU en un tiempo t."""
    return posicion_inicial + velocidad * t

def mru(posicion_inicial: float, velocidad: float, tiempo_final: float, divisiones: int) -> dict[str, list[float]]:
    """Calcula la posición, velocidad y aceleración para un MRU."""
    if tiempo_final <= 0 or divisiones <= 0:
        raise ValueError("El tiempo final debe ser positivo y las divisiones mayores a cero.")
    
    t_lista = calcular_lista_tiempo(tiempo_final, divisiones)
    x_lista = [calcular_posicion_mru(posicion_inicial, velocidad, t) for t in t_lista]
    v_lista = [velocidad for _ in t_lista]
    a_lista = [0.0 for _ in t_lista]
    
    return {"t": t_lista, "x": x_lista, "v": v_lista, "a": a_lista}


def calcular_posicion_mruv(posicion_inicial: float, velocidad_inicial: float, aceleracion: float, t: float) -> float:
    """Calcula la posición para un MRUV en un tiempo t."""
    return posicion_inicial + velocidad_inicial * t + 0.5 * aceleracion * (t ** 2)

def calcular_velocidad_mruv(velocidad_inicial: float, aceleracion: float, t: float) -> float:
    """Calcula la velocidad para un MRUV en un tiempo t."""
    return velocidad_inicial + aceleracion * t

def mruv(posicion_inicial: float, velocidad_inicial: float, aceleracion: float, tiempo_final: float, divisiones: int) -> dict[str, list[float]]:
    """Calcula la posición, velocidad y aceleración para un MRUV."""
    if tiempo_final <= 0 or divisiones <= 0:
        raise ValueError("El tiempo final debe ser positivo y las divisiones mayores a cero.")
    
    t_lista = calcular_lista_tiempo(tiempo_final, divisiones)
    x_lista = [calcular_posicion_mruv(posicion_inicial, velocidad_inicial, aceleracion, t) for t in t_lista]
    v_lista = [calcular_velocidad_mruv(velocidad_inicial, aceleracion, t) for t in t_lista]
    a_lista = [aceleracion for _ in t_lista]
    
    return {"t": t_lista, "x": x_lista, "v": v_lista, "a": a_lista}


def obtener_componentes_velocidad(velocidad_inicial: float, angulo: float) -> tuple[float, float]:
    """Calcula las componentes horizontal (x) y vertical (y) de la velocidad inicial."""
    angulo_rad = math.radians(angulo)
    v0x = velocidad_inicial * math.cos(angulo_rad)
    v0y = velocidad_inicial * math.sin(angulo_rad)
    return v0x, v0y

def calcular_tiempo_vuelo(velocidad_inicial_y: float, altura_inicial: float) -> float:
    """Calcula el tiempo de vuelo de un tiro oblicuo hasta que vuelve a y = 0."""
    a_coef = 0.5 * G
    b_coef = -velocidad_inicial_y
    c_coef = -altura_inicial
    
    discriminante = (b_coef ** 2) - (4 * a_coef * c_coef)
    if discriminante < 0:
        raise ValueError("El discriminante es negativo; no hay raíces reales (no llega al suelo de la misma forma analizada).")
    
    t1 = (-b_coef - math.sqrt(discriminante)) / (2 * a_coef)
    t2 = (-b_coef + math.sqrt(discriminante)) / (2 * a_coef)
    
    tiempo_vuelo = max(t1, t2)
    if tiempo_vuelo <= 0:
        raise ValueError("El tiempo de vuelo calculado es menor o igual a cero.")
        
    return tiempo_vuelo

def tiro_oblicuo(velocidad_inicial: float, angulo: float, altura_inicial: float, divisiones: int) -> dict[str, list[float]]:
    """Calcula las variables de la trayectoria de un tiro oblicuo."""
    if divisiones <= 0:
        raise ValueError("La cantidad de divisiones debe ser mayor a cero.")
        
    v0x, v0y = obtener_componentes_velocidad(velocidad_inicial, angulo)
    tiempo_vuelo = calcular_tiempo_vuelo(v0y, altura_inicial)
    
    t_lista = calcular_lista_tiempo(tiempo_vuelo, divisiones)
    
    x_lista = [v0x * t for t in t_lista]
    y_lista = [altura_inicial + v0y * t - 0.5 * G * (t ** 2) for t in t_lista]
    vx_lista = [v0x for _ in t_lista]
    vy_lista = [v0y - G * t for t in t_lista]
    ax_lista = [0.0 for _ in t_lista]
    ay_lista = [-G for _ in t_lista]
    
    return {
        "t": t_lista,
        "x": x_lista,
        "y": y_lista,
        "vx": vx_lista,
        "vy": vy_lista,
        "ax": ax_lista,
        "ay": ay_lista
    }