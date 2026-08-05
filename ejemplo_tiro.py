import fisica
print(fisica.cinematica.tiro_oblicuo(10,10,10,10))
from fisica.graficos import graficar_tiro_oblicuo

resultado = fisica.cinematica.tiro_oblicuo(10, 10, 10, 10)
graficar_tiro_oblicuo(resultado)