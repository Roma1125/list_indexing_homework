def main(list1):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    t=0
    while t<len(list1):
        if list1[t]==0:
            list1[t]=False
        if list1[t]==1:
            list1[t]=True
        t+=1
    return list1
print(main([1,0,0,0,0]))