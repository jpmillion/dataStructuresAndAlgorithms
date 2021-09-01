def mergeSort(arr)
    if arr.length < 2
        return arr 
    end

    midpoint = ((arr.length - 1) / 2).floor

    left = mergeSort(arr[..midpoint])
    right = mergeSort(arr[midpoint + 1...arr.length])

    
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

puts mergeSort([3, 7, -7, 11, 4, -7, 1, 0, -1, 13])
