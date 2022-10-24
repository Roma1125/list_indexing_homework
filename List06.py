def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace one with True.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    t=0
    while t<len(list1):
        if list1[t]==1:
            list1[t]=True
        t+=1
    return list1
print(main([1,0,0,0,0]))