import numpy as np 
import time
np.set_printoptions(precision=2)

x=np.zeros((3,))
weights =np.zeros((3,))
desired =np.zeros((3,))
actual =np.zeros((3,))

for i in range (0,3):
    x[i] =float(input("initial inputs :"))
for i in range (0,3):
    weights[i] =float(input("initial weight :"))
for i in range (0,3):
    desired[i] =float(input("initial desired :"))

learning_rate=float(input("Enter learning rate:"))

actual =x*weights
print("actual",actual)
print("desired",desired)

while True:
    if np.array_equal(desired,actual):
        break
    else:
        for i in range (0,3):
            weights[i] =weights[i]+learning_rate*(desired[i] -actual[i])
        actual=x*weights

        print("weights",weights)
        print("actual",actual)
        print("desired",desired)
        print("*",30)

print("final output")
print("corrected weights",weights)
print("actual",actual)
print("desired",desired)

