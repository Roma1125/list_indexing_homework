def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    i=0
    count = 0
    while i<len(list1):
        if list1[0] == list1[i]:
            count+=1
        i+=1
    return count == len(list1)
print(main([1,0,0,0,0]))