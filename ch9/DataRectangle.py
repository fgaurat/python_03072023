from dataclasses import dataclass

@dataclass
class Rectangle:
    
    longueur:int=0
    largeur:int=0
    
    @property
    def surface(self):
        return self.largeur*self.longueur