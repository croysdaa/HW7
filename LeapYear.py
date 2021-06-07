def leapyear_check(a):

    if (a % 4 == 0):
        if (a % 100 == 0):
            if (a % 400 == 0):
                return True
            return False
        return True

    return False
while 1:
    year = input("Please enter a year to check if it's a leap year: ")
    if (year.isnumeric()):
        break

if (leapyear_check(int(year)) == True):
    print(year + " is a leap year! :D")
else:
    print(year + " is not a leap year. :(")

