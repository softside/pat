a = range(5)
def mutate(a):
    a[3] = 100
mutate(a)
print a[3]

a = range(5)
def mutate(b):
    a[3] = 100
mutate(a)
print a[3]

a = range(5)
def mutate(b):
    b[3] = 100
mutate(a)
print a[3]
