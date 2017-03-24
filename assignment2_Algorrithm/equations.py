
"""
Created on Fri Mar 24 09:21:21 2017

#Author: Ashish Kumar Jayant
#Title: Regular-Falsi method 
"""
from __future__ import division
import math
def solve(equation_n,xa,xb,n,e):
	equation_o = equation_n.replace('b','a')
	equation_sn = equation_n.replace('b','c')
	for i in range(n):
		xc = xb - eval(equation_n) * ((xb-xa) / (eval(equation_n) - eval(equation_o)))
		b = abs((xc - xb) / xb)

		if (b < e):
			break
		elif (eval(equation_n) * eval(equation_sn) < 0):
			temp = xb
			xb = xc
			xa = temp
		elif (eval(equation_n) * eval(equation_sn) >= 0):
			xb = xc
	   
		
	print ("Root of "+equation_n+'= '+str(xc))

solve("xb**2 - 2*xb - 1",1,2,10,0.0001)
solve("5*(math.sin(xb)**2) - 8*(math.cos(xb)**5)",0.5,1.5,10,0.00001)




