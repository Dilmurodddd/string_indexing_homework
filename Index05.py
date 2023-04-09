def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:Besh uzunlikdagi o'zgaruvchining qatori berilgan. Ushbu o'zgaruvchiga kiritilgan raqamlar sonini aniqlang.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    a=str(s)[0]
    b=str(s)[1]
    c=str(s)[2]
    d=str(s)[3]
    e=str(s)[4]
    t=0
    if str(a).isdigit():
        t=1
    if str(b).isdigit():
        t=t+1
    if str(c).isdigit():
        t=t+1
    if str(d).isdigit():
        t=t+1
    if str(e).isdigit():
        t=t+1
    return  t
print(main('ab123'))