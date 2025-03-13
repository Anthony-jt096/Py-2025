"""
#Ex-1
leap_year = int(input("Enter a year: "))
if leap_year % 4 == 0 and leap_year % 100 != 0 or leap_year % 400 == 0: #in english, this basically means: "the entered year IS a leap year if its divisable by 4, but is NOT divisible by 100, OR if its divisible by 400"
    print("This IS a leap year.")
else:
    print("this is NOT a leap year.")
"""

#Ex-2
'''
age_group = ["toddler", "child", "teenager", "adult", "senior"]         # always use a list for multiple variables for simplicity, unless speficic conditions need to be addressed. 
age = int(input("Enter an age: "))                          # remember to use 'int(input(""))' any time you use numbers.
if age <= 3:
    result = age_group[0]                           # using the list, itll be more orginized to sort the age groups.
elif age <= 12:
    result = age_group[1]
elif age <= 19:
    result = age_group[2]
elif age <= 59:
    result = age_group[3]
elif age >= 60:                                     # remember that '>=' is always used at the end of an integer if-else because if anything is bigger than the last list item, then itll be consitered a 'senior' for example, in this program, unless speficied.
    result = age_group[4]

print(f"A person aged {age} is classified as: {result}")
'''

#Ex-3 
'''
even_num = []                                   #  --- creates empty lists for the upcoming variables
odd_num = []
numbers = []

for i in range(5):                              #  --- user enteres 5 numbers, and adds them to the empty 'numbers' list
    num = int(input("Enter 5 numbers: "))
    numbers.append(num)

for num in numbers:                             #  --- program checks if the number is disivable by 2 since its an even digit, if true, then itll add it (using .append) to the emtpy 'even_num' list, otherwise itll add it to the empty 'odd_num' list.
    if num % 2 == 0:
        even_num.append(num)
    else:
        odd_num.append(num)

sum_even = sum(even_num)                        #  --- converts variables
sum_odd = sum(odd_num)

print(f"even numbers = {even_num}")             #  --- displays the even and odd numbers to console, and adds the sum of both
print(f"odd numbers = {odd_num}")
total_sum = sum_even + sum_odd
print(f"sum of both: {total_sum}")
'''


