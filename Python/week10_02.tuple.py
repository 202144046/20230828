# p.317

tuple_data = (10,20,30)
a = tuple_data[0]
b = tuple_data[0:]
print(a, b)



# p.318
a = []
b = [1]
c = ()
d = (1, ) #cf. d = (1)
print(type(a), type(b), type(c), (type(d)))

a, b = [10, 20]
c, d = (10, 20)
print(a, b, c, d)

a = 10, 20, 30
b, c, d = a
print(a,b,c,d)

# p.320
a, b = 10,20
b, a = a, b
for a in enumerate([1,2,3]):


def divide(n1, n2):
    a = n1 // n2
    b = n1 % n2
    return a, b

q, r = divide(10, 3)
print(q, r)

