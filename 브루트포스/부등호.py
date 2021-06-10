# https://www.acmicpc.net/problem/2529
"""
1st version
"""
from itertools import permutations

k = int(input())
order = input().split()
minimum, maximum = '9876543210', '0'
arr = [i for i in range(10)]
for num in permutations(arr, k+1):
    flag = 0
    for i in range(len(num)-1):
        if (order[i] == '<' and num[i] > num[i+1]) or (order[i] == '>' and num[i] < num[i+1]):
            flag = 1
            break
    if flag == 0:
        if int(minimum) > int(''.join(list(map(str, num)))):
            minimum = ''.join(list(map(str, num)))
        if int(maximum) < int(''.join(list(map(str, num)))):
            maximum = ''.join(list(map(str, num)))
print(maximum)
print(minimum)

"""
2nd version
"""
# num = int(input())
# op = input().split()
# check = [False] * 10
# mx , mn = "",""
# def poss(i,j,k): # 부등호 조건이  만족할 때만 작동
#     if k == ">":
#         return i>j
#     else:
#         return i<j


# def recu(cnt, s):
#     global mx,mn
#     if cnt > num: #맨처음 나타나는 값이 최소, 마지막 저장되는 것이 최대
#         if len(mn) == 0:
#             mn = s
#         else:
#             mx = s
#         return
#     for i in range(10): #재귀 함수
#         if check[i] == False:
#             if cnt == 0 or poss(s[-1],str(i),op[cnt-1]):
#                 check[i] = True
#                 recu(cnt+1,s+str(i))
#                 check[i] = False

# recu(0,"")
# print(mx)
# print(mn)
        
    