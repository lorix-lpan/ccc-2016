# f = open("./test/j5.txt", "r")

TYPE = int(input())
num = int(input())

def max_speed(arr1, arr2):
    total = 0

    for i in range(num):
        if arr1[i] < arr2[i]:
            total += arr2[i]
        else:
            total += arr1[i]

    return total

dmo = [int(x) for x in input().split()]
peg = [int(x) for x in input().split()]

if TYPE == 1:
    dmo = sorted(dmo, reverse=True)
    peg = sorted(peg, reverse=True)
    print(max_speed(dmo, peg))
else:
    dmo = sorted(dmo, reverse=True)
    peg = sorted(peg)
    print(max_speed(dmo, peg))
