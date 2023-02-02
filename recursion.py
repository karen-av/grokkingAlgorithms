import datetime 


def counter(i):
    print(i)
    if i > 0:
        counter(i-1)
    return True


#print(counter(5))

def fact(x):
    if x == 1:
        return x
    return x * fact(x - 1)
start = datetime.datetime.now()

#print(fact(10))
#print(datetime.datetime.now() - start)




def summ(x):
    if x == 1:
        return x
    return x + summ(x - 1)

#print(summ(100))

def sum(list_x):
    if len(list_x) == 1:
        return int(list_x[0])
    
    return int(list_x[0]) + sum(list_x[1:])

list_x = '123'
k = sum(list_x)
print(k)



