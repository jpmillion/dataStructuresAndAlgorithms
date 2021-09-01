function mergeSort1(arr) {
    if (arr.length < 2) return arr;
    const mid = Math.floor(arr.length / 2);

    const left = mergeSort1(arr.slice(0, mid));
    const right = mergeSort1(arr.slice(mid));

    return merge(left, right);
}

function merge(a1, a2){
    const a3 = new Array(a1.length + a2.length);

    for (i = 0, j = 0, k = 0; i < a3.length; i++) {
        if (k >= a2.length || (j < a1.length && a1[j] < a2[k])) a3[i] = a1[j++];
        else a3[i] = a2[k++];
    }

    return a3;
}

function mergeSort2(arr) {
    if (arr.length < 2) return arr;

    const arrCopy = [...arr];
    mergeSortHelper(arr, 0, arr.length - 1, arrCopy);
    return arr;
}

function mergeSortHelper(arr, start, end, arrCopy) {
    if (start === end) return;
    const midPoint = Math.floor((start + end) / 2);

    mergeSortHelper(arrCopy, start, midPoint, arr);
    mergeSortHelper(arrCopy, midPoint + 1, end, arr);

    mergeInPlace(arr, start, midPoint, end, arrCopy);
}

function mergeInPlace(arr, start, midPoint, end, arrCopy) {
    let leftIdx = start;
    let rightIdx = midPoint + 1;

    for (let i = start; i <= end; i++) {
        if (rightIdx > end || (leftIdx <= midPoint && arrCopy[leftIdx] < arrCopy[rightIdx])) arr[i] = arrCopy[leftIdx++];
        else arr[i] = arrCopy[rightIdx++];
    }
}

arr = mergeSort1([-9, 9, -8, 8, 7, 6, -7, -6]);
console.log(arr);

arr = mergeSort2([-9, 9, -8, 8, 7, 6, -7, -6]);
console.log(arr);




