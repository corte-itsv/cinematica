import fisica
from fisica.graficos import graficar_mru_mruv

resultado = fisica.cinematica.mru(
    posicion_inicial=3.0,
    velocidad=6.0,
    tiempo_final=16.5,
    divisiones=5,
)
print(resultado)
graficar_mru_mruv(resultado)