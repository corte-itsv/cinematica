"""Ejemplo de simulación de Movimiento Rectilíneo Uniforme (MRU)."""

from fisica import mru, graficar_mru_mruv


def main():
    posicion_inicial = 0.0  
    velocidad = 15.0        
    tiempo_final = 10.0     
    divisiones = 100

    print("=== Simulación de Movimiento Rectilíneo Uniforme (MRU) ===")
    print(f"Posición inicial: {posicion_inicial} m")
    print(f"Velocidad constante: {velocidad} m/s")
    print(f"Tiempo de simulación: {tiempo_final} s\n")

    resultado = mru(
        posicion_inicial=posicion_inicial,
        velocidad=velocidad,
        tiempo_final=tiempo_final,
        divisiones=divisiones
    )

    print(f"Posición final alcanzada: {resultado['x'][-1]:.2f} m")

    graficar_mru_mruv(resultado)


if __name__ == "__main__":
    main()