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

print(fact(10))
print(datetime.datetime.now() - start)


