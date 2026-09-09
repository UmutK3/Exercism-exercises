def find(search_list, value):
    left = 0
    right = len(search_list) - 1
    while right >= left:
        middle = (right + left) // 2
        if search_list[middle] == value:
            return middle
        elif search_list[middle] > value:
            right = middle - 1
        else:
            left = middle + 1
    raise ValueError("value not in array")
