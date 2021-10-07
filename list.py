# Basic List Operations
# len()
length_list = [1, 2, 3, 4, 5]

list_length = len(length_list)
print("There are", list_length, "numbers in this list")

# append()
append_list = [6, 7, 8, 9]

append_list.append(10)
print(append_list)

# insert()
insert_list = [11, 13, 14, 15]

insert_list.insert(1, 12)
print(insert_list)

# pop()
pop_list = [16, 17, 21, 18, 19, 20, 67]

popped_item = pop_list.pop()
print("Removed", popped_item)
print(pop_list)

second_popped_item = pop_list.pop(2)
print("Removed", second_popped_item)
print(pop_list)

# Numerical List Operations
# sum(numeric_list)
num_list = [21, 22, 23, 24, 25]
num_sums = sum(num_list)
print("The total of all the numbers is", num_sums)

# min() and max()
num_list2 = [26, 27, 28, 29, 30]
print("The highest number is", max(num_list2))
print("The lowest number is", min(num_list2))