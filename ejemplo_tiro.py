import fisica
from fisica.graficos import graficar_tiro_oblicuo
from fisica.graficos import animar_tiro_oblicuo

resultado = fisica.cinematica.tiro_oblicuo(15, 25, 12, 50)

animar_tiro_oblicuo(resultado)