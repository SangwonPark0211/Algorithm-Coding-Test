# https://www.acmicpc.net/problem/9935

s = input()
bomb = input()
last_char = bomb[-1]
bomb_len = len(bomb)
st = []
for i in range(len(s)):
    st.append(s[i])
    if st[-1]==last_char and ''.join(st[(-1)*bomb_len:]) == bomb:
        # st = st[:(-1)*bomb_len]
        del st[(-1)*bomb_len:]
if not st:
    print("FRULA")
else:
    print(''.join(st))