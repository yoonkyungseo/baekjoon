N, M = map(int, input().split())
b_ball = [n for n in range(1, N+1)]
for m in range(M):
    i, j = map(int, input().split())
    a = b_ball[i-1]
    b_ball[i-1] = b_ball[j-1]
    b_ball[j-1] = a
    
for k in b_ball:
    print(k, end=" ")