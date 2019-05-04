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

print(a)
print(checks(a, set([1,3])))

class Abasi:
    general = 0
    def __init__(self, data):
        self.d = data
        Abasi.general = Abasi.general+1
    
    def get_data(self):
        return self.d

sall = []
vall = []

Abasi.general = 5

a1 = Abasi(1)
sall.append(a1)
a2 = Abasi(2)
sall.append(a2)
a3 = Abasi(3)
sall.append(a3)
a4 = Abasi(4)
sall.append(a4)
a5 = Abasi(5)
sall.append(a5)

middle = int(len(sall)/2)+1
print(middle)
for i in sall:
    print(i.d, '- ', end='')
print('\n')
