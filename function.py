

def fun1(x):
    '''
    Function calculates something
    :param x: value
    :return: multiplication
    '''
    if x < 2:
        return x
    else:
        return x * x


f = fun1
print(fun1(4))

lista = [fun1(x) for x in range(1, 90)]
print(lista)

print(fun1.__doc__)

