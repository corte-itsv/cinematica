from fisica import tiro_oblicuo
from fisica.graficos import graficar_tiro_oblicuo
# Si prefieres la animación, puedes importar:
# from fisica.graficos import animar_tiro_oblicuo

resultado = tiro_oblicuo(
    velocidad_inicial=20,
    angulo=45,
    altura_inicial=0,
    divisiones=100,
)

graficar_tiro_oblicuo(resultado)

# O bien:
# animar_tiro_oblicuo(resultado)