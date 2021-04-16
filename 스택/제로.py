# https://www.acmicpc.net/problem/10773

n = int(input())
st = []
for _ in range(n):
    x = int(input())
    if x==0:
        st.pop()
    else:
        st.append(x)
if not st:
    print(0)
else:
    print(sum(st))