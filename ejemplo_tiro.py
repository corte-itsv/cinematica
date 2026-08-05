from fisica.graficos import (
    graficar_posicion,
    graficar_velocidad,
    graficar_aceleracion,
    graficar_mru_mruv,
    graficar_tiro_oblicuo,
    animar_tiro_oblicuo,
)

import fisica

resultado = fisica.cinematica.tiro_oblicuo(10, 10, 10, 10)

animar_tiro_oblicuo(resultado)