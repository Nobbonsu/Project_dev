def linear_search(list, target):

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("Is at index: ", index)
    else:
        print("Is not in the list")


num1 = [2, 3, 5, 7, 1, 8, 9, 4, 6]
target = 7

findNum = linear_search(num1, target=target)
verify(findNum)
