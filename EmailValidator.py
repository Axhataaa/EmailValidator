def validate_email(email):
    # Check if at least one lowercase character is present
    if not any(char.islower() for char in email):
        return False

    # Check if at least one uppercase character is present
    if not any(char.isupper() for char in email):
        return False

    # Check if at least one numeric character is present
    if not any(char.isdigit() for char in email):
        return False

    # Check if at least one special symbol is present
    special_symbols = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    if not any(char in special_symbols for char in email):
        return False

    return True


def main():
    while True:
        email = input("Enter your email address: ")
        if validate_email(email):
            print("Valid email address!")
            break  # exit the loop if valid
        else:
            print("Invalid email address. Please try again.\n")


if __name__ == "__main__":
    main()
