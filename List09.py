def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    
    t=0
    while t<len(list1):
        
        if list1[0]!=list1[t]:
            a=(False)
        else: 
            a=(True)
        t+=1
    return a 
print(main([1,0,0,0,0]))