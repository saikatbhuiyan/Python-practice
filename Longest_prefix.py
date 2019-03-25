def prefix(st):
    sz = zip(*st)
    s = ""
    
    for i in sz:
        if len(set(i)) == 1:
            s += i[0]
        else:
            break
    return s

print(prefix(['sami','saikat','sajib']))
