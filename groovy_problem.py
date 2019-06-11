# Author: Dahir Muhammad Dahir
# REGNO: U18CO2044
# Date: 1st-June-2019
# PROBLEM: PROBLEM F (GROOVY NUMBERS)
from math import sqrt


def main():
    while True:
        current_num = int(input())

        if current_num == -1:
            break

        current_num_divisors = get_divisors(current_num)

        is_square_free = True

        for number in current_num_divisors:
            if is_perfect_square(number):
                print("{} is not square-free".format(current_num))
                is_square_free = False
                break

        if is_square_free:
            print("{} is square-free".format(current_num))


def get_divisors(num):
    divisors = []
    for i in range(2, num):
        if num % i == 0:
            divisors.append(i)

    return divisors


def is_perfect_square(num):
    square_root_num = sqrt(num)

    if square_root_num == int(square_root_num):
        return True
    return False


if __name__ == "__main__":
    main()
