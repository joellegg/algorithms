import random


def quicksort(arr, low, high):
    if high - low > 1:
        p = partition(arr, low, high)
        # sort the left side
        quicksort(arr, low, p)
        # sort the right side
        quicksort(arr, p + 1, high)


def partition(arr, start, end):
    pivot = arr[start]
    low = start + 1
    high = end

    while True:
        # If the current value is larger than the pivot
        # it's in the correct place (right side of pivot)
        # and we can move left, to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and arr[high] >= pivot:
            high = high - 1

        while low <= high and arr[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]

        else:
            break

    arr[start], arr[high] = arr[high], arr[start]

    return high


arrayLength = 10
array = []
for x in range(arrayLength):
    array.append(random.randint(1, 101))

quicksort(array, 0, arrayLength - 1)

print(array)
