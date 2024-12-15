from question_c import stock_purchase_history

def main():
    while True:
        print("\nMenu:")
        print("1 - Display stock purchase history")
        print("2 - Exit")
        
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == '1':
            stock_purchase_history()
        elif choice == '2':
            break  
        else:
            print("Invalid choice. Please enter 1 or 2.")

main()