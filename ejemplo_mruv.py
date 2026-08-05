import fisica
from fisica.graficos import graficar_mru_mruv

resultado = fisica.cinematica.mruv(
    posicion_inicial=0.0,
    velocidad_inicial=10.0,
    aceleracion=4.0,
    tiempo_final=4.0,
    divisiones=40,
)
print(resultado)
graficar_mru_mruv(resultado)