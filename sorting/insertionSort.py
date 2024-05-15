def insertion_sort(list):
    n = len(list)
    for i in range(1,n):
        key = list[i]
        j = i-1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
    return list

arr = [3,3,4,5,6,4,3,5,-1,-9,-8,-7,44,66,76,87,98,9765,78,1,0,88]

sorted_list = insertion_sort(arr)

print(sorted_list)