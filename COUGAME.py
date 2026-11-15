T = int(input())

for i in range(T):
    G, B = map(int, input().split())

    remaining = B - G

    print(remaining)