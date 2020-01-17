print('1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);')
def prime(n):
    i = 2
    while n > i:
        if n % i == 0:
            return 'no_prime'
        i += 1
        if i == n:
            return 'prime'
print(prime(51))
#print(prime(17))

print('2) функция выводит список всех делителей числа:', 256)
def denominator(n):
    result = [] 
    for i in range(1,n+1):
        if n % i == 0:
            result.append(i)
    return result
print(denominator(256))

print('3) выводит самый большой простой делитель числа')
from functools import reduce
def max_denominator(n):
    max_number = denominator(n)
    max_number = reduce(lambda a,b: a if a>b else b, max_number)
    return(max_number)
print(max_denominator(256))

def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum+=i
    return sum

def find(x,*args):
    b=denominator(x)
    number_from10 = []
    for i in b:
        if i>10: number_from10.append(i)
    return number_from10
print(find(256))

def denominator(n):
    result = []
    n = n // 2
    for i in range(1,n+1):
        if n % i == 0:
            result.append(i)
    return result
#print(denominator(256))
