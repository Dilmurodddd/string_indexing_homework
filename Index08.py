def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:Besh uzunlikdagi qator berilgan. "*" belgisining indeksini qaytaring, agar mavjud bo'lmasa, False qiymatini qaytaring.
        s(str): parameter
    Returns:
        int: answer
    """

    return str(s).index('*')
print(main('assdd*'))
        