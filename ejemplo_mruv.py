from fisica import mruv
from fisica.graficos import graficar_mru_mruv

resultado = mruv(
    posicion_inicial=0,
    velocidad_inicial=0,
    aceleracion=2,
    tiempo_final=10,
    divisiones=100,
)

graficar_mru_mruv(resultado)