import fisica
from fisica.graficos import graficar_mru_mruv

resultado = fisica.cinematica.mru(
    posicion_inicial=5.0,
    velocidad=5.0,
    tiempo_final=5.0,
    divisiones=5,
)
print(resultado)
graficar_mru_mruv(resultado)