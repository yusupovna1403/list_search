def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    i = 0
    num = []
    
    while i < len(data):
        
        if data[i] % 2 == 1:
            num.append(data[i])
            
        i+=1
    if len(num) == 0:
        return -1
    else:
        
        return min(num)

            
            

    
data = [1,4,7,8,9,-3]
print(find_min_odd(data))

