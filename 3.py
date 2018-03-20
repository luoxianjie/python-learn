
###list  有序列表
classmates = ['jack','bob','lucy']

print(classmates[0])
print(len(classmates))
print(classmates[-1])
print(classmates[-3])


classmates.append('tom')

print(classmates)

classmates.insert(2,'michael')

print(classmates)

classmates.pop()

print(classmates)

### tuple  元组 (元素不允许修改)
classmates = ('tom','bob','jack')

print(classmates[0])

# classmates[0] = 'lucy' 会报错

### 条件判断
age = 18

if age >= 18:
    print('hahah')
elif age >= 28:
    print('hehed')
else:
    print('haxbb')

### 循环语句
classmates = ['jack','tom','bob']

for classmate in classmates :
    print('your classmate:'+ classmate)

### dict 字典
d = {'name':'bob','age':18,'sex':'male'}

print(d['name'])

d['name'] = 'jack'

print(d)

for prop in d:
    print(prop + ':'+ str(d[prop]))    #'+'号只能用于连接字符串要用str()强制转换类型

print('name' in d)
print(d.get('name'))
print(d.pop('sex'))
print(d)

### set
s = set([1,2,3])

print(s)

s.add(4)

print(s)

s.remove(4)

print(s)


s1 = set([1,2,3])
s2 = set([2,3,4])

print(s1 & s2)
print(s1 | s2)

### 函数
def my_fun(num):
    a = abs(num)
    return a

print(my_fun(-28))

def power(x):
    return x*x

print(power(5))

def fact(n):
    if(n == 1):
        return 1
    return n * fact(n-1)

print(fact(5))


### 切片
L = ['Tom','Bob','Lucy'];

print(L[:3])

print(L[2:3])

