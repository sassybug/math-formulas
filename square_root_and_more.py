

def square_root(number):
    if number < 0:
        print("sorry will not work")
        exit(0)
    x = 1
    while x ** 2 <= number:
        x = x + 1
    whole_num = x - 1
    decimal = 0
    while (whole_num + decimal) ** 2 <= number:
        decimal = decimal + 0.1
    real_decimal = decimal - 0.1
    almost_answer = real_decimal + whole_num
    decimal_2 = 0
    while (almost_answer + decimal_2) ** 2 <= number:
        decimal_2 = decimal_2 + 0.01
    real_decimal_2 = decimal_2 - 0.01
    answer = almost_answer + real_decimal_2
    decimal_3 = 0
    while (answer + decimal_3) ** 2 <= number:
        decimal_3 = decimal_3 + 0.001
    real_decimal_3 = decimal_3 - 0.001
    answer_1 = answer + real_decimal_3
    rounded_answer = round(answer_1, 3)
    return rounded_answer


def cube_root(number):
    if number < 0:
        print("sorry will not work")
        exit(0)
    if number == 0:
        print(0)
        exit(0)
    x = 1
    while x ** 3 <= number:
        x = x + 1
    whole_num = x-1
    decimal = 0
    while (whole_num+decimal)**3 <= number:
        decimal = decimal + 0.1
    real_decimal = decimal - 0.1
    almost_answer = real_decimal + whole_num
    decimal_2 = 0
    while(almost_answer+decimal_2)**3 <= number:
        decimal_2 = decimal_2 + 0.01
    real_decimal_2 = decimal_2 - 0.01
    answer = almost_answer + real_decimal_2
    decimal_3 = 0
    while(answer+decimal_3)**3 <= number:
        decimal_3 = decimal_3 + 0.001
    real_decimal_3 = decimal_3 - 0.001
    answer_1 = answer + real_decimal_3
    t = 0
    while t <= 10:
        answer_1 = answer_1 - (((answer_1 ** 3) - number) / (3 * (answer_1 ** 2)))
        t = t + 1
    return answer_1


def fourth_root(number):
    if number < 0:
        print("sorry will not work")
        exit(0)
    x = 1
    while x ** 4 <= number:
        x = x + 1
    whole_num = x-1
    decimal = 0
    while (whole_num+decimal)**4 <= number:
        decimal = decimal + 0.1
    real_decimal = decimal - 0.1
    almost_answer = real_decimal + whole_num
    decimal_2 = 0
    while(almost_answer+decimal_2)**4 <= number:
        decimal_2 = decimal_2 + 0.01
    real_decimal_2 = decimal_2 - 0.01
    answer = almost_answer + real_decimal_2
    decimal_3 = 0
    while(answer+decimal_3)**4 <= number:
        decimal_3 = decimal_3 + 0.001
    real_decimal_3 = decimal_3 - 0.001
    answer_1 = answer + real_decimal_3
    rounded_answer = round(answer_1,3)
    return rounded_answer
print(cube_root(257.6))
