x= float (input("enter value of X"))
W= float (input("enter value of W"))
b= float (input("enter value of b"))

net =int(W*x+b)
if (net<0):
    out =0
elif((net>=0)&(net<=1)):
    out = net 
else:
    out=1
print("net =",net)
print("output=",out)

