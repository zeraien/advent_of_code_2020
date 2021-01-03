#part 1
found_invalid = False
with open('input.txt') as file:
    lines = [int(x) for x in file.readlines()]

def is_valid_number(index, list):
    preamble = list[index-25:index]
    is_found = False
    for i in preamble:
        for y in preamble:
            if i + y == list[index]:
                is_found = True
    return is_found

for i in range(0, len(lines)-1):
    if i > 24 and found_invalid == False:
        if not is_valid_number(i, lines):
            found_invalid = lines[i]

print(found_invalid)

#part 2
done = False
for i in range(0, len(lines)-1):
    l = []
    if not done:
        for y in range(i, len(lines)-1):
            if sum(l) > found_invalid:
                break
            if sum(l) == found_invalid:
                minimum = min(l)
                maximum = max(l)
                print('{0} + {1} = {2}'.format(minimum, maximum, minimum + maximum))
                done = True
                break
            else:
                l.append(lines[y])
