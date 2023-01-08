def find_min_index(data):
    """
    Given the list of numbers, return the index of minimum number in the list
    args:
        data: list of numbers
    returns: index of minimum number in the list
    """
    i = 1
    min = data[0]
    while i < len(data):
        if data[i] < min:
            min = data[i]
        i+=1
    min_index = data.index(min)
    return  min_index
data = [1,2,6,9,-4,5,9]
print(find_min_index(data))

