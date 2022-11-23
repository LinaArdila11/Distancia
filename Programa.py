
from Punto import Punto

class Programa:

    def __init__ (self):

        self.mipunto1=Punto()
        self.mipunto2=Punto()
       
        self.a=self.mipunto1.calcular_distancia(self.mipunto2)

        self.mipunto1.x=8
        self.mipunto1.y=2

        self.mipunto2.x=9
        self.mipunto2.y=9

        a=self.mipunto1.calcular_distancia(self.mipunto2)

        print (a)

  




