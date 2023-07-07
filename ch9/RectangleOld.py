


class Rectangle:
    
    def __init__(self,longueur,largeur):
        self._longueur = abs(longueur)
        self._largeur = abs(largeur)
    
    def get_longueur(self):
        return self._longueur

    def get_largeur(self):
        return self._largeur
    
    def set_longueur(self,longueur):
        self._longueur = abs(longueur)

    def set_largeur(self,largeur):
        self._largeur = abs(largeur)
    
    def get_surface(self):
        return self._largeur * self._longueur 
        