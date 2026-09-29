num =int(input("enter the number"))
p =len(str(num))
sum =0
n =num
while(num>0):
    sum+=(num% 10)**p
    num//=10
if (n==sum):
    print("Number is Armstorng")