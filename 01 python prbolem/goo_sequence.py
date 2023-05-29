N = int(input())
a = list(map(int, input().split()))

counter = 0
occurrences = {}

for num in a:
    if num in occurrences:
        occurrences[num] += 1
    else:
        occurrences[num] = 1

for num in a:
    if occurrences[num] > num:
        counter += occurrences[num] - num

print(counter)
