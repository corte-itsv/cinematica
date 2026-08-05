from fisica import mru
from fisica.graficos import graficar_mru_mruv

resultado = mru(
    posicion_inicial=0,
    velocidad=5,
    tiempo_final=10,
    divisiones=100,
)

graficar_mru_mruv(resultado)