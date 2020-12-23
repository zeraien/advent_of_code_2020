

try:
    with open('input.txt') as x:
        for num_a in x:
            with open('input.txt') as y:
                for num_b in y:
                    with open('input.txt') as z:
                        for num_c in z:
                            if int(num_a) + int(num_b) + int(num_c) == 2020:
                                print(int(num_a) * int(num_b) * int(num_c))

except ValueError:
    print('done')