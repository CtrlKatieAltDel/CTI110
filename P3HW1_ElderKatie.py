# Katie Elder
# Date: 03/17/2024
# Program: P3HW1
# Description: This program takes a number grade and determines average and displays the letter grade average. 

# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades
lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

# determine letter grade for average
if average_grade >= 90:
    print('Your grade is: A')
elif average_grade >= 80:
    print('Your grade is: B')
else:
    print('Your grade is: F')

# TO DO: finish this (output results) 
print(f"\n{'Lowest Grade:':<15} {lowest_grade:<5}")
print(f"{'Highest Grade:':<15} {highest_grade:<5}")
print(f"{'Sum of grades:':<15} {sum_of_grades:<5}")
print(f"{'Average grade:':<15} {average_grade:.2f}") 