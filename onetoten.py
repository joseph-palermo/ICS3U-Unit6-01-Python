#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: December 2019
# This program adds 10 random numbers to an array and calculates the average

import random


def main():
    # this function adds 10 numbers to an array and calculates the average

    # variables & arrays
    array_of_numbers = []
    average = 0

    # process
    try:
        print("Your random numbers are: ")
        for counter in range(0, 10):
            number = random.randint(1, 100)
            array_of_numbers.append(number)
            print(array_of_numbers[counter])

        for counter in range(0, 10):
            average = array_of_numbers[counter] + average
        average = (average/10)

    # output
        print("The average is: {0}".format(average))
    except (ValueError):
        print("Something went wrong, please try again")


if __name__ == "__main__":
    main()
