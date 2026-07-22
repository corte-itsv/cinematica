"""Funciones de visualización gráfica para los movimientos físicos.

Este módulo provee las herramientas necesarias para graficar los resultados
de las simulaciones de MRU, MRUV y Tiro Oblicuo utilizando matplotlib,
empleando listas estándar de Python para evitar dependencias de numpy.
"""

import math
import time
from typing import Dict, Any, List
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.patches import Patch
from matplotlib.animation import FuncAnimation


def graficar_posicion(resultado: Dict[str, List[float]], ax: Any = None) -> None:
    """Grafica la posición en función del tiempo.

    Soporta tanto un gráfico independiente como dibujar en un eje (subplot) existente.

    Args:
        resultado (Dict[str, List[float]]): Diccionario con los datos simulados.
            Debe contener 't' y 'x'. Opcionalmente 'y' para tiro oblicuo.
        ax (Any, opcional): Eje de matplotlib sobre el cual graficar. Si es None,
            se crea una nueva figura y se muestra el gráfico.

    Raises:
        TypeError: Si resultado no es un diccionario.
        ValueError: Si faltan las claves necesarias ('t', 'x').
    """
    if not isinstance(resultado, dict):
        raise TypeError("El resultado debe ser un diccionario.")
    if "t" not in resultado or "x" not in resultado:
        raise ValueError("El diccionario de resultados debe contener al menos las claves 't' y 'x'.")

    mostrar = False
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 5))
        mostrar = True

    if "y" in resultado:
        # Movimiento bidimensional
        ax.plot(resultado["t"], resultado["x"], label="Posición X (Horizontal)", color="blue", linewidth=2)
        ax.plot(resultado["t"], resultado["y"], label="Posición Y (Vertical)", color="green", linewidth=2)
        ax.set_ylabel("Posición (m)")
        ax.set_title("Posición vs Tiempo (Tiro Oblicuo)")
        ax.legend()
    else:
        # Movimiento unidimensional
        ax.plot(resultado["t"], resultado["x"], label="Posición x(t)", color="blue", linewidth=2)
        ax.set_ylabel("Posición (m)")
        ax.set_title("Posición vs Tiempo")
        ax.legend()

    ax.set_xlabel("Tiempo (s)")
    ax.grid(True, linestyle="--", alpha=0.7)

    if mostrar:
        plt.show()


def graficar_velocidad(resultado: Dict[str, List[float]], ax: Any = None) -> None:
    """Grafica la velocidad en función del tiempo.

    Soporta tanto un gráfico independiente como dibujar en un eje (subplot) existente.

    Args:
        resultado (Dict[str, List[float]]): Diccionario con los datos simulados.
            Debe contener 't' y ('v' o 'vx').
        ax (Any, opcional): Eje de matplotlib sobre el cual graficar. Si es None,
            se crea una nueva figura y se muestra el gráfico.

    Raises:
        TypeError: Si resultado no es un diccionario.
        ValueError: Si faltan las claves necesarias de velocidad.
    """
    if not isinstance(resultado, dict):
        raise TypeError("El resultado debe ser un diccionario.")
    if "t" not in resultado:
        raise ValueError("El diccionario de resultados debe contener la clave 't'.")

    mostrar = False
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 5))
        mostrar = True

    if "vy" in resultado and "vx" in resultado:
        # Movimiento bidimensional
        ax.plot(resultado["t"], resultado["vx"], label="Velocidad Vx (Horizontal)", color="blue", linewidth=2)
        ax.plot(resultado["t"], resultado["vy"], label="Velocidad Vy (Vertical)", color="green", linewidth=2)
        
        # Calcular el módulo del vector velocidad para cada muestra
        v_modulo = [math.sqrt(vx_val**2 + vy_val**2) for vx_val, vy_val in zip(resultado["vx"], resultado["vy"])]
        ax.plot(resultado["t"], v_modulo, label="Módulo de Velocidad |V|", color="red", linestyle="--", linewidth=1.5)
        
        ax.set_ylabel("Velocidad (m/s)")
        ax.set_title("Velocidad vs Tiempo (Tiro Oblicuo)")
        ax.legend()
    elif "v" in resultado:
        # Movimiento unidimensional
        ax.plot(resultado["t"], resultado["v"], label="Velocidad v(t)", color="green", linewidth=2)
        ax.set_ylabel("Velocidad (m/s)")
        ax.set_title("Velocidad vs Tiempo")
        ax.legend()
    else:
        raise ValueError("El diccionario de resultados debe contener las claves de velocidad ('v' o 'vx'/'vy').")

    ax.set_xlabel("Tiempo (s)")
    ax.grid(True, linestyle="--", alpha=0.7)

    if mostrar:
        plt.show()


