import fisica

# 1. Definición de parámetros para el Tiro Oblicuo
# Proyectil lanzado a 20 m/s con un ángulo de 45 grados desde una altura de 10 metros
v0 = 20.0          # Velocidad inicial en m/s
angulo = 50.0      # Ángulo de elevación en grados (°)
y0 = 0.0          # Altura inicial del lanzamiento en metros (m)
divisiones = 1000   # Cantidad de divisiones de tiempo

print("=== Simulación de Tiro Oblicuo (Lanzamiento Parabólico) ===")
print(f"Parámetros iniciales:")
print(f"  - Velocidad de disparo (v0): {v0} m/s")
print(f"  - Ángulo de elevación (theta): {angulo}°")
print(f"  - Altura de lanzamiento (y0): {y0} m")
print(f"  - Divisiones: {divisiones}")
print("-" * 65)

# 2. Ejecución del cálculo cinemático
# Calcula internamente el tiempo total de vuelo hasta impactar el suelo (y = 0)
resultado_tiro = fisica.tiro_oblicuo(
    velocidad_inicial=v0,
    angulo=angulo,
    altura_inicial=y0,
    divisiones=divisiones
)

# Tiempo de vuelo y distancia horizontal alcanzada
t_vuelo = resultado_tiro["t"][-1]
alcance_max = resultado_tiro["x"][-1]

print("Cálculos de trayectoria completados.")
print(f"  - Tiempo de vuelo calculado: {t_vuelo:.2f} s")
print(f"  - Alcance horizontal máximo: {alcance_max:.2f} m")
print("Abriendo animación en tiempo real. Disfrute del trayecto del proyectil...")
print("-" * 65)

# 3. Generación de la animación
fisica.animar_tiro_oblicuo(resultado_tiro)

print("Ejemplo de Tiro Oblicuo cerrado.")
