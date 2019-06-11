# Author: Dahir Muhammad Dahir
# Date: 1st-June-2019
# PROBLEM: PROBLEM F (GROOVY NUMBERS)

# About: the problem is asking us to find out if a number is square-free [for info on square-free nums
# please refer to the question]
# the solution implement is to check if any of the divisor of the number greater than 1 is a perfect square
# if it is then we know that the number in question is not square-free

from math import sqrt  # we will use this for getting square root of a num


def main():
    # we loop forever since there could be any number of input
    while True:
        current_num = int(input())  # getting the current input 4rm the user or judge

        if current_num == -1:  # if the input is -1 then we know we have reach end of judge input
            break

        if is_square_free(current_num):  # we call the function which check if number is square free
            print("{} is square-free".format(current_num))
        else:
            print("{} is not square-free".format(current_num))


def is_square_free(num):
    for i in range(2, num + 1):  # we exclude 1 since from our range just as the question implies also we exclude the
        if num % i == 0:     # number itself, otherwise every number is square-free
            if is_perfect_square(i):  # we call the function for checking perfect square
                return False

    return True


def is_perfect_square(num):
    square_root_num = sqrt(num)

    if square_root_num == int(square_root_num):  # this check is just specific to python due to the nature of
        return True                              # it's data structure
    return False


if __name__ == "__main__":
    main()
