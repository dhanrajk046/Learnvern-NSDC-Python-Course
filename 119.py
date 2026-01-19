user_input = input("Enter elements of the list seperated by spaces: ")
my_list = user_input.split()
print("Alternate elements of the list are:")
for i in range(0,len(my_list),2):
    print(my_list[i])
                                                                  