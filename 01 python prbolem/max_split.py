S = input().strip()

counter = 0
balanced_strings = []
count_L = 0
count_R = 0

for char in S:
    if char == 'L':
        count_L += 1
    else:
        count_R += 1

    if count_L == count_R:
        balanced_strings.append(S[:count_L + count_R])
        S = S[count_L + count_R:]
        count_L = 0
        count_R = 0
        counter += 1

print(counter)
for balanced_string in balanced_strings:
    print(balanced_string)
