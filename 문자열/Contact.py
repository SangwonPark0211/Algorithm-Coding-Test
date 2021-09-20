# https://www.acmicpc.net/problem/1013

import re

T = int(input())
for _ in range(T):
    a = input()
    p = re.compile('(100+1+|01)+')
    # p.match를 사용하면 안됨. 이 경우 처음부터 끝까지 문자열이 일치해야 하지만, p.match의 경우 부분적으로 일치하는 문자열이 있으면 True return
    m = p.fullmatch(a)
    if m:
        print("YES")
    else:
        print("NO")
