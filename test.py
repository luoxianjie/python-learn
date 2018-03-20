# 自定义函数
def my_abs(x):
    if x >=0:
        return x
    else:
        return -x

# list
a = [1,2,3,4]

# tuple
b = (1,2,3,4)

# dict
c = {'a':1,'b':2}

# set
d = set([1,1,22,3,4,4])

# 递归

def fact(x):
    if x==1 or x==2:
        return x
    else:
        return fact(x-1) + fact(x-2)

L = ['Michael', 'Sarah', 'Tracy']
r = []
n = 3

for i in range(n):
    r.append(L[i])



print(my_abs(-23))
print(a)
print(b)
print(c)
print(d)

print(fact(4))

print(r)
print(r[:1])
print(r[1:])

