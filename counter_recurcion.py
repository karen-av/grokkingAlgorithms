def sum_el(l):
    if len(l) == 1:
        return 1
    del l[0]
    return 1 + sum_el(l)

x = [1,3,4,5,6,7]
print(sum_el(x))


def max_dig(l):
    l = l
    if len(l) == 1:
        return l[0]
    return l[0] if l[0] > max_dig(l[1:]) else max_dig(l[1:])

l = '123458352'
print(max_dig(l))

x = [1,2,3,4,5]
x.pop(0)
print(x)


def bin_serch(l, c):
    #print(l)
    if len(l) == 1:
        if int(l[0]) == c:
            return True
        return False
    #print(f'c - {int(l[len(l) // 2])}')
    if c >= int(l[len(l) // 2]):
        return bin_serch(l[len(l) // 2:], c)
    return bin_serch(l[:(len(l)) // 2], c)


l = '123456789'
c = 7
print(bin_serch(l,c))

def fast_serch(arr):
    if len(arr) < 2:
        return arr
    else:
        point = arr[0]
        left = [i for i in arr[1:] if i <= point]
        rigth = [i for i in arr[1:] if i > point]
        return fast_serch(left) + [point] + fast_serch(rigth)

x = [4,1,2,4,23,7,4,5,3]
print('fast_serch')
print(fast_serch(x))
