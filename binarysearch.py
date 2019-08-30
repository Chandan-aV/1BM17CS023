def search(lis,len,key):
    start=0
    end=len-1
    while start<=end:
        mid=int((start+end)/2)
        if key==lis[mid]:
            print("\nEntered number is present at position : ",mid)
            return -1
        elif key<lis[mid]:
            end=mid-1
        elif key>lis[mid]:
            start=mid+1
            print("\nelement not found!")
    return -1
lst=[]
size=int(input("enter size of list :\t"))
for n in range(size):
    num=int(input("Enter number:\t"))
    lst.append(num)
lst.sort()
print("\n sorted list",lst)
x=int(input("\nEmter the number to search: "))
search(lst,size,x)
