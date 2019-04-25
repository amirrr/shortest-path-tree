
def checks(di, vis):
    res = set()
    for i in di:
        if i in vis:
            if not di[i] in vis:
                res.add(di[i])
        else:
            res.add(i)

    return res

a = {1: 4, 2: 5, 3: 6}
b = {}

for key in a:
    b[a[key]] = a[key]

#a.update(b)

print(a)
print(checks(a, set([1,3])))
