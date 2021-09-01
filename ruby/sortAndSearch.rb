def mergeSortA(arr)
    if arr.length < 2
        return arr 
    end

    midpoint = ((arr.length - 1) / 2).floor

    left = mergeSortA(arr[..midpoint])
    right = mergeSortA(arr[midpoint + 1...arr.length])

    
    merge(left, right)
end

def merge(a1, a2)
    mergedArr = Array.new(a1.length + a2.length)
    a1Idx = 0
    a2Idx = 0

    for i in 0...mergedArr.length
        if a2Idx >= a2.length || (a1Idx < a1.length && a1[a1Idx] < a2[a2Idx])
            mergedArr[i] = a1[a1Idx]
            a1Idx += 1
        else 
            mergedArr[i] = a2[a2Idx]
            a2Idx += 1
        end
    end

    mergedArr
end

def mergeSortB(arr)
    return arr if arr.length < 2

    mergeSortHelper(arr, 0, arr.length - 1, arr[...arr.length])
    arr
end

def mergeSortHelper(arr, start, finish, arrCopy)
    return if start >= finish
    midpoint = midpoint = ((start + finish) / 2).floor

    mergeSortHelper(arrCopy, start, midpoint, arr)
    mergeSortHelper(arrCopy, midpoint + 1, finish, arr)

    mergeB(arr, start, midpoint, finish, arrCopy)
end

def mergeB(arr, start, midpoint, finish, arrCopy)
    left = start
    right = midpoint + 1

    for i in start..finish
        if right > finish || (left <= midpoint && arrCopy[left] < arrCopy[right])
            arr[i] = arrCopy[left]
            left += 1
        else
            arr[i] = arrCopy[right]
            right += 1
        end
    end
end

puts mergeSortA([3, 7, -7, 11, 4, -7, 1, 0, -1, 13])
puts mergeSortB([3, 7, -7, 11, 4, -7, 1, 0, -1, 13])
