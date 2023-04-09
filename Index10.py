def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:Beshta raqamdan iborat qator berilgan. Uning sonlari yig‘indisini toping.
        s(str): parameter
    Returns:
        int: answer
    """
    a=s[0]
    b=s[1]
    c=s[2]
    d=s[3]
    e=s[4]
    f=0
    

    if str(a).isdigit():
        f+=int(a)
    if str(b).isdigit():
        f+=int(b)
    if str(c).isdigit():
        f+=int(c)
    if str(d).isdigit():
        f+=int(d)
    if str(e).isdigit():
        f+=int(e)
    return f
print(main('a2b3c'))
