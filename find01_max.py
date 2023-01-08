def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    i = 1
    max = data[0]
    while i < len(data):
        if data[i] > max:
            max = data[i]
        i+=1
    return  max
data = [1,2,6,4,5,9]
print(find_max(data))
    