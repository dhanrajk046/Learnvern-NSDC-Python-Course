filename = "fruits.txt"  # fixed filename (was 'ffruits.txt')

try:
    with open(filename, "r", encoding="utf-8") as file:
        fruits = [line.strip() for line in file]
    print("List read from file:", fruits)
except FileNotFoundError:
    print(f"File not found: {filename}")                                                                                                                