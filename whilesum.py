#sum of natural numbers till n
n=int(input("enter value of n"))
sum=0

i=1
while i<=n:
    sum=sum+i
    print(sum,end="")
    i=i+1
    print(i,end="")
    
print()   
print(sum)    