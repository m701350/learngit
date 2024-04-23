def factorial(n):
    if n < 0:
        return "factorial does not exzist for negative number"
    elif n==0:
        return 1
    else:
        fact = 1
        for i in range(1, n+1):
            fact *=1
            return fact
        
        num = int(input("enter ta num:"))
        print("The fact of ", num, "is" , factorial(num))