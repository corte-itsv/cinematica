import fisica

# 1. Definición de parámetros para el MRUV
# Un móvil que arranca en x = 0 metros, con velocidad inicial de 2 m/s y acelera a 0.5 m/s^2 durante 15 segundos
x0 = 0.0          # Posición inicial en metros (m)
v0 = 2.0          # Velocidad inicial en metros por segundo (m/s)
a = 0.5           # Aceleración constante en metros por segundo al cuadrado (m/s^2)
tf = 15.0         # Tiempo final en segundos (s)
divisiones = 150  # Cantidad de divisiones de tiempo

print("=== Simulación de Movimiento Rectilíneo Uniformemente Variado (MRUV) ===")
print("Parámetros iniciales:")
print(f"  - Posición inicial (x0): {x0} m")
print(f"  - Velocidad inicial (v0): {v0} m/s")
print(f"  - Aceleración (a): {a} m/s²")
print(f"  - Tiempo total de simulación (tf): {tf} s")
print(f"  - Divisiones: {divisiones}")
print("-" * 65)

resultado_mruv = fisica.mruv(
    posicion_inicial=x0,
    velocidad_inicial=v0,
    aceleracion=a,
    tiempo_final=tf,
    divisiones=divisiones
)

print("Cálculos completados exitosamente.")
print(f"Muestras de tiempo (t): de {resultado_mruv['t'][0]}s a {resultado_mruv['t'][-1]}s")
print(f"Posición final calculada (x_final): {resultado_mruv['x'][-1]:.2f} m")
print(f"Velocidad final calculada (v_final): {resultado_mruv['v'][-1]:.2f} m/s")
print("Mostrando los tres gráficos unificados en la misma ventana...")
print("-" * 65)

fisica.graficar_mru_mruv(resultado_mruv)

print("Fin del ejemplo de MRUV.")
