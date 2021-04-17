# https://www.acmicpc.net/problem/1700

n, k = list(map(int, input().split()))
kind = list(map(int, input().split()))
plug = []
cnt = 0
for i in range(k):
    if len(plug)<n and kind[i] not in plug:
        plug.append(kind[i])
    elif kind[i] in plug:
        continue
    else:
        tmp = []
        for j in range(len(plug)):
            try:
                tmp.append(kind[i:].index(plug[j]))
            except:
                tmp.append(101)
        idx_out = tmp.index(max(tmp))
        del plug[idx_out]
        plug.append(kind[i])
        cnt += 1

print(cnt)

        