# part 1
# found = 0
# for i in open('input.txt'):
#     rule, letter, password = i.replace(':','').replace('\n','').split(' ')
#     rule_min, rule_max = [int(x) for x in rule.split('-')]
#     if rule_min <= password.count(letter) <= rule_max:
#         found += 1
# print(found)

# part 2
found = 0
for i in open('input.txt'):
    rule, letter, password = i.replace(':','').replace('\n','').split(' ')
    rule_min, rule_max = [int(x)-1 for x in rule.split('-')]
    try:
        if password[rule_min] == letter and password[rule_max] != letter:
            found += 1
        if password[rule_min] != letter and password[rule_max] == letter:
            found += 1
    except:
        pass
    
print(found)