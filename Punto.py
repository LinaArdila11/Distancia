import math

class Punto:

    def __init__ (self):

       self.x=0
       self.y=0

    def calcular_distancia (self,otropunto):

        R=math.sqrt(math.pow((self.x-otropunto.x),2)+math.pow((self.y-otropunto.y),2))

        return R






