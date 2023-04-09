def main(s,n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:s string o'zgaruvchisi berilgan. n Indeksdagi belgini qaytaring, aks holda False qiymatini qaytaring.
        s(str): parameter
    Returns:
        str: answer
    """
    if len(s)>=n:
        s=s[n]
    return s
print(main('abcdefghijklmnopqrstuvxyz',10))
