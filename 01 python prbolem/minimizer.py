N = int(input())
A = list(map(int, input().split()))

operations = 0
all_even = True

while all_even:
    for num in A:
        if num % 2 != 0:
            all_even = False
            break

    if all_even:
        operations += 1
        A = [num // 2 for num in A]

print(operations)
