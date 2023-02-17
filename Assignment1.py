import numpy as np
import matplotlib.pyplot as plt

k=int(input("Enter number of features: ")) 
#i=int(input("Enter number of sample points: ")) 
input_string = input('Enter elements of a list separated by space for sample points : ')
inputList = input_string.split()
# convert each item to int type
for i in range(len(inputList)):
    # convert each item to int type
    inputList[i] = int(inputList[i])
errorList=[]
for i in inputList:
   θ=np.random.normal(0,1,size=(k, 1))#theta
   X=np.random.normal(0,4,size=(i, k))
   e=np.random.normal(0,0.1,1)
   eMatrix = [e * 1] * i
   Y=X@θ+eMatrix
   if(np.linalg.matrix_rank(X.T@X) == len(X.T@X)):
     θ1=(np.linalg.inv(X.T@X))@(X.T)@Y
     #print(θ1)
     temp=θ-θ1
     result_square=temp.T@temp
     result=result_square**0.5
     print("------------------------")
     print("The error calculated is : ",end="")
     print(result)
     #print(type(result[0][0]))
     errorList.append(result[0][0])
     print("------------------------")
   else:
     print("for the given input values XT.X is not invertible")
     break    


  
plt.plot(inputList, errorList)
plt.xlabel('input N')
plt.ylabel('error')
plt.title('')
plt.show()
plt.savefig('image.jpeg')