def graficar_aceleracion(resultado: Dict[str, List[float]], ax: Any = None) -> None:
    """Grafica la aceleración en función del tiempo.

    Soporta tanto un gráfico independiente como dibujar en un eje (subplot) existente.

    Args:
        resultado (Dict[str, List[float]]): Diccionario con los datos simulados.
            Debe contener 't' y ('a' o 'ax'/'ay').
        ax (Any, opcional): Eje de matplotlib sobre el cual graficar. Si es None,
            se crea una nueva figura y se muestra el gráfico.

    Raises:
        TypeError: Si resultado no es un diccionario.
        ValueError: Si faltan las claves necesarias de aceleración.
    """
    if not isinstance(resultado, dict):
        raise TypeError("El resultado debe ser un diccionario.")
    if "t" not in resultado:
        raise ValueError("El diccionario de resultados debe contener la clave 't'.")

    mostrar = False
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 5))
        mostrar = True

    if "ay" in resultado and "ax" in resultado:
        # Movimiento bidimensional
        ax.plot(resultado["t"], resultado["ax"], label="Aceleración Ax (Horizontal)", color="blue", linewidth=2)
        ax.plot(resultado["t"], resultado["ay"], label="Aceleración Ay (Vertical)", color="green", linewidth=2)
        ax.set_ylabel("Aceleración (m/s²)")
        ax.set_title("Aceleración vs Tiempo (Tiro Oblicuo)")
        ax.legend()
    elif "a" in resultado:
        # Movimiento unidimensional
        ax.plot(resultado["t"], resultado["a"], label="Aceleración a(t)", color="purple", linewidth=2)
        ax.set_ylabel("Aceleración (m/s²)")
        ax.set_title("Aceleración vs Tiempo")
        ax.legend()
    else:
        raise ValueError("El diccionario de resultados debe contener las claves de aceleración ('a' o 'ax'/'ay').")

    ax.set_xlabel("Tiempo (s)")
    ax.grid(True, linestyle="--", alpha=0.7)

    if mostrar:
        plt.show()


def graficar_mru_mruv(resultado: Dict[str, List[float]]) -> None:
    """Muestra los gráficos de posición, velocidad y aceleración en una misma ventana.

    Genera una disposición vertical de 3 subplots para comparar fácilmente
    las variables del movimiento en el tiempo.

    Args:
        resultado (Dict[str, List[float]]): Diccionario con los datos simulados.
    """
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10), sharex=True)
    
    graficar_posicion(resultado, ax=ax1)
    graficar_velocidad(resultado, ax=ax2)
    graficar_aceleracion(resultado, ax=ax3)

    plt.tight_layout()
    plt.show()


