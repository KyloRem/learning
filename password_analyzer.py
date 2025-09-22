"""
Password Strength Analyzer
Analyzes password strength based on length and character types.
"""

# Standard library imports
import getpass

#Header
print("Password Strength Analyzer")
print("-" * 25)


# Password Input - hides password input
password = getpass.getpass("Enter a password to analyze: ")


# Check Password Length
print("\nPassword Analysis")
print("=" * 18)

length = len(password)
print(f"Length: {length} characters")

if length < 8:
    print("❌ Too short (minimum 8 characters recommended)")
elif length < 12:
    print("⚠️ Okay length (12+ characters preferred)")
else:
    print("✅ Good length")


# Character checks
# Uses generator expressions and assigns c to each character in the password
# C can be anything
has_uppercase = any(c.isupper() for c in password)
has_lowercase = any(c.islower() for c in password)
has_numbers = any(c.isdigit() for c in password)
has_symbols = any(not c.isalnum() for c in password)

print(f"Uppercase letters: {'✅' if has_uppercase else '❌'}")
print(f"Lowercase letters: {'✅' if has_lowercase else '❌'}")
print(f"Numbers: {'✅' if has_numbers else '❌'}")
print(f'Symbols: {'✅' if has_symbols else '❌'}')


# Calculate Strength Score
## Assigns points for each satisfied condition
## Awards an overall score out of 6
print("\nOverall Strength:")
score = 0

if length >= 8:
    score += 1
    # print(f"After length >= 8: score = {score}")
if length >= 12:
    score += 1
    # print(f"After length >= 12: score = {score}")
if has_uppercase:
    score += 1
    # print(f"After has_uppercase: score = {score}")
if has_lowercase:
    score += 1
    # print(f"After has_lowercase: score = {score}")
if has_numbers:
    score += 1
if has_symbols:
    score += 1
    # print(f"After has_symbols: score = {score}")

print(f"Score: {score}/6")

if score <= 2:
    print("❌ Very weak")
elif score <= 4:
    print("⚠️ Could be better")
elif score >= 5:
    print("✅ Strong password!")

print('=' * 18)