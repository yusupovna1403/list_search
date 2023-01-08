def find_min(data):
    """
    Given the list of numbers, return the minimum number in the list
    args:
        data: list of numbers
    returns: minimum number in the list
    """

    i = 1
    min = data[0]
    while i < len(data):
        if data[i] < min:
            min = data[i]
        i+=1
    
    return  min
data = [1,2,6,9,4,5,9]
print(find_min(data))
    