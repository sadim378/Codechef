t = int(input())

for i in range(t):
    x, N = map(int, input().split())

    each = x // 10
    score = each * N

    print(score)