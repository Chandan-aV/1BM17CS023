num=int(input("Enter the number:"))
divisor=[]
print("The divisors of the number are:")
for i in range(1,num+1):
    if(num%i==0):
        divisor.append(i)
print(divisor)
        
