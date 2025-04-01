#Ex-1
'''
def is_prime(n):                                            #defines what a prime number actually is
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = []                                          #gives a range of numbers to loooks through, then checks if they're prime or not
for num in range(1, 101):
    if is_prime(num):
        prime_numbers.append(num)

print("Prime numbers between 1 and 100:")                   #displayes all prime numbers
print(prime_numbers)
'''

#Ex-2 
'''
sentence = input("Enter a sentence: ")              # gets teh input from user

words = sentence.lower().split()

# empty dictionary
word_frequency = {}

#s count word frequencie
for word in words:

    word = word.strip(".,!?")
    
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1


print("\nWord frequencies:")
for word, count in word_frequency.items():           # displays the results
    print(f"{word}: {count}")
'''

#Ex-3
'''
r1 = [3, 4, 6]
r2 = [3, 6, 8]
r3 = [7, 9, 2]

row1_sum = sum(r1)
row2_sum = sum(r2)
row3_sum = sum(r3)
print("Row 1:", r1, "Sum:", row1_sum)
print("Row 2:", r2, "Sum:", row2_sum)
print("Row 3:", r3, "Sum:", row3_sum)
total_sum = row1_sum + row2_sum + row3_sum
print("total sum of all Rows:", total_sum)
'''








