
list1 = ["item1", "item2", "item3", "item4"]

list2 = [(x, y) for x in list1 for y in range(1, 10)]
print list2

add = lambda x, y: x+y
sub = lambda x, y: x-y
mul = lambda x, y: x*y
div = lambda x, y: x/y

print("addition: {0}".format(add(2, 3)))
print("subtraction: {0}".format(sub(2, 3)))
print("multiplication: {0}".format(mul(2, 3)))
print("division: {0}".format(div(2, 3)))


"""
for x in list1:
    for y in range(1, 10):
        print(x, y)
"""

