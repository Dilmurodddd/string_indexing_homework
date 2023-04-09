def main(s):
    """
    A string variable consisting of several characters is given. Add and return the first and last character.
    Args:Bir nechta belgilardan iborat qator o'zgaruvchisi berilgan. Birinchi va oxirgi belgini qo'shing va qaytaring.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    return f"{s[:1]+s[-1]}"
print(main('abcde'))