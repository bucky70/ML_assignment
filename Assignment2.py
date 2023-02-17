import numpy as np
import matplotlib.pyplot as plt

k=int(input("Enter number of features: ")) 
i=int(input("Enter number of sample points: ")) 
input_string = input('Enter elements of a list separated by space for lambda λ: ')
inputList = input_string.split()
# convert each item to int type
for j in range(len(inputList)):
    # convert each item to int type
    inputList[j] = float(inputList[j])
errorList=[]
for λ in inputList:
   θ=np.random.normal(0,1,size=(k, 1))#theta
   X=np.random.normal(0,4,size=(i, k))
   e=np.random.normal(0,0.1,1)
   eMatrix = [e * 1] * i
   Y=np.matmul(X,θ)+eMatrix
   #λ=0.01
   θ1=(np.linalg.inv(X.T@X+(λ**2)*np.identity(k)))@((X.T)@Y)
   temp=θ-θ1
   result_square=temp.T@temp
   result=result_square**0.5
   print("------------------------")
   print("The error calculated is : ",end="")
   print(result)
   errorList.append(result[0][0])
   print("------------------------")
      


  
plt.plot(inputList, errorList)
plt.xlabel('lambda λ')
plt.ylabel('error')
plt.title('')
plt.show()
plt.savefig('image.jpeg')
