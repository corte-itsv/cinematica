from fisica import mruv, graficar_mru_mruv

datos = mruv(
    posicion_inicial=0,
    velocidad_inicial=40,
    aceleracion=-9.81,
    tiempo_final=10,
    divisiones=30,
)

graficar_mru_mruv(datos)