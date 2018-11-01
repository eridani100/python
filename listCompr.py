
lista1 = [ "lukasz", "gosia", "pawel", "jas"]

list = [ (x,y) for x in lista1 for y in range(1,10) ]
print list

add = lambda x,y : x+y
sub = lambda x,y : x-y
mul = lambda x,y : x*y
div = lambda x,y : x/y

print("dodawanie: ".format( add(2,3) ) )