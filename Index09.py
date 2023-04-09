def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:bitta belgilar qatori beriladi. Uni int turiga aylantiring, iloji bo'lmasa -1ni qaytaring.
        s(str): parameter
    Returns:
        int: answer
    """
    return str(s).find('1')
print(main('asdfghjkl'))