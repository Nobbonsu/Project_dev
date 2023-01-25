def binary_search(list, target):

    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if midpoint == target:
            return midpoint
        elif midpoint < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in the list")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8

results = binary_search(numbers, target=target)
verify(results)
