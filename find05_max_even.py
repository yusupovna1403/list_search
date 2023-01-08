def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    i = 0
    max_even = []
    while i < len(data):
        if data[i] % 2 == 0:
            max_even.append(data[i])
    
        i+=1
    j = 1
    max = max_even[0]
    while j < len(max_even):
        if max_even[j] > max:
            max = max_even[j]
        j+=1

    return  max
data = [11,9,5,8,9]
print(find_max_even(data))
    
