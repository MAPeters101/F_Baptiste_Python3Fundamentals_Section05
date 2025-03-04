rate = 5.0, 5.12
print(rate[0])
print(rate[1])
print()

apr = rate[0]
apy = rate[1]
print(apr)
print(apy)
print()

apr, apy = rate
print(apr)
print(apy)
print('-'*80)


a, b, c = 10, 3.14, 'abc'
print(a)
print(b)
print(c)
print()

# a, b, c = 10, 20
#a, b, c = 10, 20, 30, 40

print()

x, y, z = 'abc'
print(x)
print(y)
print(z)
print('='*80)

a = 10 * 2**3 + 5
print(a)
a, b, c = [1,2,3]
print(a)
print(b)
print(c)
print()

s = 'abcdef'
a, b, c =(1+1, s[::-1], 3.14)
print(a)
print(b)
print(c)
print('='*80)

a = 100
b = 3.14
print(a, b)
tmp = a
a = b
b = tmp
print(a, b)
print()

a = 100
b = 3.14
t = b, a
print(t)
a, b = t
print(a)
print(b)
print()

a = 100
b = 3.14
a, b = b, a
print(a)
print(b)
print()



