#Library for matrix
import numpy as np
#Library to make copies
import copy

print ("Gauss-Seidel")
print (" ")

#/////////Add coefficients!!!!!!!!/////////
A = np.matrix('4. -1. 0. 1. 0.; -1. 4. -1. 0. 1.; 0. -1. 4. -1. 0.; 1. 0. -1. 4. -1.; 0. 1. 0. -1. 4.')
b = np.matrix('100.; 100.; 100.; 100.; 100.')
#A = np.matrix('-1. 1. 0. 0. 0. 1.; 5. 20. 0. 0. 0. 0.; 1. -1. -1. 0. 0. 0.; 0. 0. 1. -1. -1. 0.; 0. 0. 0. -12. 11. 0.; 0. -20. 6. 12. 0. 4.')
#b = np.matrix('0.; 110.; 0.; 0.; 0.; 0.')

print ('A=',A)
print ('b=',b)

#/////////Initializacion parameters
n=len(A)				#get lenght
k=0						#index
xk=np.zeros(n)			#inital values 0 vector k
xk1=np.zeros(n)			#vector k+1
xbackup1=np.zeros(n)	#backup
xbackup2=np.ones(n)		#backup. Initial value 1 to do first iteration
iteration=0
R=np.zeros(n)			#Residual

#/////////Convergence
while  not np.allclose(xbackup1, xbackup2, rtol=1e-10): #compare xbackup1 with xbackup2 if the direfference > 1e-7 then do another iteration 
	iteration+=1
	xbackup1=copy.copy (xk)	#backup x(k) to avoid losing values to check convergence	
	xk=np.zeros
	#/////////Sustitution
	for i in range(0,n):
		R=np.zeros(n)
		#/////////Sum x(k+1)
		for j in range (0,i):
			R[i]=R[i]+A[i,j]*xk1[j]
		#/////////Sum x(k)
		for j in range (i,n):
			R[i]=R[i]+A[i,j]*xk[j]
		#/////////Getting residual
		R[i]=(b[i]-R[i])/A[i,i]
		#/////////Getting x(k+1)
		xk1[i]=xk[i]+R[i]+xk[i]
	xbackup2=copy.copy (xk1)		#backup x(k+1) to avoid losing values to check convergence	
	xk1=copy.copy (xk)

print (" ")
print ("Results:")
print ('x=',xk)
print ('x=',xk1)
print ('No. Iteration=',iteration)