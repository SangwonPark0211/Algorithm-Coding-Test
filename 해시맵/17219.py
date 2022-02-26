# https://www.acmicpc.net/problem/17219
import sys

site_pw = {}
M, N = map(int, sys.stdin.readline().split())
for _ in range(M):
    site, pw = sys.stdin.readline().split()
    site_pw[site] = pw
for _ in range(N):
    to_find = sys.stdin.readline().strip()
    print(site_pw[to_find])