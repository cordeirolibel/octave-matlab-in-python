import math
import os

variables_names = ['ans','e'   ,'exp' ,'pi'   ] 
variables_value = [None ,math.e,math.e,math.pi]
n_variables = 4

#save new value in variable, return None if variable is not defined
def saveVariable (name,value):
	#find varible
	i=0
	while i < n_variables:
		if name == variables_names[i]:
			variables_value[i]=value
			return i
		i+=1
	#variable is not defined
	return None

#save new value in variable, return None if variable is not defined
def creatVariable (name,value):
	global n_variables
	n_variables+=1
	variables_names.append(name)
	variables_value.append(value)

#return value of variable name, None if not exist
def valueVariable(name):
	i=0
	while i < n_variables:
		if name == variables_names[i]:
			return variables_value[i]
		i+=1
	return None

#return True if num it is multiple of pi in the variables
def multiplePi(num):
	#find variable pi
	pi = valueVariable('pi')
	if pi is None:#not find pi
		return False
	#rest
	rest_float = num/pi
	try:
		rest_int = int(rest_float)
	except:#variable incorrect
		return False
	#if multiple
	if rest_int == rest_float:
		return True
	else:
		return False
		
#print(s of help 
def printHelp (clause):
	if clause == '':
		print('==================Help==================')
		print('Type it: > help clause')
		print('Variables:',n_variables)
		i=0
		while i<n_variables:
			print('\t',variables_names[i],'\t=',variables_value[i])
			i+=1
		print('Functions:')
		print('\tsqrt')
		print('\tlog')
		print('\tln')
		print('\tsin')
		print('\tcos')
		print('\ttan or tg or tag')
		print('\tasin or arcsin')
		print('\tacos or arccos')
		print('\tatan or atg or atag or arctan or arctg or arctag')
		print('\tsind')
		print('\tcosd')
		print('\ttand or tgd or tagd')
		print('\tasind or arcsind')
		print('\tacosd or arcosd')
		print('\tatand or atgd or atagd or arctand or arctgd or arctagd')
		print('\tpow')
		print('\tdivision')
		print('\tmultiplication')
		print('\tsubtraction')
		print('\taddition')
		print('Commands:')
		print('\tquit')
		print('\tclear or clc')
		print('\tsay')
		print('\thelp')
		print('===================//===================')
	else:
		print(clause, 'is not define')

#find term (variable, constante) starting in pos+1 or pos-1, return your other limit
def findTerm(string, pos, direction):
	#for right
	if direction == 'R':
		pos_finish=pos
		for character in string[pos+1:]:
			#if not number or letter or signal or point or comma
			if not character.isalnum() and not character=='-' and not character=='.' and not character==',':
				break
			pos_finish+=1
		if pos_finish == pos: #not exist term
			return None
		return pos_finish
	#for left
	elif direction == 'L':
		pos_start=pos
		while pos_start > 0:
			#if not number or letter or signal or point or comma
			if not string[pos_start-1].isalnum() and not string[pos_start-1]=='-'and not string[pos_start-1]=='.'and not string[pos_start-1]==',':
				break
			pos_start-=1
		if pos_start == pos: #not exist term
			return None
		return pos_start
	else :
		return None

#find the ')'
def parClose (string, par_start):
	num_par=1
	par_close = par_start+1
	for letter in string[par_start+1:]:
		if letter == '(':
			num_par += 1
		elif letter == ')':
			num_par -= 1
		if num_par == 0: #find the close
			return par_close 
		par_close+=1
	#dont find the close
	return -1

