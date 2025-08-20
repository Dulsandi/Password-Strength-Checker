import re

def check_password_strength(password):
    # Check the length of the password
    length_error = len(password) < 8

    # Check if it contains at least one uppercase letter
    uppercase_error = not re.search(r"[A-Z]", password)

    # Check if it contains at least one lowercase letter
    lowercase_error = not re.search(r"[a-z]", password)

    # Check if it contains at least one digit
    digit_error = not re.search(r"[0-9]", password)

    # Check if it contains at least one special character
    special_char_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    # Collect all errors
    errors = [length_error, uppercase_error, lowercase_error, digit_error, special_char_error]

    # If none of them are errors → strong password
    if not any(errors):
        return "Strong password ✅"
    # If at least 2 errors → weak password
    elif sum(errors) >= 2:
        return "Weak password ❌"
    # Otherwise → medium password
    else:
        return "Medium strength password ⚠️"

# Example usage
if __name__ == "__main__":
    pwd = input("Enter your password: ")
    print(check_password_strength(pwd))






