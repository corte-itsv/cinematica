from fisica import mru, graficar_mru_mruv

datos = mru(
    posicion_inicial=0,
    velocidad=5,
    tiempo_final=10,
    divisiones=20,
)

graficar_mru_mruv(datos)