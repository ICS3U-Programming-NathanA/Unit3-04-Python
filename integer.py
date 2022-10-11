#!/usr/bin/env python3
# Created by: Nathan Araujo
# Created on: Oct 11 2022
# This program asks the user for a integer it then tells them if its positive, negative or zero


def main():
    # Get the the integer from the user
    user_num = int(input("Enter a integer: "))

    # An if statement to see if the users integer is positive, negative or zero
    if user_num >= 1:
        print("Your number is positive")
    elif user_num <= -1:
        print("Your number is negative")
    else:
        print("Your number is zero")


if __name__ == "__main__":
    main()
