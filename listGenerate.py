L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [ s.lower() for s in L1 if isinstance(s, str)]

print(L2)

g = (x for x in range(10))
for n in g:
    print(n)