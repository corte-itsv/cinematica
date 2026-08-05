import fisica
from fisica.graficos import graficar_mru_mruv

resultado = fisica.cinematica.mruv(
    posicion_inicial=2.0,
    velocidad_inicial=5.0,
    aceleracion=6.0,
    tiempo_final=7.0,
    divisiones=35,
)
print(resultado)
graficar_mru_mruv(resultado)