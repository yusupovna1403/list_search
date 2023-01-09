def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    i = 0
    a = []

    while i < len(data):
        
        if data[i] % 2 == 1:
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

            
            

    
data = [11,4,7,8,2]
print(find_max_odd(data))

            
            
