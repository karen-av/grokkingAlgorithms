
# Проверка есть или нет чиста в списке
def serch_binary(arr, serch_num):
    while len(arr) > 1:
        if serch_num > arr[len(arr) // 2]:
            del arr[0:len(arr) // 2]
        elif serch_num < arr[len(arr) // 2]:
            del arr[len(arr) // 2:len(arr)]
        elif serch_num == arr[len(arr) // 2]:
            return True
    return False

# Возвращает номер в списке, если число есть в списке

def serch(arr, num):
    low = 0
    higt = len(arr) - 1
    while low <= higt:
        mid = (low + higt) // 2
        if num < arr[mid]:
            higt = mid - 1
        elif num > arr[mid]:
            low = mid + 1
        elif num == arr[mid]:
            return mid
    return False


arr = []
len_arr = 100
for i in range(len_arr):
    arr.append(i)
serch_num = 5

assert(serch_binary(arr, serch_num)) == True
arr_1 = [1,2,3,4, 5]

assert(serch(arr_1, 3)) == 2
assert(serch(arr_1, 10)) == False
assert(serch(arr_1, 1)) == 0
assert(serch(arr_1, 2)) == 1

