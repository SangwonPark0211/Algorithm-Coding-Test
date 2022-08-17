# https://www.acmicpc.net/problem/16724

def makeGraph(arr):
    link = [[] for _ in range(len(arr)*len(arr[0]))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            curNode = i*len(arr[0])+j
            if arr[i][j]=='U':
                toNode = (i-1)*len(arr[0])+j
            elif arr[i][j]=='D':
                pass
            elif arr[i][j]=='L':
                pass
            elif arr[i][j]=='R':
                pass
    return link