#functions, return result (num is number or numbers)
def functions(name_function, num):
	#root
	if name_function == 'sqrt':
		if num < 0:#Math Error
			print('Math Error, is not defined')
			print(name_function + '(' + str(num) + ')')
			return None
		else: #calculus
			return math.sqrt(num)
	#ln
	elif name_function == 'ln':
		if num < 0:#Math Error
			print('Math Error, is not defined')
			print(name_function + '(' + str(num) + ')')
			return None
		else:#calculus
			return math.log(num)
	#log
	elif name_function == 'log':
		try:#if known base 
			base = num[0]
			log = num[1]
			if base <= 0 or base == 1 or log <= 0:#Math Error
				print('Math Error, is not defined')
				print(name_function + '(' + str(base) + ',' + str(log) + ')')
				return None
			return math.log(log)/math.log(base)
		except:#base is exp
			return functions('ln',num)
	#sin
	elif name_function == 'sin' or name_function == 'sind':
		if name_function[-1] == 'd':#degrees
			num = math.radians(num) #degrees to radians 
		if multiplePi(num) is True:
			return 0
		return math.sin(num)
	#cos
	elif name_function == 'cos' or name_function == 'cosd':
		if name_function[-1] == 'd':#degrees
			num = math.radians(num) #degrees to radians
		return math.cos(num)
	#tag
	elif name_function == 'tg' or name_function == 'tgd' or name_function == 'tan' or name_function == 'tand' or name_function == 'tag' or name_function == 'tagd':
		if name_function[-1] == 'd':#degrees
			num = math.radians(num) #degrees to radians
		#calculus
		#if multiple of pi/2 
		if multiplePi(num+valueVariable('pi')/2) is True: 
			print('Math Error, is not defined')
			print(name_function + '(' + str(num) + ')')
			return None
		return math.tan(num)
	#asin
	elif name_function == 'asin' or name_function == 'asind' or name_function == 'arcsin' or name_function == 'arcsind':
		if (num < -1) or (num > 1):#Math Error
			print('Math Error, is not defined')
			print(name_function + '(' + str(num) + ')')
			return None
		num = math.asin(num)
		if name_function[-1] == 'd':#degrees
			num = math.degrees(num) #radians to degrees
		return num
	#acos
	elif name_function == 'acos' or name_function == 'acosd' or name_function == 'arccos' or name_function == 'arccosd':
		if (num < -1) or (num > 1):#Math Error
			print('Math Error, is not defined')
			print(name_function + '(' + str(num) + ')')
			return None
		num = math.acos(num)
		if name_function[-1] == 'd':#degrees
			num = math.degrees(num) #radians to degrees
		return num
	#atan
	elif name_function == 'atg' or name_function == 'atgd' or name_function == 'atan' or name_function == 'atand' or name_function == 'atag' or name_function == 'atagd' or name_function == 'arctg' or name_function == 'arctgd' or name_function == 'arctan' or name_function == 'arctand' or name_function == 'arctag' or name_function == 'arctagd':
		num = math.atan(num)
		if name_function[-1] == 'd':#degrees
			num = math.degrees(num) #radians to degrees
		return num
	#exponent
	elif name_function == 'pow':
		try:#if known base and exponent 
			base = num[0]
			exp = num[1]
			if base < 0:
				return -((-base)**exp)
			else:
				return base**exp
		except:#if known exponent: base = 10
			base = 10
			exp = num
			return base**exp
	#division
	elif name_function == 'division':
		try:
			quotient = num[0]
			dividend = num[1]
		except:
			print('Syntax Error')
			print('Function', name_function, '( , ) expects 2 arguments')
			return None
		if dividend == 0:
			print('Math Error')
			print(name_function + '(' + str(quotient) + ',' + str(dividend) + ')')
			return None
		return float(quotient)/dividend
	#multiplication
	elif name_function == 'multiplication':
		try:
			num1 = num[0]
			num2 = num[1]
		except:
			print('Syntax Error')
			print('Function', name_function, '( , ) expects 2 arguments')
			return None
		return num1*num2
	#subtraction
	elif name_function == 'subtraction':
		try:
			num1 = num[0]
			num2 = num[1]
		except:
			print('Syntax Error')
			print('Function', name_function, '( , ) expects 2 arguments')
			return None
		return num1-num2
	#addition
	elif name_function == 'addition':
		try:
			num1 = num[0]
			num2 = num[1]
		except:
			print('Syntax Error')
			print('Function', name_function, '( , ) expects 2 arguments')
			return None
		return num1+num2
	#undefined	
	else:
		print('Syntax Error')
		print('Function', name_function, 'is not defined')
		return None
 
#string to float or int number
def number (string):
	#vetor
	pos_comma = string.find(',')
	if not pos_comma == -1:
		#find the terms in vector
		num1_start = findTerm(string,pos_comma,'L')
		num2_finish = findTerm(string,pos_comma,'R')
		if num1_start is None or num2_finish is None:
			return None
		num1 = number(string[num1_start:pos_comma])
		num2 = number(string[pos_comma+1:num2_finish+1])
		if num1 is None or num2 is None:
			return None
		#number to vector
		try:
			num1[0]
		except:#if not vector
			num1 = [num1]
		try:
			num2[0]
		except:#if not vector
			num2 = [num2]
		return num1 + num2 #concatenate vectors
	#if not vector
	#negative
	if string [0] == '-':
		signal=-1
		string = string[1:]
	else:
		signal=1
	try:
		num_float = float (string)
		num_int = int (num_float)
	except:
		#find varibles
		i=0
		while i < n_variables:
			if string == variables_names[i]:
				num_float = variables_value[i]
				try:
					num_int = int (num_float)
				except: #invalid value of variable
					return None
				break
			i+=1
		else:#invalid
			return None
	#integer
	if num_int==num_float:
		return num_int*signal
	#decimal 
	else:
		return num_float*signal

