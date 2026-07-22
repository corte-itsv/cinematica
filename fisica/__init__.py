"""Biblioteca física para cinemática de nivel secundario.

Este paquete permite realizar cálculos y graficar resultados para:
- Movimiento Rectilíneo Uniforme (MRU)
- Movimiento Rectilíneo Uniformemente Variado (MRUV)
- Tiro Oblicuo

Se exportan las funciones principales para facilitar su uso directo.
"""

# Exportación de las funciones de cálculo cinemático
from fisica.cinematica import mru, mruv, tiro_oblicuo

# Exportación de las funciones de graficación
from fisica.graficos import (
    graficar_posicion,
    graficar_velocidad,
    graficar_aceleracion,
    graficar_mru_mruv,
    graficar_tiro_oblicuo,
    animar_tiro_oblicuo,
)
