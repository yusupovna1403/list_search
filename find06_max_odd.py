# Given the list of numbers, Find the maximum odd number in the list
def find_max_odd(data:list[int])->int:
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    m = data[0]
    for i in data:
        if m<i and i%2!=0:
            m=i
    return m

# Example
# Input: [1, 8, 3, 8, 5]
# Output: 5