T = int(input())

for i in range(T):
    N, K = map(int, input().split())

    total_person = N + 1

    if K >= total_person:
        print("YES")
    else:
        print("NO")