
#getEvalSteps("2+3*4-8**3%3")
# print 8 ** 3 

"""2+3*4-8**3%3 = 2+3*4-512%3 
			 = 2+12-512%3
             = 2+12-2
             = 14-2
             = 12"""
tempString = ''
equation = '8*3+5'  
sign = equation.index('*')
print sign 
print equation[1]
if equation[1] == '*': 
	temp =  int(equation[1-1]) * int(equation[1+1])
print temp 
tempString = tempString + str(temp) + equation[3:]
print tempString 


