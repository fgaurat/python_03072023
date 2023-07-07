def fib(n:int):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        print("la suite")
        a, b = b, a+b
    print()
# Now call the function we just defined:
a = fib(2000)
print(a)




def fib2(n:int)->list:    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    l = []
    a, b = 0, 1
    while a < n:
        l.append(a)
        a, b = b, a+b
    
    return l

a = fib2(2000)
# [0,1,1,2,3,5,8]
print(a)
print(50*'-')

def hello(name,firstName="empty"):
    print("hello "+name+" "+firstName)

# hello(firstName="fred")
# # hello()
# hello("Gaurat","fred")
# hello(firstName="fred",name="Gaurat")

print(50*'-')


def add(*theList):
    print(theList)
    total=0
    for v in theList:
    #    total=total+v 
       total+=v 
    return total

l = [1,2,3,4]
# r = add(l)
r = add(1,2,3,4)
r = add(1,2,3,4,58)
r = add(1,12)
print(r)  # 10


print('toto','titi','tutu',sep="-")



def hello(**info):
    print("name",info['name'])
    print("firstName",info['firstName'])

hello(name="toto",firstName="tutu")
# hello(nom="toto",prenom="tutu")


d = {"toto":"truc"}

print(50*'-')


def f1(a,b):
    print(a,b)

f1("truc a",'truc b') # position
f1(b="truc b",a="truc a") # keyword

def f2(*a):
    print(a)    

f2("truc a",'truc b')
f2("truc a",'truc b','truc c')


def f3(**a):
    print(a)    

f3(k1="truc a",k2='truc b')
f3(k2="truc a",k1='truc b',uneAutre='truc c')

def f4(*p,**k):
    print(p)
    print(k)

f4("position 01","position 03",k2="truc a",k1='truc b',uneAutre='truc c')
f4("position 01","position 03")
f4(k2="truc a",k1='truc b',uneAutre='truc c')


print(50*'-')


def add(*theList):
    print(theList)
    total=0
    for v in theList:
       total+=v 
    return total


r = add(1,2,3)
l = [1,2,3]
r = add(*l)

print(50*'-')

l = [1,2,3]

def mult2(item):
    return item*2

l2 = map(mult2,l)
print(list(l2))

l2 = map(lambda i:i*2,l)
print(list(l2))


