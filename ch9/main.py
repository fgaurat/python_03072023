import sys
from Rectangle import Rectangle
from Carre import Carre
from Cercle import Cercle
from DataRectangle import Rectangle as DataRectangle

def main():
    r = Rectangle(2,4)
    r1 = Rectangle(2,4)
    # print(r.get_longueur())
    # r.set_longueur(-12) 
    # print(r.get_longueur())
    surface = r.get_surface() # 8
    print(surface)
    r.longueur = 12
    r1.longueur = 12
    a = r.longueur
    print(a)

    # if r.__eq__(r1):
    if r==r1:
        print('ok')
    else:
        print('ko')
        
    
    s = str(r)
    print(s)
    
    dr = DataRectangle(3,2)
    print(dr)
    print(dr.longueur)
    print(dr.surface)
    print(50*'-')
    c = Carre(2)
    print(c.get_surface())
    print(c)
    print(50*'-')
    
    ce = Cercle(2)
    ce1 = Cercle(2)
    ce2 = Cercle(2)
    del ce2
    print("ce.cpt",ce.cpt)
    print("ce1.cpt",ce1.cpt)
    print("Cercle.cpt",Cercle.cpt)
    print("Cercle.get_cpt()",Cercle.get_cpt())
    print(ce)
    print(ce.get_surface())
    print()
    
    
if __name__=='__main__':
    main()

