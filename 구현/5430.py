# https://www.acmicpc.net/problem/5430

from collections import deque

def sol():
    func = input()
    n = int(input())
    arr = input()
    if n==0:
        if 'D' in func:
            print("error")
            return
        else:
            print([])
            return
    arr = list(map(int,arr.strip('[]').split(',')))
    dq = deque(arr)
    is_reverse = False
    for f in func:
        if f == 'R':
            is_reverse = not(is_reverse)
        elif f == 'D':
            if len(dq) == 0:
                print("error")
                return
            else:
                if is_reverse == False:
                    dq.popleft()
                else:
                    dq.pop()

    if is_reverse == True:
        dq.reverse()

    dq = list(map(str,list(dq)))
    print('['+','.join(dq)+']')

for _ in range(int(input())):
    sol()