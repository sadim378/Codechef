t = int(input())

for i in range(t):
    N, X = map(int, input().split())

    remaining = N - X

    print(remaining)