# Take a number as input from the user
num = int(input("Enter a number: "))

# sum_digits will store the total sum of all digits
sum_digits = 0

# temp is a copy of num, so we don't change the original number
temp = num

# Loop runs until temp becomes 0 (means no digits are left)
while temp > 0:
    # Get the last digit of the number
    digit = temp % 10
    
    # Add that digit to the sum
    sum_digits += digit
    
    # Remove the last digit from temp
    temp //= 10

# Print the final result
print("Sum of digits =", sum_digits)
