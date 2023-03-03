# Поиск наименьшего числа в массиве перебором всего  массива          
def find_smoller(arr):
    smoller = arr[0] 
    index_smoller = 0
    for i in range(len(arr)):
        if arr[i] < smoller:
            smoller = arr[i]
            index_smoller = i
    return index_smoller


# сортировака массива
def sort_choose(arr):
    sort_arr = []
    for i in range(len(arr)):
        sort_arr.append(arr.pop(find_smoller(arr)))
    return sort_arr


x = [2,4,1, 7, 4, 6]
print(sort_choose(x))
           
    