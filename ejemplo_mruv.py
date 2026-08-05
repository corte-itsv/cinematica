from fisica.graficos import (
    graficar_posicion,
    graficar_velocidad,
    graficar_aceleracion,
    graficar_mru_mruv,
    graficar_tiro_oblicuo,
    animar_tiro_oblicuo,
)

import fisica

resultado = fisica.cinematica.mruv(5, 5, 5, 5, 5)

print(resultado)