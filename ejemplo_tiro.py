from fisica import tiro_oblicuo, graficar_tiro_oblicuo

datos = tiro_oblicuo(
    velocidad_inicial=25,
    angulo=45,
    altura_inicial=0,
    divisiones=100,
)

graficar_tiro_oblicuo(datos)