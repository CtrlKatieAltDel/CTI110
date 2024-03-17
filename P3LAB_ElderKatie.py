# Katie Elder
# Date: 03/17/2024
# Program: P3LAB
# Description: A program that determines whether that year is a leap year or not.

is_leap_year = False
   
input_year = int(input())


if (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 == 0):
    is_leap_year = True

if is_leap_year:
    print(input_year, "- leap year")
else:
    print(input_year, "- not a leap year")