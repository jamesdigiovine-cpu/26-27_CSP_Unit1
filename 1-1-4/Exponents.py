# Variable to hold solution
product = 1

# Get user input and the exponent
base = int(input("What is the base of your problem?"))
exponent = int(input("What is the exponent of your problem?"))

# Write a loop to run exponent
for l in range (exponent):
    product *= base

# Print out solution
print(product)