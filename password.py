@@ -0,0 +1,36 @@
import re

def check_password_strength(password):
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1

    # Lowercase letter
    if re.search(r"[a-z]", password):
        score += 1

    # Uppercase letter
    if re.search(r"[A-Z]", password):
        score += 1

    # Numbers
    if re.search(r"[0-9]", password):
        score += 1

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Final result
    if score == 5:
        return "Excellent Password 💪🔥"
    elif score >= 3:
        return "Moderate Password 🙂"
    else:
        return "Weak Password ⚠️"

# Program starts here
password = input("Enter your password: ")
print(check_password_strength(password))
print(check_password_strength(password))
