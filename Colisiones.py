import matplotlib

class objeto:
    '''Todo los objetos tienen masa y
    velocidad durante una colision por ello podemos 
    calcular su velocidad y momentum'''
    def __init__ (self,masa,velocidad):
        self.masa = masa
        self.velocidad = velocidad
        
        self.momentum = masa*velocidad
        self.energia = (0.5*masa*velocidad**2)

objeto1= objeto(10,10)
print(objeto1.energia)