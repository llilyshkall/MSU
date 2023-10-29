words = {}
while s := input():
    for word in s.split(" "):
        if word != "":
            if word in words:
                words[word] += 1
            else:
                words[word] = 1

countmax = 0
ret = ""
for key in words.keys():
    if words[key] == countmax:
        ret = "---"
    if words[key] > countmax:
        countmax = words[key]
        ret = key

print(ret)