#expression of assignments
def assignments (string, pos_equal):
	if string[pos_equal+1:].find('=') is not -1: #Error, many assignments
			pos_equal += string[pos_equal+1:].find('=')+1
			print('Syntax Error')
			print(string[:pos_equal+1])
			return None
	else:
		#value
		variable_value = expression(string[pos_equal+1:])
		if variable_value is None:
			return None
		#name
		variable_name=string[:pos_equal]
		#name invalid if first digit is not character or not compound only numbers and characters
		if variable_name=='' or not variable_name[0].isalpha() or not variable_name.isalnum():
			print('Syntax Error')
			print('Variable', variable_name, 'is not valid')
			return None
		else:
			#save value in variable or creat a variable
			if saveVariable (variable_name,variable_value) is None:
				creatVariable(variable_name,variable_value)
			print(variable_name,'=',variable_value)
			return None

#expression in parentheses (function or expression)
def parentheses(string, par_start):
	#find the close parentheses
	par_close = parClose(string, par_start)
	if par_close == -1: #Error
		print('Error, not close (')
		print(string[:par_start+1])
		return None
	#find function (if exist) and your start
	func_start=par_start
	while func_start>0 and string[func_start-1].isalpha():#isalpha()->true if letter
		func_start-=1
	#expression, not a function
	if func_start == par_start :
		#replace the parentheses by number
		num = expression(string[par_start+1:par_close])
		if num is None: #Error
			return None
		else:
			string = string[:par_start] + str(num) + string[par_close+1:]
			return string
	#function, not a expression
	else:
		#save function name 
		name_function = string[func_start:par_start]
		#save number of parentheses
		num = expression(string[par_start+1:par_close])
		if num is None: #Error
			return None
		num = functions(name_function, num)
		if num is None: #Error
			return None
		string = string[:func_start] + str(num) + string[par_close+1:]
		return string

#exponent, exp_pos = position of operansion, exp start = position start the expoente
def exponent(string,exp_pos,exp_start):
	exp_finish = findTerm(string, exp_start-1, 'R')#find the variable or constante in the right
	base_finish = exp_pos - 1
	base_start = findTerm(string, exp_pos, 'L')#find the variable or constante in the left
	if base_start == None or exp_finish == None: #Error
		print('Syntax Error')
		print('Incorrect Exponent')
		print(string)
		return None
	base = number(string[base_start:base_finish+1])
	exp = number(string[exp_start:exp_finish+1])
	if base == None: #Error
		print('Syntax Error')
		print( string[base_start:base_finish+1], 'is not defined')
		return None
	elif exp == None: #Error
		print('Syntax Error')
		print( string[exp_start:exp_finish+1], 'is not defined')
		return None
	else:
		num = functions('pow',[base,exp])
		string = string[:base_start] + str(num) + string[exp_finish+1:]
		return (string)

#division, div_pos = position of operansion
def division(string,div_pos):
	dividend_finish = findTerm(string, div_pos, 'R')
	quotient_start = findTerm(string, div_pos, 'L')
	if dividend_finish == None or quotient_start == None: #Error
		print('Syntax Error')
		print('Incorrect Division')
		print(string)
		return None
	dividend = number(string[div_pos+1:dividend_finish+1])
	quotient = number(string[quotient_start:div_pos])
	if dividend == None: #Error
		print('Syntax Error')
		print( string[div_pos+1:dividend_finish+1], 'is not defined')
		return None
	elif quotient == None: #Error
		print('Syntax Error')
		print( string[quotient_start:div_pos], 'is not defined')
		return None
	num = functions('division',[quotient,dividend])
	if num == None:
		return None
	string = string[:quotient_start] + str(num) + string[dividend_finish+1:]
	return (string)

#division, mul_pos = position of operansion
def multiplication (string, mul_pos):
	num2_finish = findTerm(string, mul_pos, 'R')
	num1_start = findTerm(string, mul_pos, 'L')
	if num2_finish == None or num1_start == None: #Error
		print('Syntax Error')
		print('Incorrect Multiplication')
		print(string)
		return None
	num2 = number(string[mul_pos+1:num2_finish+1])
	num1 = number(string[num1_start:mul_pos])
	if num2 == None: #Error
		print('Syntax Error')
		print( string[mul_pos+1:num2_finish+1], 'is not defined1')
		return None
	elif num1 == None: #Error
		print('Syntax Error')
		print( string[num1_start:mul_pos], 'is not defined')
		return None
	num = functions('multiplication',[num1,num2])
	if num == None:
		return None
	string = string[:num1_start] + str(num) + string[num2_finish+1:]
	return (string)

