from question_b import create_multiplication_table, display_multiplication_table

def main():
    while True:

        size = int(input("Enter the size of the multiplication table: "))
        
        multiplication_table = create_multiplication_table(size)

        display_multiplication_table(multiplication_table)
        
        continue_prompt = input("Do you want to create another multiplication table? (yes/no): ").strip().lower()
        if continue_prompt != 'yes':
            break

if __name__ == "__main__":
    main()
