T = int(input())

for _ in range(T):
    N = int(input())
    digits = str(N)[::-1]
    print(' '.join(digits))