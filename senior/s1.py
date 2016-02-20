one = sorted(list(input()), reverse=True)
two = sorted(list(input()), reverse=True)

success = True
while success:
    if one[0] != "*":
        if one[0] in two:
            two.pop(two.index(one[0]))
            one.pop(0)
        else:
            if "*" in two:
                two.pop(two.index("*"))
                one.pop(0)
            else:
                success = False
    else:
        one.pop(0)
        two.pop(0)
    if not one:
        break

if success:
    print("A")
else:
    print("N")
