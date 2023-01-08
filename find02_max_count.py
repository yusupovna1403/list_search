def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """

    i = 1
    s = 0
    max = data[0]
    while i < len(data):
        if data[i] > max:
            max = data[i]
        i+=1
    while data:
        if max == data.pop():
            s+=1
    return  s
data = [1,2,6,9,4,5,9]
print(find_max_count(data))
