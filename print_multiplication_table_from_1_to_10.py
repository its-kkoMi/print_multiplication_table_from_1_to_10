# Assignment 5 - Exercise 13
# Print multiplication table from 1 to 10

# Use nested for loop
# Print

for column in range(1, 11):
    for row in range(1, 11):
        print(column * row, end=" ")
    print("\t\t")