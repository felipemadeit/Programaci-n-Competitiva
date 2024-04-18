cases = int(input())

for case in range(cases):
    first = input()
    second = input()
    one_string = ''
    one_string += first
    one_string += second
    set_letters = set(one_string)
    if len(set_letters) == 4:
        print(3)
    elif len(set_letters) == 3:
        print(2)
    elif len(set_letters) == 2:
        print(1)
    else:
        print(0)
