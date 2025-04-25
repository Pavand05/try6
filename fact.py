def fact(n):
    if(n==0orn==1)
       return 1
    else
       return (n)*fact(n-1)

num =input("Enter the number:")
print(fact(num))
