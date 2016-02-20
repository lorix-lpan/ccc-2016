# f = open("./test/j2.txt")

yes = "magic"
no = "not magic"

square = []
for i in range(4):
    square.append([int(x) for x in input().split()])

total = sum(square[0])
magic = True
for i in square:
    if not magic:
        break
    if sum(i) != total:
        magic = False

for i in range(4):
    if not magic:
        break
    suma = 0
    for j in range(4):
        suma += square[j][i]
    if suma != total:
        magic = False

if magic:
    print(yes)
else:
    print(no)
