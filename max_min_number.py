def find_max_min(numberlist):
    min_max = []
    mynewlist = [s for s in numberlist if isinstance(s, int)]
    mynewlist.sort()
    if len(mynewlist) > 0:
        if mynewlist[0] == mynewlist[-1]:
            return [mynewlist[0]]
        min_max.append(mynewlist[0])
        min_max.append(mynewlist[-1])

    return min_max

print(find_max_min([1, 2, 3]))