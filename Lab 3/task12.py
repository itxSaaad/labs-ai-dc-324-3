def main():
    lines = []
    
    while True:
        line = input("Enter a line: ")
        
        if line == "":
            break
        
        lines.append(line)
    
    for line in lines:
        print(line.lower())
        
main()