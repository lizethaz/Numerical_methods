#Library for matrix
import numpy as np
#Library to make copies
import copy

print ("Gauss-Seidel")
print (" ")

#/////////Add coefficients!!!!!!!!/////////
A = np.matrix('4 -1 0 1 0; -1 4 -1 0 1; 0 -1 4 -1 0; 1 0 -1 4 -1; 0 1 0 -1 4')
b = np.matrix('100; 100; 100; 100; 100')

print ('A=',A)
print ('b=',b)

#initializacion parameters
n=len(A)	#get lenght
k=0			#index
xk=np.zeros(n)	#inital values 0 vector k
xk1=np.zeros(n)	#vector k+1
xbackup1=np.zeros(n)	#backup of xk
xbackup2=np.ones(n)		#backup of xk1 (after sustitution). Initial value 1 to do first iteration
iteration=0

xbackup1=copy.copy (xk)

#convergence
while  not np.allclose(xbackup1, xbackup2, rtol=1e-7): #compare xbackup1 with xbackup2 if the direfference > 1e-7 then do another iteration 
	iteration+=1
	xbackup1=copy.copy (xk)	#backup xk to avoid losing values for the comparison	
#/////////Sustitution
	for i in range(0,n):
		for j in range (0,n):
			if j!=i:			#if to avoid evaluating elements from the diagonal
				xk1[i]=xk1[i]+A[i,j]*xk[j]
		xk[i]=(b[i]-xk1[i])/A[i,i]
	xbackup2=copy.copy (xk)	
	xk1 = np.zeros(n) #clean vector for next iteration
print (" ")
print ("Results:")
print ('x=',xk)
print ('No. Iteration=',iteration)