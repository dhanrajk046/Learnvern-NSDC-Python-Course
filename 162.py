def read_first_n_lines(file_name, n):
    """Print the first n lines of file_name. Handles file-not-found and basic errors."""
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for _ in range(n):
                line = file.readline()
                if not line:                                                                                                                                                   
                    break
                print(line.rstrip())
    except FileNotFoundError:
        print(f"The file {file_name} was not found. Please check the file name and try again.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")


if __name__ == "__main__":
    # default file name (change as needed)
    file_name = "example.txt"

    # get number of lines to read from user, with validation
    try:
        n = int(input("Enter number of lines to read: "))
        if n < 0:
            raise ValueError("Number of lines must be non-negative")
    except ValueError as ve:
        print(f"Invalid number: {ve}")
    else:
        read_first_n_lines(file_name, n)