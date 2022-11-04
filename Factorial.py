def fact(n):
    p = 1
    for i in range(1,n+1):
        p=p*i
    return p

N = int(input("Enter the number to find the factorial of: "))
s = fact(N)
print(f"Factorial of {N} is {s}")
