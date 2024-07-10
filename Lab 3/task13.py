def main():
    binary_numbers = input("Enter a sequence of comma separated 4 digit binary numbers: ")
    binary_numbers = binary_numbers.split(',')
    
    for binary_number in binary_numbers:
        decimal_number = int(binary_number, 2)
        
        if decimal_number % 5 == 0:
            print(binary_number, end=', ')

main()
