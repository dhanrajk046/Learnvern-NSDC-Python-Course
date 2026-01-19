user_input = input("Enter numbers separated by commas: ")  # e.g., "1,2,3,4,5,6,7,8"
my_tuple = tuple(user_input.split(","))
count = len(my_tuple)
print("The number of elements in the tuple is:", count)