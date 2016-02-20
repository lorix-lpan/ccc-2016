players = []
for i in range(6):
    players.append(input())

count = 0
for i in players:
    if i == "W":
        count += 1

if count == 5 or count == 6:
    print(1)
elif count == 3 or count == 4:
    print(2)
elif count == 1 or count == 2:
    print(3)
else:
    print(-1)
        
