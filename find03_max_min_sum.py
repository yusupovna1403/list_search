def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    i = 1
    max = data[0]
    while i < len(data):
        if data[i] > max:
            max = data[i]
        i+=1
    min = data[0]
    i = 1
    max = data[0]
    while i < len(data):
        if data[i] > min:
            min = data[i]
        i+=1
    
    return  max + min
data = [-4,1,2,6,9,4,5,9]
print(find_max_min_sum(data))

