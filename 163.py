def append_and_display(filename, text):
    # append the text to the file
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text + "\n")

    # read and display updated contents
    with open(filename, "r", encoding="utf-8") as file:
        print("Updated file content:\n")
        print(file.read())


if __name__ == "__main__":
    # ask for filename (use example.txt by default)
    filename = input("Enter filename to append to (press Enter for 'example.txt'): ").strip() or "example.txt"
    text = input("Enter text to append:")
    append_and_display(filename, text)