import fisica

# 1. Definición de parámetros para el MRU
# Un móvil que arranca en x = 5 metros y se mueve a 2 m/s constante durante 10 segundos
x0 = 5.0          # Posición inicial en metros (m)
v = 2.0           # Velocidad constante en metros por segundo (m/s)
tf = 10.0         # Tiempo final en segundos (s)
divisiones = 100  # Cantidad de divisiones de tiempo

print("=== Simulación de Movimiento Rectilíneo Uniforme (MRU) ===")
print("Parámetros iniciales:")
print(f"  - Posición inicial (x0): {x0} m")
print(f"  - Velocidad constante (v): {v} m/s")
print(f"  - Tiempo total de simulación (tf): {tf} s")
print(f"  - Divisiones: {divisiones}")
print("-" * 55)

resultado_mru = fisica.mru(
    posicion_inicial=x0,
    velocidad=v,
    tiempo_final=tf,
    divisiones=divisiones
)

print("Cálculos completados exitosamente.")
print(f"Muestras de tiempo (t): de {resultado_mru['t'][0]}s a {resultado_mru['t'][-1]}s")
print(f"Posición final calculada (x_final): {resultado_mru['x'][-1]:.2f} m")
print("-" * 55)

fisica.graficar_mru_mruv(resultado_mru)

print("Fin del ejemplo de MRU.")
