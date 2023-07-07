from CalcGeo import CalcGeo


class Rectangle(CalcGeo):
    
    def __init__(self,longueur,largeur):
        self._longueur = abs(longueur)
        self._largeur = abs(largeur)
    
    @property
    def longueur(self):
        return self._longueur
    
    @property
    def largeur(self):
        return self._largeur
    
    @longueur.setter
    def longueur(self,longueur):
        self._longueur = abs(longueur)
    
    @largeur.setter
    def largeur(self,largeur):
        self._largeur = abs(largeur)
    
    def get_surface(self):
        return self._largeur * self._longueur 
        
    def __eq__(self, o):
        return self._longueur == o._longueur and self._largeur == o._largeur
    
    def __str__(self):
        return f"Rectangle : {self._longueur=}, {self.largeur=}"