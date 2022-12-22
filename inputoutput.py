s = 'Hello, world.'
print(str(s))
print(repr(s))
print(str(1/7))

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

hello = 'hello, world\n'
print(hello)
hellos = repr(hello)
print(hellos)
repr((x, y, ('spam', 'eggs')))#can take any vales
print(repr)