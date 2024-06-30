def add(x):
    r = lambda z: z+x
    return r

g = add(7)
d = g(4)
print(d)