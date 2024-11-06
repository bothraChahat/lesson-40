#sum of natural numbers
i=0
sum1=0
n=int(input("Enter a  number"))
while i<n:
    sum1=sum1+i
    i=i+1
print("sum of ",n,"number is",sum1)

total_sum=sum(range(1,n))
print("total sum is", total_sum)