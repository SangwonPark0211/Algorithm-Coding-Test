# https://www.acmicpc.net/problem/4949

s = input()
op, cl = ['[','('], [']',')'] 
while s != '.':
    st = []
    flag = 0
    for i in s:
        if i in op:
            st.append(i)
        elif i in cl:
            if not st or ((st[-1],i) not in zip(op,cl)):
                print("no")
                flag = 1
                break
            elif (st[-1],i) in zip(op,cl):
                st.pop()

    if not st and flag==0:
        print("yes")
    if st and flag==0:
        print('no')
    s = input()

