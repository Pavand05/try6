def fact(n):
    
    # single line to find factorial
    return 1 if (n==1 or n==0) else n * fact(n - 1) 

# Driver Code
num =input("Enter the number:")
print(fact(num))
