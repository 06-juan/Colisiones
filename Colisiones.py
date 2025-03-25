import math

class objeto:
    '''Todo los objetos tienen masa y
    velocidad durante una colision por ello podemos 
    calcular su velocidad y momentum'''
    def __init__ (self,masa,direccion):
        self.masa = masa
        self.direccion_x = direccion[0]
        self.direccion_y = direccion[1]
        self.direccion_z = direccion[2]
        rapidez = math.sqrt(direccion[0]**2+direccion[1]**2+direccion[2])
        self.rapidez = rapidez
           
        #self.momentum_magnitud = masa*rapidez
        self.energia = (0.5*masa*rapidez**2)

        self.momentum_x = self.direccion_x*masa 
        self.momentum_y = self.direccion_y*masa
        self.momentum_z = self.direccion_z*masa


class colision_inelastica:
    '''para las colisiones inelasticas la masa final es la suma de las masas y se conserva el momentum'''
    def __init__ (self,objeto1,objeto2):
        masa_final = objeto1.masa + objeto2.masa
        self.masa_final = masa_final 

        self.velocidad_final_x = (objeto1.momentum_x + objeto2.momentum_x)/self.masa_final
        self.velocidad_final_y = (objeto1.momentum_y + objeto2.momentum_y)/self.masa_final
        self.velocidad_final_z = (objeto1.momentum_z + objeto2.momentum_z)/self.masa_final                                  

    def __str__ (self):
        return (f'despues de la colision se tiene una masa de {self.masa_final} con una velocidad descrita por el vector'
                '({self.velocidad_final_x},{self.velocidad_final_y},{self.velocidad_final_z})')


class colision_elastica:
    '''para las colisiones elasticas tanto el momentum como la energia se conserva'''
    def __init__(self,objeto1,objeto2):
        self.velocidad_final_x_2 = (2*objeto1.momentum_x + objeto2.momentum_x - (objeto1.masa * objeto2.direccion_x))/(objeto1.masa + objeto2.masa)
        self.velocidad_final_y_2 = (2*objeto1.momentum_y + objeto2.momentum_y - (objeto1.masa * objeto2.direccion_y))/(objeto1.masa + objeto2.masa)
        self.velocidad_final_z_2 = (2*objeto1.momentum_z + objeto2.momentum_z - (objeto1.masa * objeto2.direccion_z))/(objeto1.masa + objeto2.masa)

        self.velocidad_final_x_1 = objeto2.direccion_x - objeto1.direccion_x + self.velocidad_final_x_2
        self.velocidad_final_y_1 = objeto2.direccion_y - objeto1.direccion_y + self.velocidad_final_y_2
        self.velocidad_final_z_1 = objeto2.direccion_z - objeto1.direccion_z + self.velocidad_final_z_2

    def __str__(self):
        return('despues de la colision el objeto 1 tiene una velocidad descrita por el vector'
               f'({self.velocidad_final_x_1},{self.velocidad_final_y_1},{self.velocidad_final_z_1})'
                'y el el objeto 2 descrita por el vector' 
                f'({self.velocidad_final_x_2},{self.velocidad_final_y_2},{self.velocidad_final_z_2})')


Vector1=[1,0,0]
Vector2 = [-1,0,0]

objeto1 = objeto(1,Vector1)
objeto2 = objeto(10,Vector2)

colision = colision_elastica(objeto1,objeto2)


print(colision)