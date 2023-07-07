import copy


print("Bonjour")

# theWorldIsFlat => camelCase
# TheWorldIsFlat => UpperCamelCase, PascalCase
# the-world-is-flat => kebab-case
# the_world_is_flat => snake_case

the_world_is_flat = False  # inférence de type
if the_world_is_flat:
    print("Be careful not to fall off!")
    print("toto !")
    

a = "Une valeur"
b = 'Une autre valeur'
print(a)
print(b)
print(a+" "+b)

a = 'L\'orage gronde'
print(a)
a = "L'orage gronde"
print(a)

a=12
b = "La valeur de a : "+str(a)
print(b)

a=2
b=3
c=a+b
lines = "Ligne 1\nLigne 2"
print(lines)
path = "c:\news\truc"
path = "c:\\news\\truc"
path = r"c:\news\truc"
print(path)

lines="""Ligne1
Ligne3
Ligne4
Ligne5"""
print(lines)


print(50*'-')
a = 12
s = "a:"*a

print(s)
print(50*'-')
word = 'Python'

print(len(word))
print(word[len(word)-1])
print(word[-1]) 
print(word[3:5]) 
print(word[:3]) 
print(word[3:]) 
print(word[::2]) 

# word[1] = 't'
print(word)

a = 1
print(hex(id(a)) )
a = 2
print(hex(id(a)) )

b=2
print(hex(id(b)) )

word = 'Python'
word2 = 'J' + word[1:]
print(word)
print(word2)

print(50*'-')
squares = [1, 4, 9, 16, 25]
print(squares)
squares2 = squares[:]
squares2[0] = 1000
print(squares2)
print(squares)

print(50*"-")
l1 = [
    [0,1],
    [2,3],
    [4,5],
]
# l2 = l1[:]
l2 = copy.deepcopy(l1)
l2[0][1]=1000
print(l1)
print(l2)


print(50*'-')
squares = [1, 4, 9, 16, 25]
print(hex(id(squares)))
squares.append(36)
print(hex(id(squares)))
print(squares)