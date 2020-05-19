def trim(s):
    j = 0
    k = 1
    for i in s:
        print('front: ' + i)
        if i == ' ':
            j = j+1
        else:
            break
    while s[-k] == ' ':
        print('end: ' + s[-k])
        k = k+1
    print(j, k)
    s = s[j:-k+1]
    return s

print(trim('    hello     '))
