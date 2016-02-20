f = open("./test/s3.2.txt")

class Res(object):
    def __init__(self, name, dep=[]):
        self.name = name
        self.dep  = dep

total, phoNum = [int(x) for x in f.readline().split()]

phos = [int(x) for x in f.readline().split()]

maps = []

for i in range(total-1):
    a, b = [int(x) for x in f.readline().split()]
    unique = True
    for j in range(len(maps)):
        if min(a, b) == maps[j].name:
            unique = False
            maps[j].dep.append(max(a, b))
            break
    if unique:
        obj = Res(min(a, b), [max(a, b)])
        maps.append(obj)

def isPho(res, phos):
    for i in phos:
        if int(res) == int(i):
            return True
    return False

def bothPho(arr, phos):
    if arr[0] in phos and arr[1] in phos:
        return True
    else:
        return False

def inMaps(res, maps):
    for i in range(len(maps)):
        if int(res) == int(maps[i].name):
            return i
    return False

def find_res(maps, phos, obj, counter):
    total = 0
    print(obj.name)
    print(obj.dep)
    for i in obj.dep:
        index = inMaps(i, maps)
        if index:
            if isPho(maps[index].name, phos):
                if bothPho(maps[index].dep, phos):
                    total += 1
                total += counter
                total += find_res(maps, phos, maps[index], 1)
            else:
                total += find_res(maps, phos, maps[index], counter + 1)
        else:
            if isPho(i, phos):
                total += counter
    return total
            

print(find_res(maps, phos, maps[0], 1))
