# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 18:54:17 2019

@author: RAJDEEP PAL
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
#%%
# Function to return gcd of a and b 
def gcd(a, b):   # want a > b
  
    if (a == b):
        return a
    elif ( b == 0 ):
        return a
    elif (a < b):
        return gcd(b, a)
    return gcd(b, b%a) 

#%%
def gcd(a, b): 
  
    if (a == 0): 
        return b 
    return gcd(b % a, a) 

#"""  Euler Totient Function  """
def phi(n): 
  
    result = 1
    for i in range(2, n): 
        if (gcd(i, n) == 1): 
            result+=1
    return result 

#%%  
# Driver Code 
totient_vals = np.zeros(1000)   
x = np.zeros(1000) 
for i in range(1, 1001): # i = 1 to 1000  
    #print (i)
    x[i-1] = i
    totient_vals[i-1] = phi(i)
    print ( phi(i) )
#%%
y = totient_vals
temp = x-1
font = {
 #   'family' : 'Bitstream Vera Sans',
    'family' : 'DejaVu Sans',
    'weight' : 'bold',
    'size'   : 18
}
matplotlib.rc('font', **font)

plt.figure(figsize=(20, 20))


plt.plot(x, y, 'ro')





plt.title("Euler's Totient Function for the first 1000 positive integers")
#plt.legend(loc='upper right', shadow=True)
plt.ylabel('Totient values : phi(x)')
plt.xlabel('Integers : x')

plt.savefig("Totient Fuction")






             
# This code is contributed 
# by Smitha 