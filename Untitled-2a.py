num_ip=int (input("Enter the number of input :"))
w1=1
w2=1
print("for the",num_ip,"input calculate the net using yin =x1w1+x2w2")

x1=[]
x2=[]

for j in range(0,num_ip):
    ele1=int(input("x1="))
    ele2=int(input("x2="))
    x1.append(ele1)
    x2.append(ele2)
print("x1=",x1)
print("x2=",x2)

n=x1*w1
m=x2*w2

yin =[]

for i in range (0,num_ip):
    yin .append(n[i]+m[i])
print("yin=",yin)

yin =[]

for i in range (0,num_ip):
    yin.append(n[i]-m[i])
print("After assuming one weight as excitatiry and other as yin=",yin)
y =[]

for i in range(0,num_ip):
    if (yin[i]>=1):
        ele1
        y.append(ele)
    if (yin[i]<1):
        ele =0
        y.append(ele)
print("y",y)