def graficar_tiro_oblicuo(resultado: Dict[str, List[float]]) -> None:
    """Genera una ventana interactiva y optimizada de la trayectoria del Tiro Oblicuo.

    Permite desplazar el tiempo usando un Slider y visualizar de manera
    proporcionada los vectores de velocidad (verde) y aceleración (púrpura),
    optimizando el área útil del gráfico con respecto al tamaño de la ventana.

    Args:
        resultado (Dict[str, List[float]]): Diccionario con los datos simulados.
            Debe contener las claves 't', 'x', 'y', 'vx', 'vy', 'ax', 'ay'.
    """
    if not isinstance(resultado, dict):
        raise TypeError("El resultado debe ser un diccionario.")
    
    claves_requeridas = ["t", "x", "y", "vx", "vy", "ax", "ay"]
    for clave in claves_requeridas:
        if clave not in resultado:
            raise ValueError(f"El diccionario de resultados debe contener la clave '{clave}'.")

    # Extraer variables
    t = resultado["t"]
    x = resultado["x"]
    y = resultado["y"]
    vx = resultado["vx"]
    vy = resultado["vy"]
    ax_val = resultado["ax"]
    ay_val = resultado["ay"]

    # Crear la figura y el eje principal, optimizando márgenes para agrandar el gráfico
    fig, ax = plt.subplots(figsize=(10, 5.5))
    plt.subplots_adjust(left=0.07, right=0.95, top=0.92, bottom=0.22)

    # Graficar trayectoria fija
    ax.plot(x, y, label="Trayectoria completa", color="blue", linestyle="--", linewidth=1.5)

    # Identificar puntos clave (altura máxima usando max() estándar)
    y_max_val = max(y)
    idx_ymax = y.index(y_max_val)
    x_max = x[idx_ymax]

    # Graficar puntos hitos
    ax.plot(x[0], y[0], "go", markersize=6)      # Punto Inicial (Verde)
    ax.plot(x_max, y_max_val, "y^", markersize=8) # Altura Máxima (Triángulo Amarillo)
    ax.plot(x[-1], y[-1], "ks", markersize=6)    # Punto Final (Cuadrado Negro)

    # Punto dinámico indicador de posición actual (Rojo)
    punto_actual, = ax.plot(x[0], y[0], "ro", markersize=8)

    # Escalamiento visual óptimo y acotado de los vectores (para que no queden muy grandes)
    # Se define que la longitud máxima del vector de velocidad sea del 5% del span de X.
    x_span = max(x) - min(x)
    x_span_limit = x_span if x_span > 0 else 1.0
    
    v0_magnitud = math.sqrt(vx[0]**2 + vy[0]**2)
    v_scale_factor = (0.05 * x_span_limit) / v0_magnitud if v0_magnitud > 0 else 1.0
    
    # Se define que la longitud del vector de aceleración (gravedad) sea del 4% del span de X.
    g_magnitud = abs(ay_val[0])
    a_scale_factor = (0.04 * x_span_limit) / g_magnitud if g_magnitud > 0 else 1.0

    # Crear vectores iniciales (quiver) más delgados (width=0.003) para mayor elegancia
    v_quiver = ax.quiver(
        x[0], y[0], vx[0] * v_scale_factor, vy[0] * v_scale_factor,
        angles="xy", scale_units="xy", scale=1, color="green", width=0.003
    )
    a_quiver = ax.quiver(
        x[0], y[0], ax_val[0] * a_scale_factor, ay_val[0] * a_scale_factor,
        angles="xy", scale_units="xy", scale=1, color="purple", width=0.003
    )

    # Ajustar límites estrictos para evitar márgenes vacíos gigantes al usar set_aspect("equal")
    x_max_val = max(x)
    x_max_limit = x_max_val if x_max_val > 0 else 1.0
    y_max_limit = y_max_val if y_max_val > 0 else 1.0
    
    ax.set_xlim(-0.05 * x_max_limit, 1.05 * x_max_limit)
    ax.set_ylim(-0.08 * y_max_limit, 1.12 * y_max_limit)
    ax.set_aspect("equal")

    # Etiquetas y título
    ax.set_xlabel("Distancia horizontal (m)")
    ax.set_ylabel("Altura (m)")
    ax.set_title("Simulación Interactiva de Tiro Oblicuo")
    ax.grid(True, linestyle=":", alpha=0.6)

    # Crear leyenda estática
    legend_elements = [
        plt.Line2D([0], [0], color="blue", linestyle="--", label="Trayectoria"),
        plt.Line2D([0], [0], color="green", marker="o", linestyle="", label="Punto Inicial"),
        plt.Line2D([0], [0], color="yellow", marker="^", markeredgecolor="orange", linestyle="", label="Altura Máxima"),
        plt.Line2D([0], [0], color="black", marker="s", linestyle="", label="Punto Final"),
        plt.Line2D([0], [0], color="red", marker="o", linestyle="", label="Posición Actual"),
        Patch(facecolor="green", edgecolor="green", label="Vector Velocidad (Escalado)"),
        Patch(facecolor="purple", edgecolor="purple", label="Vector Aceleración (Escalado)")
    ]
    ax.legend(handles=legend_elements, loc="upper right")

    # Caja de texto informativa
    texto_inicial = (
        f"Tiempo: {t[0]:.2f} s\n"
        f"Posición: ({x[0]:.2f}, {y[0]:.2f}) m\n"
        f"Velocidad: ({vx[0]:.2f}, {vy[0]:.2f}) m/s\n"
        f"  [Módulo: {v0_magnitud:.2f} m/s]\n"
        f"Aceleración: ({ax_val[0]:.2f}, {ay_val[0]:.2f}) m/s²"
    )
    info_box = ax.text(
        0.05, 0.95, texto_inicial,
        transform=ax.transAxes,
        fontsize=9,
        verticalalignment="top",
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.85, edgecolor="gray")
    )

    # Control deslizante (Slider) de tiempo colocado más abajo
    ax_slider = plt.axes([0.15, 0.06, 0.7, 0.03])
    slider_tiempo = Slider(
        ax=ax_slider,
        label="Tiempo (s) ",
        valmin=float(t[0]),
        valmax=float(t[-1]),
        valinit=float(t[0]),
        valfmt="%.2f s",
        color="royalblue"
    )

    # Función de actualización del Slider
    def update(val: float) -> None:
        t_actual = slider_tiempo.val

        # Búsqueda manual del índice con el tiempo más cercano (evitando lambda y numpy)
        idx = 0
        min_diff = abs(t[0] - t_actual)
        for i in range(1, len(t)):
            diff = abs(t[i] - t_actual)
            if diff < min_diff:
                min_diff = diff
                idx = i

        x_curr = x[idx]
        y_curr = y[idx]
        vx_curr = vx[idx]
        vy_curr = vy[idx]
        ax_curr = ax_val[idx]
        ay_curr = ay_val[idx]
        v_mag = math.sqrt(vx_curr**2 + vy_curr**2)

        # Actualizar punto de posición actual
        punto_actual.set_data([x_curr], [y_curr])

        # Actualizar vectores (quiver)
        nonlocal v_quiver, a_quiver
        v_quiver.remove()
        a_quiver.remove()
        
        v_quiver = ax.quiver(
            x_curr, y_curr, vx_curr * v_scale_factor, vy_curr * v_scale_factor,
            angles="xy", scale_units="xy", scale=1, color="green", width=0.003
        )
        a_quiver = ax.quiver(
            x_curr, y_curr, ax_curr * a_scale_factor, ay_curr * a_scale_factor,
            angles="xy", scale_units="xy", scale=1, color="purple", width=0.003
        )

        # Actualizar caja de texto
        texto_actualizado = (
            f"Tiempo: {t[idx]:.2f} s\n"
            f"Posición: ({x_curr:.2f}, {y_curr:.2f}) m\n"
            f"Velocidad: ({vx_curr:.2f}, {vy_curr:.2f}) m/s\n"
            f"  [Módulo: {v_mag:.2f} m/s]\n"
            f"Aceleración: ({ax_curr:.2f}, {ay_curr:.2f}) m/s²"
        )
        info_box.set_text(texto_actualizado)

        # Redibujar
        fig.canvas.draw_idle()

    slider_tiempo.on_changed(update)
    plt.show()


