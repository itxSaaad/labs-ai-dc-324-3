def main():
    string = input("Enter a string: ")
    
    letters = 0
    digits = 0
    
    for char in string:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
    
    print(f"Letters {letters}")
    print(f"Digits {digits}")
    
main()
