def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    i = 0
    a = []

    while i < len(data):
        
        if data[i] % 2 == 0:
            a.append(data[i])
            
        i+=1
    if len(a) == 0:
        return -1
    else:
        j = 0
        max = a[0]
        while j < len(a):
            if a[j] > max:
                max = a[j]
            j+=1
        return max

            
            

    
data = [11,4,7,8,2,9]
print(find_max_even(data))
    
