#!/usr/bin/python
# filename:fib.py

def fib(n):
    a,b = 0,1
    while b < n:
        print(b,end=' ')
        a,b = b,a+b
    print('Over...')

if __name__ == '__main__':
    print('程序自身运行')
    print(dir())
else:
    print('外部导入程序')

