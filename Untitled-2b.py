import numpy as np

print("enter weight")
w11=int(input ("weight w11="))
w12=int(input ("weight w12="))
w21=int(input ("weight w21="))
w22=int(input ("weight w22="))
v1 = int(input("weight v1="))
v2 =int(input("weight v2="))

print("enter thershold value")
theta =int(input("theta"))

x1=np.array([0,0,1,1])
x2=np.array([0,1,0,1])
z =np.array([0,1,1,0])
con=1

y1 =np.zeros((4,))
y2 =np.zeros((4,))
y =np.zeros((4,))

while con==1:

    zin1 =np.zeros((4,))
    zin1 =np.zeros((4,))
    zin1=x1*w11+x2*w21
    zin2=x1*w12+x2*w22
    print('z1',zin1)
    print('z1',zin1)

    for i in range (0,4):
        if zin1[i]>=theta:
            y2[i]=1
        else:
            y2 [i] =0
yin =np.array([])
yin=y1*v1+y2*v2

for i in range (0,4):
    if yin[i]>=theta:
        y[i]=1
    else :
        y[i]=0
print("yin",yin)
print("output of net")
y=y.astype(int)
print("y",y)
print("z",z)
            
if np.array_equal(y,z) :
    con=0
else:
    print("net is not learning enter another set of weights and thershold value")
    w11 = input("weight w11=")
    w12 = input("weight w12=")
    w21 = input("weight w21=")
    w22 = input("weight w22=")
    v1 = input("weight v1=")
    v2= input("weight v2=")
    theta = input("theta")
            
print("McCulloch-pitts Net for XOR function")
print("weight of neuron Z1")
print(w11)
print(w21)
print("weight of neuron Z2")
print(w12)
print(w22)
print("weight of neuron Y")
print(v1)
print(v2)
print("thershold value")
print('theta')
