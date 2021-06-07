def leapyear_check(a):

    if (a % 4 == 0):
        if (a % 100 == 0):
            if (a % 400 == 0):
                return True
            return False
        return True

    return False

