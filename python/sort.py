def mergeSort(arr):
    if len(arr) < 2:
        return arr
    
    mergeSortHelper(arr, 0, len(arr) - 1, arr[:])
    return arr


def mergeSortHelper(arr, start, end, copy):
    if start == end:
        return

    mid = (end + start) // 2

    mergeSortHelper(copy, start, mid, arr)
    mergeSortHelper(copy, mid+1, end, arr)

    merge(arr, start, mid, end, copy)

def merge(arr, start, mid, end, copy):
    i = start
    j = mid + 1

    for k in range(start, end+1):

        if j > end:
            arr[k] = copy[i]
            i += 1
            continue

        elif i > mid:
            arr[k] = copy[j]
            j += 1
            continue
        
        if copy[i] < copy[j]:
            arr[k] = copy[i]
            i += 1
        else:
            arr[k] = copy[j]
            j += 1
    