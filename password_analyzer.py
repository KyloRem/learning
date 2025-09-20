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