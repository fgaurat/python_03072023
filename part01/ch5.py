from collections import deque

l = [1,2,3,4]
print(l)
i = l.pop()
print(l)
print(i)
l.insert(0,0)
print(l)
firstItem = l.pop(0)
print(firstItem)
print(l)

d = deque(l)

d.appendleft(-12)
print(d)


l = []

for i in range(20):
    if i%2 ==0:
        l.append(i)
print(l)
l = []

for i in range(0,20,2):
    l.append(i)
print(l)

l = list(map(lambda i:i,range(0,20,2)))
print(l)

l = [x for x in range(0,20,2)]
print(l)

l = [x for x in range(20)[1:] if x%2==0]
print(l)
l = ["  ligne 01   ","  ligne 02","ligne 03   "]
print(l)
l = [i.strip() for i in l]
print(l)

# l1 = ['val1','val2','val3','val4']
# l2 = [12,14,59]
# print(list(zip(l1,l2)))


print(l[0])
del l[0]
print(l[0])
print(l)
print(50*'-')

t = 10,20,859,"toto","tutu"
print(t)
a,b,*c=0,1,2,4,5,9,8,7,4
# t=0,1

# def t(a,b,*c):
#     pass
# t(0,1,2,4,5,9,8,7,4)
print(a,b,c)


def f():
    
    return 12,15

a,b = f()
print(a,b)


a = 1,

print(50*'-')

l = [1,2,3]
t =1,2,3
s = {1,2,3,2,1}
print(s)

l=['ligne1','ligne2','ligne3','ligne1']
l = list(set(l))
print(l)

print(50*'-')



d = {
    "name":"GAURAT",
    "firstName":"Fred"
}

# print(d['name'])

for k,v in d.items():
    print(k,v)
    
l = ["value 01","value 02","value 03"]

for i,v in enumerate(l):
    print(i,v)
