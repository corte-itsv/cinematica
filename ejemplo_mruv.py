import fisica
from fisica.graficos import graficar_mru_mruv

resultado = fisica.cinematica.mruv(
    posicion_inicial=0.0,
    velocidad_inicial=6.0,
    aceleracion=2.0,
    tiempo_final=6.0,
    divisiones=40,
)
print(resultado)
graficar_mru_mruv(resultado)