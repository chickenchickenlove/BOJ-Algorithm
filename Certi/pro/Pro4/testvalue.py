a = {}

a = [(10,1),(1,10)]

print(min(a, key= lambda x: (x[1], x[0]) if x[0] <5 else (9999,9999)))
print(min(a, key= lambda x: (x[0], x[1])))