# https://www.acmicpc.net/problem/1259

while True:
    a = input()
    if a == '0':
        break
    l, r = 0, len(a)-1
    while l<r:
        if a[l]!=a[r]:
            print("no")
            break
        else:
            l += 1
            r -= 1
    if l>=r:
        print("yes")
