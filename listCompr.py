
list1 = ["item1", "item2", "item3", "item4"]

list2 = [(x, y) for x in list1 for y in range(1, 10)]
print list

add = lambda x, y: x+y
sub = lambda x, y: x-y
mul = lambda x, y: x*y
div = lambda x, y: x/y

print("addition: ".format(add(2, 3)))
