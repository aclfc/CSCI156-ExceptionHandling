__author__ = 'Aidan'
yourssn = "Please input your social security number. Include dashes. "
sep = tuple()

def ExcHand(ssn):
    try:
        a, g, s = ssn.split("-")
    except ValueError:
        return None
    try:
        int(a)
        int(g)
        int(s)
    except ValueError:
        return None
    if len(a) != 3 or len(g) != 2 or len(s) != 4:
        return None
    elif int(a) == 000 or int(a) == 666 or 900 <= int(a) <= 999 or int(g) == 00 or int(s) == 0000:
        return None
    sep = (a,g,s)
    if sep == ("078","05","1120"):
        return None
    return sep

def SS(SSN = input(yourssn)):
    while ExcHand(SSN) is None:
        SSN = input(yourssn)
        ExcHand(SSN)

SS()