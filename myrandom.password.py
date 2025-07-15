import string # Import string module to access character sets
import random # Import random module for generating random choices

# Ask the user for the desired password length
length = int(input("Enter desired password length:"))

# combine letters (upper and lower case), digits, and symbols
characters = string.ascii_letters + string.digits + string.punctuation

# Generate a random password of the desired length
password = ''.join(random.choice(characters )for i in range(length))
# Display the generated password
print("Generated password:" , password)