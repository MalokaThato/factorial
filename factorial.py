def factorial_num(x):
    result = 1
    try:
        if int(x) < 0:
            return(print("We can not produce the factorial of a negative number:"))
        else:
            for p in range(1,int(x) + 1):
                if p >= 1 or p == 0:
                    result = result * p
                else:
                    continue
    except:
        return(print("Please input only numbers."))
    return(result)
print(factorial_num(input("Enter the number you would like to get's factorial: ")))
