# part 1
# trees = 0
# slope = open("input.txt", "r").readlines()
# slope = slope[1:]
# width = len(slope[0]) -1
# x = 3
# for t in slope:
#     if x >= width:
#         x = 0 + (x - width)
#     if t[x] == '#':
#         trees += 1
#     x += 3
# print(trees)

#part 2
result = 1
a = 0
slope = open("input.txt", "r").readlines()
slope = slope[1:]
width = len(slope[0]) -1
for x in [1,3,5,7]:
    i = x
    a = 0
    for t in slope:
        if i >= width:
            i = 0 + (i - width)
        if t[i] == '#':
            a += 1
        i += x
    print('x {0}  = {1}'.format(x, a))
    result = result * a
    

x = 0
a = 0
slope = open("input.txt", "r").readlines()
for i in range(0, len(slope), 2):
        if x >= width:
            x = 0 + (x - width)
        if slope[i][x] == '#':
            a += 1
        x += 1
print(a)
result = result * a

print(result)