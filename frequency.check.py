list1=[]
n=int(input("Enter the number of elements in list: "))
for i in range(0,n):
    x=int(input("Enter elements of list: "))
    list1.append(x)
print("list of numbers: ",list1)
b=int(input("enter element for freq check: "))
print(b,"is occuring",list1.count(b),"times")

