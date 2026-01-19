fruits = ["Apple", "Mango", "Orange"]
filename = "fruits.txt"
with open(filename, "w", encoding="utf-8") as file:
    for fruit in fruits:
        file.write(fruit + "\n")

print(f"List stored successfully in {filename}")