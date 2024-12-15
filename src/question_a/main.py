from question_a import get_most_likely_ancestor_consensus

def main():
    """
    Main program loop to interact with the user.
    """
    while True:
        dna_string1 = input("Enter a DNA string (9-16 characters): ").strip().upper()
        if not (8 < len(dna_string1) <= 16):
            print("Invalid input. DNA string must be greater than 8 characters and less than or equal to 16 characters.")
            continue

        dna_string2 = input("Enter a DNA substring (exactly 4 characters): ").strip().upper()
        if len(dna_string2) != 4:
            print("Invalid input. DNA substring must be exactly 4 characters.")
            continue

        positions = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
        if positions:
            print("The substring is found at positions:", *positions)
        else:
            print("The substring was not found in the DNA string.")

        continue_choice = input("Do you want to try again? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            break

if __name__ == "__main__":
    main()