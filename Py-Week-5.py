import math
import random
import datetime
import sys
import csv
import json
import os
#1

'''Radius = float(input('Enter the radius of a circle: ' ))
area = math.pi * pow(Radius, 2)

print(f"The area of the circle is: {round(area, 2)}cm^2")

rand = []  
for _ in range(10):  
    num = random.randint(1, 100)  
    rand.append(num)  

minimum = min(rand)  
maximum = max(rand)  
average = sum(rand) / len(rand)  

print(f"Generated Numbers: {rand}")  
print(f"Minimum: {minimum}")  
print(f"Maximum: {maximum}")  
print(f"Average: {average:.2f}")  
'''

#2     
'''    
from datetime import datetime

birthday = input("Enter your birthday (MM-DD): ")

today = datetime.now()

next_birthday = datetime.strptime(birthday, "%m-%d").replace(year=today.year)
if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)

days_left = (next_birthday - today).days

print(f"Days until your birthday: {days_left}")
'''

#3
'''

def list_contents_with_sizes():
    for item in os.listdir():
        path = os.path.join(os.getcwd(), item)
        if os.path.isfile(path):
            size = os.path.getsize(path)
            print(f"File: {item} | Size: {size} bytes")
        elif os.path.isdir(path):
            dir_size = sum(os.path.getsize(os.path.join(dirpath, f)) 
                          for dirpath, _, files in os.walk(path) 
                          for f in files)
            print(f"Directory: {item} | Size: {dir_size} bytes")

list_contents_with_sizes()


def sum_numbers():
    try:
        numbers = [float(arg) for arg in sys.argv[1:]]
        total = sum(numbers)
        print(f"Sum: {total}")
    except ValueError:
        print("Error: All arguments must be numbers")

sum_numbers()
'''

#4

'''
def display_employees(json_file):
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
            print("Employee Data:\n" + "-"*20)
            for employee in data['employees']:
                print(f"Name: {employee['name']:<15} | Age: {employee['age']}")
    except FileNotFoundError:
        print(f"Error: File '{json_file}' not found")
    except KeyError as e:
        print(f"Error: Invalid JSON structure - missing key {e}")


def display_csv_data(csv_file):
    try:
        with open(csv_file, newline='') as f:
            reader = csv.DictReader(f)
            print("\nCSV Data:\n" + "-"*20)
            for row in reader:
                print(f"Name: {row['name']:<15} | Age: {row['age']} | Department: {row.get('department', 'N/A')}")
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found")
    except KeyError as e:
        print(f"Error: Missing required column {e} in CSV")
'''

'''
import numpy as np


print("Matrix Multiplication")
rows1 = int(input("Enter number of rows for first matrix: "))
cols1 = int(input("Enter number of columns for first matrix: "))
rows2 = int(input("Enter number of rows for second matrix: "))
cols2 = int(input("Enter number of columns for second matrix: "))


A = np.random.randint(1, 10, (rows1, cols1))
B = np.random.randint(1, 10, (rows2, cols2))

print("First matrix (A):")
print(A)
print("Second matrix (B):")
print(B)

if cols1 == rows2:
    C = np.dot(A, B)
    print("Product (A x B):")
    print(C)
else:
    print("Cannot multiply: columns of A must equal rows of B.")

print("\nDeterminant Calculation")
n = int(input("Enter size of square matrix: "))
M = np.random.randint(1, 10, (n, n))
print("Square matrix:")
print(M)
det = np.linalg.det(M)
print("Determinant:", det)

print("\nSolving Linear Systems")
n = int(input("Enter number of equations (n): "))
coeff = np.random.randint(1, 10, (n, n))
const = np.random.randint(1, 10, n)
print("Coefficient matrix:")
print(coeff)
print("Constants vector:")
print(const)
try:
    solution = np.linalg.solve(coeff, const)
    print("Solution:")
    print(solution)
except np.linalg.LinAlgError:
    print("No unique solution (matrix may be singular).")

'''











