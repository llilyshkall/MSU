import itertools as it


def LookSay():
    s = '1'
    while True:
        for item in s:
            yield int(item)
        s = "".join([str(len(list(l))) + str(k) for k, l in it.groupby(s)])
        # print(s)


# for i, l in enumerate(LookSay()):
#      print(f"{i}: {l}")
#      if i > 10:
#          break
