from CalcGeo import CalcGeo
import math

class Cercle(CalcGeo):
    cpt=0
    
    def __init__(self,rayon):
        self._rayon = rayon
        Cercle.cpt+=1
    
    @property        
    def rayon(self):
        return self._rayon
    
    @rayon.setter
    def rayon(self,rayon):
        self._rayon = rayon
        
    def __str__(self):
        return f"{__class__.__name__} rayon:{self._rayon}"
    
    def get_surface(self):
        return math.pi*self._rayon**2
    
    @staticmethod
    def get_cpt():
        return Cercle.cpt

    def __del__(self):
        Cercle.cpt-=1