def leapyear_check(a):

    if (a % 4 == 0):
        if (a % 100 == 0):
            return False
        return True

    return False

