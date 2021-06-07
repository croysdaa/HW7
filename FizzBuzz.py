def fizzbuzz_check(a):
    
    if (a % 3 == 0):
        if (a % 5 == 0):
            return "FizzBuzz"
        return "Fizz"

    if (a % 5 == 0):
        return "Buzz" 
    
    return a

for i in range(1, 101):
    print(fizzbuzz_check(i))
