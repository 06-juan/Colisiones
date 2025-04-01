# Simulación de Colisión Elástica en 2D

Este programa simula la colisión elástica entre dos objetos en un espacio bidimensional y muestra los resultados en una gráfica.

# Descripción

- Se definen objetos físicos con masa, dirección y posición inicial.
- Se calcula el momento y la energía cinética de cada objeto.
- Se determina el tiempo y la posición de colisión iterando en el tiempo.
- Se aplican las ecuaciones de colisión elástica para obtener las velocidades finales.
- Se genera una visualización con los vectores de velocidad antes y después de la colisión.

Se generará una gráfica mostrando:

- Las posiciones iniciales de los objetos.
- Sus vectores de velocidad antes de la colisión.
- El punto de colisión.
- Los vectores de velocidad después de la colisión.

## Explicación del Código

### 1. Decorador `timing`
Mide el tiempo de ejecución de la función `calcular_tiempo_colision`.

### 2. Clase `Objeto`
Representa un objeto físico en 2D con masa, dirección y posición inicial, y calcula propiedades como rapidez, momentum y energía.

### 3. Clase `Colision` (Abstracta)
Define una estructura base para simulaciones de colisiones. Obliga a que las clases que la hereden implementen el método `__str__`.

### 4. Clase `ColisionElastica`
Calcula las velocidades post-colisión usando fórmulas de colisión elástica aplicadas por componente (x, y) a partir de los objetos involucrados.

### 5. Clase 'ColisionInelastica'
Calcula la masa total y la velocidad final por componentes del objeto

### 6. Función `calcular_tiempo_colision`
Itera en el tiempo para determinar el instante y la posición en la que ocurre la colisión, basándose en una tolerancia definida.

### 7. Función `simular_colision_static`
Genera una simulación gráfica 2D de la colisión, mostrando:
- Los orígenes de los objetos.
- Los vectores de velocidad inicial.
- El punto de colisión.
- Los vectores de velocidad post-colisión.

### 8. Función `main`
Ejecuta la simulación llamando a `simular_colision_static`.

## Autor

Creado por Juan Jose Gonzalez
