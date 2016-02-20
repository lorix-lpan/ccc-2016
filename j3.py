def isPal(word):
    # word is a list
    for i in range(int(len(word)/2)):
        if word[i] != word[len(word)-i-1]:
            return False
    return True

word = list(input())

maxim = 1

for i in range(len(word)-2):
    for j in range(i+2, len(word)+1):
        if isPal(word[i:j]) and len(word[i:j]) > maxim:
            maxim = len(word[i:j])

print(maxim)
