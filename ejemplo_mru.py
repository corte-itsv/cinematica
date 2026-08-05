from fisica import mru, graficar_mru_mruv

datos = mru(
    posicion_inicial=0,
    velocidad=8,
    tiempo_final=5,
    divisiones=30,
)

graficar_mru_mruv(datos)