def reverse_list(input_list):
    """
    Reverses order of elements in list input_list.
    """
    newlst=input_list[::-1]
    return newlst

def count_digits(number):
    """
    Return count of digits
    """
    temp=number
    count=0
    while temp!=0:
        count+=1
        temp=int(temp/10)

    return count
