import math
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
import time

# -------------------------------
# Decorador para medir el tiempo de ejecución
#los decoradores toman una funcion y le agregan funcionalidad extra
def timing(func):
    """
    Decorador que mide y muestra el tiempo de ejecución de una función.
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Tiempo de ejecución de {func.__name__}: {end - start:.3f} segundos")
        return result
    return wrapper

# -------------------------------
# Clase que representa un objeto físico en 2D
class Objeto:
    def __init__(self, masa, direccion, origen):
        """
        Inicializa un objeto físico en 2D.
        
        Parámetros:
            masa: masa del objeto.
            direccion: vector de velocidad (vx, vy).
            origen: posición inicial (x, y).
        """
        # Convertir a tupla (en 2D se esperan 2 componentes)
        self.__masa = masa # los dos guiones bajos son para la encapsulación
        self.__direccion = tuple(direccion)  # vector de velocidad (vx, vy)
        self.__origen = tuple(origen)        # posición inicial (x, y)
        # Calcular la rapidez (norma del vector de velocidad)
        self.__rapidez = math.sqrt(self.__direccion[0]**2 + self.__direccion[1]**2)
        # Calcular el momentum (vector)
        self.__momentum = (self.__masa * self.__direccion[0],
                           self.__masa * self.__direccion[1])
    
    @property   #nos permite acceder a obj.masa pero sin cambiarla
    def masa(self): # el property lo combierte en solo lectura
        return self.__masa

    @property
    def direccion(self):
        return self.__direccion

    @property
    def origen(self):
        return self.__origen

    @property
    def rapidez(self):
        return self.__rapidez

    @property
    def momentum(self):
        return self.__momentum

    @property
    def energia(self):
        return 0.5 * self.__masa * self.__rapidez**2

# -------------------------------
# Clase abstracta para colisiones (define la interfaz para los tipos de colisión)
class Colision(ABC):
    @abstractmethod
    def __str__(self):
        pass
#con esta me aseguro que cada clase que la herede tenga __str__ definido, sino da error

# -------------------------------
# Clase para simular una colisión elástica en 2D
# obj1:Objeto significa que se espera que el obj1 sea una instancia de Objeto o subclase de este
class ColisionElastica(Colision):
    def __init__(self, obj1: Objeto, obj2: Objeto):
        """
        Calcula las velocidades post-colisión para una colisión elástica en 2D,
        aplicando las fórmulas unidimensionales en cada componente.
        """
        m1, m2 = obj1.masa, obj2.masa
        v1 = obj1.direccion
        v2 = obj2.direccion
        # Fórmula para velocidad final del objeto 1
        self.__velocidad_final_obj1 = (
            ((m1 - m2) / (m1 + m2)) * v1[0] + ((2 * m2) / (m1 + m2)) * v2[0],
            ((m1 - m2) / (m1 + m2)) * v1[1] + ((2 * m2) / (m1 + m2)) * v2[1]
        )
        # Fórmula para velocidad final del objeto 2
        self.__velocidad_final_obj2 = (
            ((2 * m1) / (m1 + m2)) * v1[0] + ((m2 - m1) / (m1 + m2)) * v2[0],
            ((2 * m1) / (m1 + m2)) * v1[1] + ((m2 - m1) / (m1 + m2)) * v2[1]
        )

    @property
    def velocidad_final_obj1(self):
        return self.__velocidad_final_obj1

    @property
    def velocidad_final_obj2(self):
        return self.__velocidad_final_obj2

    def __str__(self):
        return (f"Colisión elástica:\nObjeto 1 velocidad final = {self.__velocidad_final_obj1[0]:.3},{self.__velocidad_final_obj1[1]:.3}\n"
                f"Objeto 2 velocidad final = {self.__velocidad_final_obj2[0]:.3},{self.__velocidad_final_obj2[1]:.3}")

class ColisionInlastica(Colision):
    def __init__(self, obj1: Objeto, obj2: Objeto):
        """
        Calcula las velocidades post-colisión para una colisión elástica en 2D,
        aplicando las fórmulas unidimensionales en cada componente.
        """
        m1, m2 = obj1.masa, obj2.masa
        self.__masa_final = m1 + m2
        v1 = obj1.direccion
        v2 = obj2.direccion
        # Fórmula para velocidad final del objeto 1
        self.__velocidad_final_obj1 = (
            ((m1*v1[0] + m2*v2[0]) / (m1 + m2)),
            ((m1*v1[1] + m2*v2[1]) / (m1 + m2))
        )

    @property
    def velocidad_final_obj1(self):
        return self.__velocidad_final_obj1
    
    @property
    def masa_final(self):
        return self.__masa_final


    def __str__(self):
        return (f"Colisión elástica:\nObjeto 1 velocidad final = {self.__velocidad_final_obj1[0]:.3},{self.__velocidad_final_obj1[1]:.3}\n"
                f"Con una masa total de {self.__masa_final}")

# -------------------------------
# Función numérica para determinar el instante de colisión en 2D
@timing
def calcular_tiempo_colision(obj1: Objeto, obj2: Objeto, max_t=100, dt=0.001):
    """
    Itera en el tiempo para determinar el instante en el que dos objetos
    están a una distancia menor que epsilon. Se asume que en la colisión,
    ambos objetos comparten la misma posición.
    
    Retorna:
        t_col: instante de colisión.
        pos_col: posición de colisión (x, y).
    """
    t = 0
    epsilon = 1e-3  # tolerancia para determinar la colisión
    while t < max_t:
        pos1 = (obj1.origen[0] + obj1.direccion[0] * t,
                obj1.origen[1] + obj1.direccion[1] * t)
        pos2 = (obj2.origen[0] + obj2.direccion[0] * t,
                obj2.origen[1] + obj2.direccion[1] * t)
        # Calcular distancia euclidiana entre pos1 y pos2
        dist = math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)
        if dist < epsilon:
            return t, pos1  # se asume que en colisión ambas posiciones coinciden
        t += dt
    return None, None

# -------------------------------
# Función que muestra una gráfica estática en 2D
def simular_colision_static():
    """
    Simula una colisión en 2D y muestra en una gráfica:
      - Los orígenes de cada objeto con sus vectores de velocidad inicial.
      - El punto de colisión.
      - Desde el punto de colisión, se dibujan los vectores de velocidad post-colisión
        obtenidos mediante la colisión elástica.
    """
    # Definición de objetos en 2D
    origen1 = (-5, 5)
    origen2 = (4, -4)
    vector1 = (1, -1)    # velocidad inicial del objeto 1
    vector2 = (-1, 1)  # velocidad inicial del objeto 2
    obj1 = Objeto(1, vector1, origen1)
    obj2 = Objeto(2, vector2, origen2)
    
    # Determinar el instante y punto de colisión
    t_col, pos_col = calcular_tiempo_colision(obj1, obj2)
    if t_col is None:
        print("No se detectó colisión en el intervalo de tiempo dado.")
        return
    print(f"Colisión detectada en t = {t_col:.3f} s, en la posición ({pos_col[0]:.3f}, {pos_col[1]:.3f})")

    # Modificación clave: Usar una variable única para la colisión
    tipo_colision = "inelastica"  # Cambiar entre "elastica" "inelastica" si se desea

    if tipo_colision == "elastica":
        colision = ColisionElastica(obj1, obj2)
        v1_final = colision.velocidad_final_obj1
        v2_final = colision.velocidad_final_obj2
    else:
        colision = ColisionInlastica(obj1, obj2)
        v1_final = colision.velocidad_final_obj1
        v2_final = v1_final  # En inelástica, ambos objetos tienen la misma velocidad

    print(colision)
    
    # Crear la gráfica 2D
    fig, ax = plt.subplots(figsize=(8, 6)) #fig es el lienzo y ax son los ejes
    ax.set_title("Colisión en 2D: Orígenes y vectores de velocidad")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.grid(True)
    
    # Graficar los orígenes de los objetos
    ax.scatter(obj1.origen[0], obj1.origen[1], color='red', s=100, label="Origen Objeto 1")
    ax.scatter(obj2.origen[0], obj2.origen[1], color='blue', s=100, label="Origen Objeto 2")
    
    # Dibujar los vectores de velocidad inicial (pre-colisión) desde sus orígenes
    escala = 1  # factor de escala para visualizar los vectores
    ax.quiver(obj1.origen[0], obj1.origen[1],
              obj1.direccion[0], obj1.direccion[1],
              angles='xy', scale_units='xy', scale=escala,
              color='red', width=0.005, label="Vel. Inicial Objeto 1")
    ax.quiver(obj2.origen[0], obj2.origen[1],
              obj2.direccion[0], obj2.direccion[1],
              angles='xy', scale_units='xy', scale=escala,
              color='blue', width=0.005, label="Vel. Inicial Objeto 2")
    
    # Graficar el punto de colisión
    ax.scatter(pos_col[0], pos_col[1], color='magenta', s=100, label="Punto de Colisión")
    
    # Dibujar los vectores de velocidad post-colisión (desde el punto de colisión)

    if tipo_colision == "elastica":
        ax.quiver(pos_col[0], pos_col[1],
                v1_final[0], v1_final[1],
                angles='xy', scale_units='xy', scale=escala,
                color='orange', width=0.005, label="Vel. Post-colisión Objeto 1")
        ax.quiver(pos_col[0], pos_col[1],
                v2_final[0], v2_final[1],
                angles='xy', scale_units='xy', scale=escala,
                color='cyan', width=0.005, label="Vel. Post-colisión Objeto 2")
    else:
        ax.quiver(pos_col[0], pos_col[1],
                v1_final[0], v1_final[1],
                angles='xy', scale_units='xy', scale=escala,
                color='orange', width=0.005, label="Vel. Post-colisión (Fusión)")

    ax.legend()
    plt.show()

def main():
    simular_colision_static()

# solo lo ejecutamos directamente, no en otro
if __name__ == "__main__":
    main()