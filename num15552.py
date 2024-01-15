import sys
T = sys.stdin.readline()
print(T)
print(int(T))
for i in range(int(T)):
    A, B = map(int, sys.stdin.readline().split())
    print("A,B", A, B)
    print("A+B", A+B)