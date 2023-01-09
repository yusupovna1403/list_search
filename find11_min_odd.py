def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    i = 0
    num = []
    s = 0
    while i < len(data):
        
        if data[i] % 2 == 1:
            num.append(data[i])
            s+=1
        i+=1
    if s == 0:
        return -1
    else:
        min = num[0]
        while i < len(num):
            if num[i] < min:
                min = num[i]
        return min

            
            

    
data = [1,4,7,8,9]
print(find_min_odd(data))

