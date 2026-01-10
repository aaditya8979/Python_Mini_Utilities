import re

def check_password_strength(password):
    """
    Check password strength with 5 criteria including special characters.
    Returns: "Weak", "Medium", or "Strong"
    """
    score = 0
    
    # 1. Length ≥ 8
    if len(password) >= 8:
        score += 1
    
    # 2. Uppercase letter
    if re.search(r'[A-Z]', password):
        score += 1
    
    # 3. Lowercase letter  
    if re.search(r'[a-z]', password):
        score += 1
    
    # 4. Digit
    if re.search(r'\d', password):
        score += 1
    
    # 5. Special character (FIXES ISSUE #2)
    if re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]', password):
        score += 1
    
    # Strength classification
    if score <= 2:
        return "Weak"
    elif score <= 3:
        return "Medium" 
    else:
        return "Strong"

def main():
    print("🔐 Password Strength Checker")
    while True:
        pwd = input("\nEnter password (or 'q' to quit): ").strip()
        if pwd.lower() == 'q':
            break
        if pwd:
            strength = check_password_strength(pwd)
            print(f"Strength: {strength}")

if __name__ == "__main__":
    main()
