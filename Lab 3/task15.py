def main():
    password = input("Enter a password: ")
    
    if len(password) < 6 or len(password) > 16:
        print("Password must be between 6 and 16 characters")
        return
    
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in "$#@":
            has_special = True
    
    if has_lower and has_upper and has_digit and has_special:
        print("Valid password")
    else:
        print("Invalid password")
        
main()