def animar_tiro_oblicuo(resultado: Dict[str, List[float]], intervalo_ms: float = None) -> None:
    """Genera una animación interactiva y fluida de la trayectoria del Tiro Oblicuo.

    Muestra el proyectil en movimiento a lo largo del tiempo, junto a sus vectores
    de velocidad (verde) y aceleración (púrpura).

    Args:
        resultado (Dict[str, List[float]]): Diccionario con los datos simulados.
            Debe contener las claves 't', 'x', 'y', 'vx', 'vy', 'ax', 'ay'.
        intervalo_ms (float, opcional): Tiempo entre cuadros en milisegundos.
            Si es None, se calcula automáticamente para correr en tiempo real.
    """
    if not isinstance(resultado, dict):
        raise TypeError("El resultado debe ser un diccionario.")
    
    claves_requeridas = ["t", "x", "y", "vx", "vy", "ax", "ay"]
    for clave in claves_requeridas:
        if clave not in resultado:
            raise ValueError(f"El diccionario de resultados debe contener la clave '{clave}'.")

    # Extraer variables
    t = resultado["t"]
    x = resultado["x"]
    y = resultado["y"]
    vx = resultado["vx"]
    vy = resultado["vy"]
    ax_val = resultado["ax"]
    ay_val = resultado["ay"]

    # Si no se define intervalo_ms, calcular el paso real de tiempo de la física (en milisegundos)
    # para que la animación transcurra exactamente en tiempo real.
    if intervalo_ms is None:
        t_vuelo = t[-1] - t[0]
        cantidad_intervalos = len(t) - 1
        if cantidad_intervalos > 0:
            intervalo_ms = (t_vuelo / cantidad_intervalos) * 1000
        else:
            intervalo_ms = 40.0

    # Crear la figura y el eje principal, optimizando márgenes
    fig, ax = plt.subplots(figsize=(10, 5.5))
    plt.subplots_adjust(left=0.07, right=0.95, top=0.92, bottom=0.12)

    # Graficar trayectoria fija
    ax.plot(x, y, label="Trayectoria completa", color="blue", linestyle="--", linewidth=1.5)

    # Identificar puntos clave
    y_max_val = max(y)
    idx_ymax = y.index(y_max_val)
    x_max = x[idx_ymax]

    # Graficar puntos hitos
    ax.plot(x[0], y[0], "go", markersize=6)      # Punto Inicial (Verde)
    ax.plot(x_max, y_max_val, "y^", markersize=8) # Altura Máxima (Triángulo Amarillo)
    ax.plot(x[-1], y[-1], "ks", markersize=6)    # Punto Final (Cuadrado Negro)

    # Punto dinámico indicador de posición actual (Rojo)
    punto_actual, = ax.plot(x[0], y[0], "ro", markersize=8)

    # Escalamiento visual de los vectores
    x_span = max(x) - min(x)
    x_span_limit = x_span if x_span > 0 else 1.0
    
    v0_magnitud = math.sqrt(vx[0]**2 + vy[0]**2)
    v_scale_factor = (0.05 * x_span_limit) / v0_magnitud if v0_magnitud > 0 else 1.0
    
    g_magnitud = abs(ay_val[0])
    a_scale_factor = (0.04 * x_span_limit) / g_magnitud if g_magnitud > 0 else 1.0

    # Crear vectores iniciales (quiver)
    v_quiver = ax.quiver(
        x[0], y[0], vx[0] * v_scale_factor, vy[0] * v_scale_factor,
        angles="xy", scale_units="xy", scale=1, color="green", width=0.003
    )
    a_quiver = ax.quiver(
        x[0], y[0], ax_val[0] * a_scale_factor, ay_val[0] * a_scale_factor,
        angles="xy", scale_units="xy", scale=1, color="purple", width=0.003
    )

    # Ajustar límites
    x_max_val = max(x)
    x_max_limit = x_max_val if x_max_val > 0 else 1.0
    y_max_limit = y_max_val if y_max_val > 0 else 1.0
    
    ax.set_xlim(-0.05 * x_max_limit, 1.05 * x_max_limit)
    ax.set_ylim(-0.08 * y_max_limit, 1.12 * y_max_limit)
    ax.set_aspect("equal")

    # Etiquetas y título
    ax.set_xlabel("Distancia horizontal (m)")
    ax.set_ylabel("Altura (m)")
    ax.set_title("Animación en Tiempo Real de Tiro Oblicuo")
    ax.grid(True, linestyle=":", alpha=0.6)

    # Crear leyenda estática
    legend_elements = [
        plt.Line2D([0], [0], color="blue", linestyle="--", label="Trayectoria"),
        plt.Line2D([0], [0], color="green", marker="o", linestyle="", label="Punto Inicial"),
        plt.Line2D([0], [0], color="yellow", marker="^", markeredgecolor="orange", linestyle="", label="Altura Máxima"),
        plt.Line2D([0], [0], color="black", marker="s", linestyle="", label="Punto Final"),
        plt.Line2D([0], [0], color="red", marker="o", linestyle="", label="Posición Actual"),
        Patch(facecolor="green", edgecolor="green", label="Vector Velocidad (Escalado)"),
        Patch(facecolor="purple", edgecolor="purple", label="Vector Aceleración (Escalado)")
    ]
    ax.legend(handles=legend_elements, loc="upper right")

    # Caja de texto informativa
    texto_inicial = (
        f"Tiempo: {t[0]:.2f} s\n"
        f"Posición: ({x[0]:.2f}, {y[0]:.2f}) m\n"
        f"Velocidad: ({vx[0]:.2f}, {vy[0]:.2f}) m/s\n"
        f"  [Módulo: {v0_magnitud:.2f} m/s]\n"
        f"Aceleración: ({ax_val[0]:.2f}, {ay_val[0]:.2f}) m/s²"
    )
    info_box = ax.text(
        0.05, 0.95, texto_inicial,
        transform=ax.transAxes,
        fontsize=9,
        verticalalignment="top",
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.85, edgecolor="gray")
    )

    t_inicio = time.time()
    t_vuelo = t[-1] - t[0]

    # Función de inicialización para blitting
    def init() -> tuple:
        punto_actual.set_data([x[0]], [y[0]])
        v_quiver.set_offsets([[x[0], y[0]]])
        v_quiver.set_UVC(vx[0] * v_scale_factor, vy[0] * v_scale_factor)
        a_quiver.set_offsets([[x[0], y[0]]])
        a_quiver.set_UVC(ax_val[0] * a_scale_factor, ay_val[0] * a_scale_factor)
        info_box.set_text(texto_inicial)
        return punto_actual, v_quiver, a_quiver, info_box

    # Función de actualización para la animación basada en el tiempo real del sistema
    def update(frame: int) -> tuple:
        # Calcular el tiempo transcurrido real
        t_transcurrido = (time.time() - t_inicio) % t_vuelo
        
        # Búsqueda del índice de tiempo más cercano
        idx = 0
        min_diff = abs(t[0] - t_transcurrido)
        for i in range(1, len(t)):
            diff = abs(t[i] - t_transcurrido)
            if diff < min_diff:
                min_diff = diff
                idx = i
            else:
                break
                
        x_curr = x[idx]
        y_curr = y[idx]
        vx_curr = vx[idx]
        vy_curr = vy[idx]
        ax_curr = ax_val[idx]
        ay_curr = ay_val[idx]
        v_mag = math.sqrt(vx_curr**2 + vy_curr**2)

        # Actualizar punto de posición
        punto_actual.set_data([x_curr], [y_curr])

        # Actualizar quivers modificando sus propiedades internas (evita recreación lenta)
        v_quiver.set_offsets([[x_curr, y_curr]])
        v_quiver.set_UVC(vx_curr * v_scale_factor, vy_curr * v_scale_factor)
        
        a_quiver.set_offsets([[x_curr, y_curr]])
        a_quiver.set_UVC(ax_curr * a_scale_factor, ay_curr * a_scale_factor)

        # Actualizar caja de texto
        texto_actualizado = (
            f"Tiempo: {t[idx]:.2f} s\n"
            f"Posición: ({x_curr:.2f}, {y_curr:.2f}) m\n"
            f"Velocidad: ({vx_curr:.2f}, {vy_curr:.2f}) m/s\n"
            f"  [Módulo: {v_mag:.2f} m/s]\n"
            f"Aceleración: ({ax_curr:.2f}, {ay_curr:.2f}) m/s²"
        )
        info_box.set_text(texto_actualizado)
        return punto_actual, v_quiver, a_quiver, info_box

    # Crear y conservar la animación para evitar que sea eliminada por el recolector de basura.
    # Usamos blit=True para redibujar únicamente los elementos móviles y lograr máxima fluidez.
    actualizacion_ms = 15 if intervalo_ms is None else intervalo_ms
    ani = FuncAnimation(
        fig,
        update,
        init_func=init,
        frames=None,
        interval=actualizacion_ms,
        blit=True,
        repeat=True
    )
    
    # Asignamos la referencia de la animación a la figura para que persista
    fig.ani = ani
    
    plt.show()
