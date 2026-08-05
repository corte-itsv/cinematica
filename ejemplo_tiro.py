"""Ejemplo de simulación de Tiro Oblicuo."""

from fisica import tiro_oblicuo, graficar_tiro_oblicuo, animar_tiro_oblicuo


def main():
    velocidad_inicial = 25.0  
    angulo = 45.0            
    altura_inicial = 2.0      
    divisiones = 120

    print("=== Simulación de Tiro Oblicuo ===")
    print(f"Velocidad inicial: {velocidad_inicial} m/s")
    print(f"Ángulo de disparo: {angulo}°")
    print(f"Altura inicial: {altura_inicial} m\n")

    resultado = tiro_oblicuo(
        velocidad_inicial=velocidad_inicial,
        angulo=angulo,
        altura_inicial=altura_inicial,
        divisiones=divisiones
    )

    tiempo_vuelo = resultado["t"][-1]
    alcance_maximo = resultado["x"][-1]
    altura_maxima = max(resultado["y"])

    print(f"Tiempo total de vuelo: {tiempo_vuelo:.2f} s")
    print(f"Alcance horizontal máximo: {alcance_maximo:.2f} m")
    print(f"Altura máxima alcanzada: {altura_maxima:.2f} m")

    graficar_tiro_oblicuo(resultado)

if __name__ == "__main__":
    main()