#subtraction, sub_pos = position of operansion
def subtraction(string,sub_pos):
	num2_finish = findTerm(string, sub_pos, 'R')
	num1_start = findTerm(string, sub_pos, 'L')
	if num2_finish == None or num1_start == None: #Error
		print('Syntax Error')
		print('Incorrect Subtraction')
		print(string)
		return None
	num2 = number(string[sub_pos+1:num2_finish+1])
	num1 = number(string[num1_start:sub_pos])
	if num2 == None: #Error
		print('Syntax Error')
		print( string[sub_pos+1:num2_finish+1], 'is not defined')
		return None
	elif num1 == None: #Error
		print('Syntax Error')
		print( string[num1_start:sub_pos], 'is not defined')
		return None
	num = functions('subtraction',[num1,num2])
	if num == None:
		return None
	string = string[:num1_start] + str(num) + string[num2_finish+1:]
	return (string)

#addition, add_pos = position of operansion
def addition (string, add_pos):
	num2_finish = findTerm(string, add_pos, 'R')
	num1_start = findTerm(string, add_pos, 'L')
	if num2_finish == None or num1_start == None: #Error
		print('Syntax Error')
		print('Incorrect Addition')
		print(string)
		return None
	num2 = number(string[add_pos+1:num2_finish+1])
	num1 = number(string[num1_start:add_pos])
	if num2 == None: #Error
		print('Syntax Error')
		print( string[add_pos+1:num2_finish+1], 'is not defined1')
		return None
	elif num1 == None: #Error
		print('Syntax Error')
		print( string[num1_start:add_pos], 'is not defined')
		return None
	num = functions('addition',[num1,num2])
	if num == None:
		return None
	string = string[:num1_start] + str(num) + string[num2_finish+1:]
	return (string)

#expression
def expression (string):

	#assignments
	pos_equal = string.find('=')
	if pos_equal is not -1:
		num = assignments(string,pos_equal)
		if num is None:
			return None

	#open parentheses
	par_start = string.find('(')
	if par_start is not -1:
		string = parentheses(string,par_start)
		if string is None:
			return None
		else:
			return(expression(string))

	#exponent
	exp_pos = string.find('**')
	if exp_pos is not -1:
		exp_start = exp_pos+2
	else:
		exp_pos = string.find('^')
		exp_start = exp_pos+1
	if exp_pos is not -1:
		string = exponent(string,exp_pos,exp_start)
		if string is None:
			return None
		else:
			return(expression(string))

	#multiplication and division
	div_pos = string.find('/') 
	mul_pos = string.find('*') 
	#if the two operation happen, the first operation is priority
	#division
	if (mul_pos == -1 and not div_pos == -1) or ( not(mul_pos == -1 or div_pos == -1) and (mul_pos > div_pos)):
		string = division(string,div_pos)
		if string is None:
			return None
		else:
			return(expression(string))
	#multiplication 
	elif(not mul_pos == -1 and div_pos == -1) or ( not(mul_pos == -1 or div_pos == -1) and (mul_pos < div_pos)):
		string = multiplication(string,mul_pos)
		if string is None:
			return None
		else:
			return(expression(string))

	#number
	num = number (string)
	if num is not None:
		return num
	else:
		print('Syntax Error')
		print( string, 'is not defined')
		return None
		
	#addition and subtraction
	sub_pos = string.find('-')
	add_pos = string.find('+')  
	#if the two operation happen, the first operation is priority
	#subtraction
	if (add_pos == -1 and not sub_pos == -1) or ( not(add_pos == -1 or sub_pos == -1) and (add_pos > sub_pos)):
		string = subtraction(string,sub_pos)
		if string is None:
			return None
		else:
			return(expression(string))
	#addition 
	elif(not add_pos == -1 and sub_pos == -1) or ( not(add_pos == -1 or sub_pos == -1) and (add_pos < sub_pos)):
		string = addition(string,add_pos)
		if string is None:
			return None
		else:
			return(expression(string))


#===================================MAIN
while 1:
	command = input('> ')

	#exit
	if command == 'quit': 
		break
	#enter
	elif command == '': 
		continue
	#print(
	elif command.startswith('say '): 
		print((command[4:]))
	#clear
	elif command == 'clear' or command == 'clc':
		os.system('cls' if os.name=='nt' else 'clear') #windown and linux
	#clear
	elif command.startswith('help'): 
		command = command.replace(' ','')#remove the spaces
		printHelp(command[4:])
	else:
		#expression
		command = command.replace(' ','')#remove the spaces
		num=expression(command)
		if num is not None:
			saveVariable('ans',num)
			print((num))

		#Erro of syntax
		#else:
			


		


