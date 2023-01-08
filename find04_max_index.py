def find_max_index(data):
    """
    Given the list of numbers, return the index of maximum number in the list
    args:
        data: list of numbers
    returns: index of maximum number in the list
    """

    i = 1
    max = data[0]
    while i < len(data):
        if data[i] > max:
            max = data[i]
        i+=1
    
    return  data.index(max)
data = [1,2,6,4,5,9]
print(find_max_index(data))
    
