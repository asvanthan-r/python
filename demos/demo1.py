my_list = [7, 3.14, True, "Hello", [1,2,4]]
print(my_list)

print(my_list[0])
print(my_list[-1])
print(my_list[4][2])
print(my_list[1:4])

print(my_list[:3])
print(my_list[2:])

my_list.append(1)
print(my_list)

my_list.insert(1,"d")
print(my_list)

my_list.extend([1,2,2])
print(my_list)

my_list.remove('Hello')
print(my_list)

remove_element = my_list.pop(1)
print(remove_element)
print(my_list)

del my_list[1]
print(my_list)