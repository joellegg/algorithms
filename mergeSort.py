import random


def mergeSort(arr):
    # split array
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # keep splitting
        mergeSort(left_half)
        mergeSort(right_half)

        i = 0
        j = 0
        k = 0

        # while there are values remaining in both arrays
        while i < len(left_half) and j < len(right_half):
            # find smaller value
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i = i + 1
            else:
                arr[k] = right_half[j]
                j = j + 1
            k = k + 1

        # if anything left in left array
        while i < len(left_half):
            arr[k] = left_half[i]
            i = i + 1
            k = k + 1

        # if anything left in right array
        while j < len(right_half):
            arr[k] = right_half[j]
            j = j + 1
            k = k + 1


def test():
    arrayLength = 1000000
    newArray = []
    for x in range(arrayLength):
        newArray.append(random.randint(1, 101))

    mergeSort(newArray)
    if (len(newArray) != arrayLength):
        return print('Array count off')
    if any(newArray[i] > newArray[i + 1] for i in range(len(newArray) - 1)):
        return print('Array not sorted')
    else:
        return print('All pass')


test()
