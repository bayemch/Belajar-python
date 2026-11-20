# operasi logika atau boolean
# not, or, and, xor


# not
print('====Not====')
a = True
c = not a
print('data a = ', a)
print('----------NOT')
print('data c = ', c)


# or (jika salah satu atau keduanya True, maka akan true)
print('====OR====')
a = False
b = False
c = a or b
print(a, 'OR', b, '= ', c)
a = False
b = True
c = a or b
print(a, 'OR', b, ' = ', c)
a = True
b = False
c = a or b
print(a, ' OR', b, ' = ', c)
a = True
b = True
c = a or b
print(a, ' OR', b, ' = ', c)