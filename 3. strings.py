# Project 1 — Username Formatter
# Input username:
# •	remove spaces 
# •	convert lowercase
username = input("Enter your username: ")
formatted_username = username.replace(" ", "").lower()
print("Formatted username:", formatted_username)

# Project 2 — Email Validator (basic)
# Check:
# •	contains "@" 
# •	ends with .com 
email = input("Enter your email address: ")
if "@" in email and email.endswith(".com"):
    print("Valid email address.")
else:
    print("Invalid email address.")

# Project 3 — Word Counter
# Input sentence.
# Count characters.
sentence = input("Enter a sentence: ")
count = len(sentence)
print(f"Total characters: {count}")


# Project 4 — String Analyzer
# Input text.
# Print:
# •	uppercase 
# •	lowercase 
# •	length 
# •	reverse 
text = input("Enter text: ")
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Length:", len(text))
print("Reverse:", text[::-1])

