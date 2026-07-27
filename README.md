# Trabajo Práctico — Cinemática y Física con Python

## Objetivo

El objetivo de esta actividad es desarrollar una biblioteca de simulaciones físicas en Python para el estudio de movimientos en una y dos dimensiones (MRU, MRUV y Tiro Oblicuo), aplicando los conceptos vistos en la materia:

* Creación y estructura de paquetes y módulos (`__init__.py`, importaciones).
* Funciones y modularización del código.
* Estructuras de datos (`List`, `Dict`, `Tuple`).
* Operaciones matemáticas con el módulo estándar `math`.
* Visualización gráfica y animaciones interactivas utilizando `matplotlib`.
* Uso de constantes físicas compartidas.
* Entrada, salida y validación de datos.

---

## Archivos del ejercicio

El proyecto está organizado como un paquete de Python llamado `fisica` junto a tres archivos de ejemplo:

```text
tp_fisica/
├── README.md
├── ejemplo_mru.py
├── ejemplo_mruv.py
├── ejemplo_tiro.py
└── fisica/
    ├── __init__.py
    ├── cinematica.py
    ├── constantes.py
    └── graficos.py
```

### Módulos provistos (No modificar):

* `fisica/constantes.py`: Contiene las constantes físicas del sistema, como la aceleración de la gravedad (g = 9.81 m/s²).
* `fisica/graficos.py`: Provee las funciones de visualización gráfica estática, subplots interactivos y animaciones en tiempo real con `matplotlib`.
* `fisica/__init__.py`: Exporta las funciones principales para facilitar la importación directa desde el paquete `fisica`.

---

## Consigna

Deberás completar las funciones del módulo `fisica/cinematica.py` y crear los scripts de prueba (`ejemplo_mru.py`, `ejemplo_mruv.py` y `ejemplo_tiro.py`) haciendo uso de la biblioteca `fisica`.

Los alumnos deberán completar **únicamente** la lógica matemática y simulación dentro del módulo `fisica/cinematica.py`. Las herramientas de graficación y constantes ya vienen provistas.


## Modalidad de trabajo

La resolución del ejercicio deberá realizarse utilizando **Git** y **GitHub**.

### 1. Crear una rama personal

Antes de comenzar a programar, cada alumno deberá crear una rama a partir de `main`.

La rama deberá tener el siguiente formato:

```text
apellido_nombre
```

Por ejemplo:

```text
cortesini_luciano
perez_juan
```

### 2. Resolver el ejercicio

* Completar las funciones indicadas en `fisica/cinematica.py`.
* Implementar los scripts de prueba `ejemplo_mru.py`, `ejemplo_mruv.py` y `ejemplo_tiro.py`.

### 3. Realizar commits

Se recomienda realizar commits pequeños y con mensajes descriptivos.

Ejemplos:

```text
Implementa funciones auxiliares de MRU
Completa calculo de tiro oblicuo
Agrega script de ejemplo para mruv
```

### 4. Crear un Pull Request

Una vez finalizado el ejercicio, cada alumno deberá crear un **Pull Request (PR)** desde su rama personal hacia la rama `main`.

La entrega será evaluada tanto por el correcto funcionamiento del paquete físico como por el buen uso de Git y GitHub.
