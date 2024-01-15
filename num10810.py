N, M = map(int, input().split())
num = [0 for n in range(N)]


for m in range(M):
    i, j, k = map(int, input().split())
    for b in range(i-1, j):
        num[b] = k

for u in num:
    print(u, end=" ")