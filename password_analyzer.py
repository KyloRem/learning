#Password Strength Analyzer
print("Password Strength Analyzer")
print("-" * 25)

# Get Password from user
password = input("Enter a password to analyze: ")
print(f"Analyzing password: {'*' * len(password)}") # Hide the actual password


# Check password length
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


# Check character types
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


# DEBUG CODE
# print(f"\nDebug info:")
# print(f"Length >= 8: {length >= 8}")
# print(f"Length >= 12: {length >= 12}")
# print(f"Has uppercase: {has_uppercase}")
# print(f"Has lowercase: {has_lowercase}")
# print(f"Has numbers: {has_numbers}")
# print(f"Has symbols: {has_symbols}")


# Calculate an overall strength score
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