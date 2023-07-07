import sys

def main():
    # with open('mon_fichier.txt') as f: Lecture par défaut
    with open('mon_fichier.txt','r') as f:
        # s = f.read()
        # print(s)
        # l = f.readlines()
        # print(l)
        for line in f:
            print(line.strip()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
                  )

def main_write():
    with open('mon_fichier.txt','a') as f:
        f.write("Bonjour\n")
        print("Bonjour from print",file=f)
    
def main01():
    a =2
    s = f"{a}"
    print(s)
    s = f"{a=}"
    print(s)
    
    a = 2/3
    print(f"{a*100:.2f}%")
    print(f"{a:.2%}")
    
    infos=["Gaurat","Fred"]
    
    
    r = "Bonjour {0} {1}".format(infos[0],infos[1])
    r = "Bonjour {} {}".format(infos[0],infos[1])
    r = "Bonjour {} {}".format(*infos)
    print(r)
    d={
         "name":"Gaurat",   
         "firstName":"Fred",   
    }
    
    r = "Bonjour {name} {fname}".format(name=d['name'],fname = d['firstName'])
    r = "Bonjour {name} {firstName}".format(**d)
    print(r)
    
    r = f"value : {d['name']:<10} après"
    print(r)

if __name__=='__main__':
    main()
