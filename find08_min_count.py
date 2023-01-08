def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    i = 1
    min = data[0]
    while i < len(data):
        if data[i] < min:
            min = data[i]
        i+=1
    min_count = data.count(min)
    return  min_count
data = [1,2,1,6,9,4,5,9]
print(find_min_count(data))
