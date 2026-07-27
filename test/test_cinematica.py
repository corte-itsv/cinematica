import math
import pytest
from fisica.cinematica import (
    calcular_lista_tiempo,
    calcular_posicion_mru,
    mru,
    calcular_posicion_mruv,
    calcular_velocidad_mruv,
    mruv,
    obtener_componentes_velocidad,
    calcular_tiempo_vuelo,
    tiro_oblicuo,
)
import fisica.constantes as c


def test_calcular_lista_tiempo():
    # Caso normal
    t = calcular_lista_tiempo(10.0, 5)
    assert len(t) == 6
    assert t == [0.0, 2.0, 4.0, 6.0, 8.0, 10.0]

    # Caso tiempo_final = 0
    t_zero = calcular_lista_tiempo(0.0, 4)
    assert len(t_zero) == 5
    assert all(val == 0.0 for val in t_zero)


def test_calcular_posicion_mru():
    pos = calcular_posicion_mru(5.0, 2.0, 3.0)
    assert pos == 11.0

    pos_neg = calcular_posicion_mru(0.0, -5.0, 2.0)
    assert pos_neg == -10.0


def test_mru_exito():
    res = mru(posicion_inicial=5.0, velocidad=2.0, tiempo_final=10.0, divisiones=2)
    assert isinstance(res, dict)
    assert set(res.keys()) == {"t", "x", "v", "a"}
    assert res["t"] == [0.0, 5.0, 10.0]
    assert res["x"] == [5.0, 15.0, 25.0]
    assert res["v"] == [2.0, 2.0, 2.0]
    assert res["a"] == [0.0, 0.0, 0.0]


def test_mru_validaciones():
    # tiempo_final negativo
    res_tiempo_neg = mru(posicion_inicial=0.0, velocidad=5.0, tiempo_final=-1.0, divisiones=10)
    assert res_tiempo_neg is None

    # divisiones <= 0
    res_div_cero = mru(posicion_inicial=0.0, velocidad=5.0, tiempo_final=10.0, divisiones=0)
    assert res_div_cero is None

    res_div_neg = mru(posicion_inicial=0.0, velocidad=5.0, tiempo_final=10.0, divisiones=-5)
    assert res_div_neg is None


def test_calcular_posicion_mruv():
    # x = x0 + v0*t + 0.5*a*t^2 = 0 + 10*4 + 0.5*2*(16) = 40 + 16 = 56
    pos = calcular_posicion_mruv(0.0, 10.0, 2.0, 4.0)
    assert pos == 56.0


def test_calcular_velocidad_mruv():
    # v = v0 + a*t = 10 + 2*4 = 18
    vel = calcular_velocidad_mruv(10.0, 2.0, 4.0)
    assert vel == 18.0


def test_mruv_exito():
    # Se evalúa el comportamiento actual del módulo mruv
    res = mruv(posicion_inicial=0.0, velocidad_inicial=10.0, aceleracion=2.0, tiempo_final=4.0, divisiones=2)
    assert isinstance(res, dict)
    assert set(res.keys()) == {"t", "x", "v", "a"}
    assert res["t"] == [0.0, 2.0, 4.0]
    assert res["x"] == [0.0, 24.0, 56.0]
    assert res["v"] == [10.0, 14.0, 18.0]
    assert res["a"] == [-c.G, -c.G, -c.G]


def test_mruv_validaciones():
    res_tiempo_neg = mruv(0.0, 10.0, 2.0, -5.0, 10)
    assert res_tiempo_neg is None

    res_div_cero = mruv(0.0, 10.0, 2.0, 10.0, 0)
    assert res_div_cero is None


def test_obtener_componentes_velocidad():
    v0x, v0y = obtener_componentes_velocidad(100.0, 60.0)
    assert v0x == pytest.approx(50.0)
    assert v0y == pytest.approx(100.0 * math.sin(math.radians(60.0)))

    # Ángulo 0 grados
    v0x_0, v0y_0 = obtener_componentes_velocidad(50.0, 0.0)
    assert v0x_0 == pytest.approx(50.0)
    assert v0y_0 == pytest.approx(0.0)


def test_calcular_tiempo_vuelo():
    # v0y = 19.62, h0 = 0 -> t_vuelo = 2 * 19.62 / 9.81 = 4.0
    t_vuelo = calcular_tiempo_vuelo(19.62, 0.0)
    assert t_vuelo == pytest.approx(4.0)

    # Discriminante negativo
    t_vuelo_invalid = calcular_tiempo_vuelo(0.0, -100.0)
    assert t_vuelo_invalid is None


def test_tiro_oblicuo_exito():
    res = tiro_oblicuo(velocidad_inicial=20.0, angulo=45.0, altura_inicial=0.0, divisiones=10)
    assert isinstance(res, dict)
    assert set(res.keys()) == {"t", "x", "y", "vx", "vy", "ax", "ay"}
    assert len(res["t"]) == 11
    assert len(res["x"]) == 11
    assert len(res["y"]) == 11
    assert len(res["vx"]) == 11
    assert len(res["vy"]) == 11
    assert len(res["ax"]) == 11
    assert len(res["ay"]) == 11

    # Primer y último valor de tiempo
    assert res["t"][0] == 0.0
    assert res["y"][0] == pytest.approx(0.0)
    assert res["y"][-1] == pytest.approx(0.0, abs=1e-5)
    assert res["ax"] == [0.0] * 11
    assert res["ay"] == [-c.G] * 11


def test_tiro_oblicuo_validaciones():
    # Velocidad 0 y altura 0 produce t_vuelo <= 0
    res_cero = tiro_oblicuo(velocidad_inicial=0.0, angulo=45.0, altura_inicial=0.0, divisiones=10)
    assert res_cero is None
