def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left , right)

def merge(l , r):
    result = []
    i = j = 0
    n1 = len(l) 
    n2 = len(r)
    while i < n1 and j < n2:
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1

    result.extend(l[i:])
    result.extend(r[j:])
    return result


arr = [2,5,4,3,6,1,0,7,9,8,17,15,23,20,34,52]
sorted = merge_sort(arr)
print('Sorted array' , sorted)