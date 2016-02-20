start = [int(x) for x in input().split(":")]

time = start[0] * 6 + int(start[1]/10)

def to_time(num):
    hour = int(num/6)
    mins = int((num % 6) * 10)
    if hour < 10:
        hour = "0" + str(hour)
    if mins == 0:
        mins = "00"
    return str(hour) + ":" + str(mins)

total = 12

while total != 0:
    if (time >= 42 and time < 60) or (time >= 90 and time < 114):
        time += 2
        total -= 1
    else:
        time += 1
        total -= 1

if time >= 144:
    time = time - 144
print(to_time(time))