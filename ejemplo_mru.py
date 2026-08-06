import fisica
from fisica.graficos import graficar_mru_mruv

resultado = fisica.cinematica.mru(
    posicion_inicial=10.0,
    velocidad=7.0,
    tiempo_final=6.0,
    divisiones=10,
)
print(resultado)
graficar_mru_mruv(resultado)