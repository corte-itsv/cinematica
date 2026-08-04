from fisica import mruv, graficar_mru_mruv

datos = mruv(
    posicion_inicial=0,
    velocidad_inicial=20,
    aceleracion=-9.81,
    tiempo_final=5,
    divisiones=20,
)

graficar_mru_mruv(datos)