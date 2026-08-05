from fisica import tiro_oblicuo, graficar_tiro_oblicuo

datos = tiro_oblicuo(
    velocidad_inicial=30,
    angulo=60,
    altura_inicial=0,
    divisiones=100,
)

graficar_tiro_oblicuo(datos)