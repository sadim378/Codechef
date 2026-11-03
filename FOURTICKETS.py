T = int(input())

for i in range(T):
    x = int(input())

    total = 4 * x

    if total <= 1000:
        print("YES")
    else:
        print("NO")