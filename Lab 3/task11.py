def create_table(i, j):
    rows = i
    columns = j
    arr = []
    
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(i * j)
        arr.append(row)
        
    return arr

def print_table(table):
    for row in table:
        for cell in row:
            print(cell, end=' ')
        print()

def main():
    # Taking user input for rows and columns
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    
    table = create_table(rows, columns)
    print_table(table)
    
main()
