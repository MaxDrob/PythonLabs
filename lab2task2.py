# numbers

param = "string" + str(15)
print("task 1", param)



n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = float(n1) + float(n2)
print(n1 + " plus " + n2 + " = ", n3)


a = 1/3
print("a =", a)
print("{:7.3f}".format(a))

a = 2/3
b = 2/9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))


#  lists

list1 = [82,8,23,97,92,44,17,39,11,12]
print(dir(list))
help(list.insert)
help(list.append)
help(list.sort)
help(list.remove)
help(list.reverse)

print(list1)  # adding by index
list1[0] = 67
print(list1)
list1.append(2)  # adding new element into the end of the list
print(list1)
list1.insert(3, 3)  # insert a value in the desired place of the list
print(list1)
list1.remove(2)  # Remove first occurrence of value
print(list1)
del list1[5]  # removing by place in the list
print(list1)
list1.pop()   # removing the last value in the list
print(list1)


# sorting

list1.sort()
list2 = sorted(list1)
print("Sorted list", list2)
