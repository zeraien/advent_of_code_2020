
#part 1
# yes_sum = 0
# with open("input.txt", "r") as f:
#     yeses = {''}
#     for l in f:
#         if l == '\n':
#             yes_sum += len(yeses) - 1
#             yeses = {''}
#         else:
#             for i in l:
#                 if i != '\n':
#                     yeses.add(i)
# print(yes_sum)


#part 2
from collections import Counter
yes_consensus = 0
with open("input.txt", "r") as f:
    yeses = []
    group_total = 0
    for l in f:
        if l == '\n':
            yes_consensus += len([x for x in Counter(yeses).values() if x == group_total])
            yeses = []
            group_total = 0
        else:
            group_total += 1
            for i in l:
                if i != '\n':
                    yeses.append(i)
print(yes_consensus)