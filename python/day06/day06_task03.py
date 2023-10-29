ways = {}
enter = ""
exit = ""
while s := input():
    s = s.split(' ')
    if len(s) == 1:
        if enter == "":
            enter = s[0]
        else:
            exit = s[0]
            break
    else:
        if s[0] in ways:
            ways[s[0]].add(s[1])
        else:
            ways[s[0]] = {s[1]}
        if s[1] in ways:
            ways[s[1]].add(s[0])
        else:
            ways[s[1]] = {s[0]}

avalible = {enter}
count = 0
while count != len(avalible) and exit not in avalible:
    count = len(avalible)
    for key in ways.keys():
        if key in avalible:
            avalible.update(ways[key])

if exit in avalible:
    print("YES")
else:
    print("NO")
