from fisica.cinematica import mruv


resultado = mruv(
    posicion_inicial=0,
    velocidad_inicial=10,
    aceleracion=2,
    tiempo_final=5,
    divisiones=5,
)

print(resultado)