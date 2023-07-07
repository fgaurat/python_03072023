import sys

# a=input("Entrez une valeur : ")

a="0"
a_int = isinstance(a,int)
print(a_int)    

if not a.isnumeric():
    print("!int")
    sys.exit()

a = int(a)

if a==1:
    print("a==1")
elif a==2:
    print("a==2")
else:
    print("else")
print(50*'-')

l = ['Value 01','Value 02','Value 03']

for v in l:
    print(v)
 
 
# 0 Value 01
# 1 Value 02

for v in range(len(l)):
    print(str(v)+" "+l[v])
 
print(list(range(5)))



print(50*'-')


values = [1,5,8,2,4,6,78,15,89,32,87]

to_find = 600000

for v in values:
    print(v)
    if v == to_find:
        print("ok")
        break
        #continue
    print("un traitement...")
else:
    pass    
print("après")