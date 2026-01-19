my_list=[]
n=int(input("How many numbers you want to add? "))
for i in range(n):
    element=input(f"Enter element {i+1}: ")
    my_list.append(element)
print("The final list is:", my_list)