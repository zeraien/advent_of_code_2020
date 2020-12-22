# import math

# #part 1

    
# highest = 0
# seat_id = 0
# with open("input.txt", "r") as f:
#     for l in f:
#         rows = [x for x in range(0, 128)]
#         columns = [x for x in range(0, 8)]
#         for i in range(0, len(l)):
#             if i <= 6:
#                 if l[i] == 'F':
#                     rows = rows[:math.ceil(len(rows)/2)]
#                 else:
#                     rows = rows[math.floor(len(rows)/2):]
#             elif i <= 9:
#                 if l[i] == 'L':
#                     columns = columns[:math.ceil(len(columns)/2)]
#                 else:
#                     columns = columns[math.floor(len(columns)/2):]
#         r = rows[0]
#         c = columns[0]
#         seat_id = r * 8 + c
#         if seat_id > highest:
#             highest = seat_id

# print(highest)

import math

#part 2

all_sets = []
highest = 0
seat_id = 0
with open("input.txt", "r") as f:
    for l in f:
        rows = [x for x in range(0, 128)]
        columns = [x for x in range(0, 8)]
        for i in range(0, len(l)):
            if i <= 6:
                if l[i] == 'F':
                    rows = rows[:math.ceil(len(rows)/2)]
                else:
                    rows = rows[math.floor(len(rows)/2):]
            elif i <= 9:
                if l[i] == 'L':
                    columns = columns[:math.ceil(len(columns)/2)]
                else:
                    columns = columns[math.floor(len(columns)/2):]
        r = rows[0]
        c = columns[0]
        seat_id = r * 8 + c
        all_sets.append(int(seat_id))

for i in range(2, 890):
    if not i in all_sets:
        if i+1 in all_sets:
            if i - 1 in all_sets:
                print(i)
    

# # a = all_sets[1:-2]
# # b = potential
# # found = []
# # for i in range(0, len(a) -1):
# #     if a[i] != b[i] and found == []:
# #         found.append(a[i-1])
# # print(found)