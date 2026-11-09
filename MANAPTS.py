T = int(input())

for i in range(T):
    X, Y = map(int, input().split())

    attacks = Y // X

    print(attacks)