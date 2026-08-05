"""Ejemplo de simulación de Movimiento Rectilíneo Uniformemente Variado (MRUV)."""

from fisica import mruv, graficar_mru_mruv


def main():
    posicion_inicial = 0.0   
    velocidad_inicial = 5.0   
    aceleracion = 2.5        
    tiempo_final = 8.0        
    divisiones = 100

    print("=== Simulación de Movimiento Rectilíneo Uniformemente Variado (MRUV) ===")
    print(f"Posición inicial: {posicion_inicial} m")
    print(f"Velocidad inicial: {velocidad_inicial} m/s")
    print(f"Aceleración: {aceleracion} m/s²")
    print(f"Tiempo de simulación: {tiempo_final} s\n")

    resultado = mruv(
        posicion_inicial=posicion_inicial,
        velocidad_inicial=velocidad_inicial,
        aceleracion=aceleracion,
        tiempo_final=tiempo_final,
        divisiones=divisiones
    )

    print(f"Posición final alcanzada: {resultado['x'][-1]:.2f} m")
    print(f"Velocidad final alcanzada: {resultado['v'][-1]:.2f} m/s")

    graficar_mru_mruv(resultado)


if __name__ == "__main__":
    main()