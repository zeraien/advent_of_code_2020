#part 1
# found = 0
# fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:', 'cid:']
# a = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:', 'cid:']
# with open("input.txt", "r") as f:
#     for i in f:
#         if i == '\n':
#             if ((len(a) == 1) and 'cid:' in a) or len(a) == 0:
#                 found +=1
#             a = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:', 'cid:']
#         else:
#             for x in fields:
#                 if x in i:
#                     a.remove(x)
# print(found)

import re
#part 2
found = 0
fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:', 'cid:']
a = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:', 'cid:']
with open("input.txt", "r") as f:
    for i in f:
        if i == "\n":
            if ((len(a) == 1) and 'cid:' in a):
                found +=1
            a = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:', 'cid:']
        else:
            for x in fields:
                if x in i:
                    if x == 'byr:':
                        if 1920 <= int(i[i.index(x)+4:][:4]) <= 2002:
                            a.remove(x)
                    if x == 'iyr:':
                        if 2010 <= int(i[i.index(x)+4:][:4]) <= 2020:
                            a.remove(x)
                    if x == 'eyr:':
                        if 2020 <= int(i[i.index(x)+4:][:4]) <= 2030:
                            a.remove(x)
                    if x == 'hgt:':
                        try:
                            if 'cm' in i:
                                end = i.index('cm')
                                if 150 <= int(i[i.index(x)+4:end]) <= 193:
                                    a.remove(x)
                            elif 'in' in i:
                                end = i.index('in')
                                if 59 <= int(i[i.index(x)+4:end]) <= 76:
                                    a.remove(x)
                        except ValueError:
                            pass
                    if x == 'hcl:':
                        try:
                            color = i[i.index(x)+4:i.index(x)+4+7]
                            if color[0] == "#" and all((c in set('0123456789abcdef')) for c in color[1:]):
                                a.remove(x)
                        except IndexError:
                            pass
                    if x == 'ecl:':
                        if len(re.findall(r"(?=("+'|'.join(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])+r"))",i[i.index(x)+4:])) == 1:
                            a.remove(x)

                    if x == 'pid:':
                        index_at = i.index(x)
                        num = i[index_at+4:index_at+4+9]
                        if all((c in set('0123456789')) for c in num):
                            if not all((c in set('0123456789')) for c in i[index_at+4:index_at+4+10]):
                                a.remove(x)

print(found)