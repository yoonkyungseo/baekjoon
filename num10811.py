N, M = map(int, input().split())
a = ""
for n in range(1, N+1):
    a+=str(n)

for i in range(M):
    first, last = map(int, input().split())
    if first == 1:
        a = a[:first-1] + a[last-1::-1] + a[last:]
    else:
        a = a[:first-1] + a[last-1:first-2:-1] + a[last:]

for p in map(int, list(a)):
    print(p, end=" ")