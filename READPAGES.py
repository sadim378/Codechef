T = int(input())

for i in range(T):
    N, X, Y = map(int, input().split())

    total = X * Y

    if total >= N:
        print("YES")
    else:
        print("NO")