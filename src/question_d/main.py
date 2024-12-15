from question_d import get_stock_list, display_stock_history

def main():
    
    stock_list = get_stock_list()

    while True:
        print("\nMenu:")
        print("1 - Display stock purchase history")
        print("2 - Exit")
        
        choice = input("Please select an option (1 or 2): ")
        
        if choice == '1':
            display_stock_history(stock_list)
        elif choice == '2':
            break
        else:
            print("Invalid choice. Select 1 or 2.")

if __name__ == "__main__":
    main()