def create_multiplication_table(size):
    
    multiplication_table = []
    
    
    for i in range(1, size + 1):
        
        row = []
        for j in range(1, size + 1):
            
            row.append(i * j)
        
        multiplication_table.append(row)
    
    return multiplication_table

def display_multiplication_table(table):
    
    for row in table:
        for value in row:
            print(f"{value:2}", end=" ")  
        print()  

