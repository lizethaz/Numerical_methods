#Library for matrix
import numpy as np
print ("Gauss-Elimination")
print (" ")

#/////////Add coefficients!!!!!!!!/////////
#NOTE: the coeffients need the point to avoid losing data
#A = np.matrix('1. -1. -1. 0. 0. 0.; -1. 1. 0. 0. 0. 1.; 0. 0. 1. -1. -1. 0.; 0. 0. 0. -12. 11. 0.; 5. 20. 0. 0. 0. 0.; 0. -20. 6. 12. 0. 4.')
#b = np.matrix('0. ; 0.; 0.; 0.; 110.; 0.')
A = np.matrix('-1. 1. 0. 0. 0. 1.; 5. 20. 0. 0. 0. 0.; 1. -1. -1. 0. 0. 0.; 0. 0. 1. -1. -1. 0.; 0. 0. 0. -12. 11. 0.; 0. -20. 6. 12. 0. 4.')
b = np.matrix('0.; 110.; 0.; 0.; 0.; 0.')
print ('A=',A)
print ('b=',b)

#initialization parameters
n=len(A)		#get length
k=n-1			#index
x = np.zeros(n)	#vector with results
change=True		#variable to check if it needed to sawp rows

for k in range(n-1):
	#/////////routine to avoid dividing by 0
	if change:
		# 
		maxindex = abs(A[k:,k]).argmax() + k
		# Switch rows
		if maxindex != k:
			A[[k,maxindex]] = A[[maxindex, k]]
			b[[k,maxindex]] = b[[maxindex, k]]
	
	#/////////Elimination
	for k in range(n-1):
		for i in range(k+1, n):
			pivote = A[i,k]/A[k,k]
			A[i, k:] = A[i, k:] - pivote*A[k, k:]
			b[i] = b[i] - pivote*b[k]

x=np.zeros(n)

#/////////Back Substitution
for k in range(n-1, -1, -1): #for start in k=n-1, ends in k=-1, step=-1
	x[k] = (b[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k] #dot product to get results

print (" ")
print ("Results:")
print ('A=',A)
print ('x=',x)