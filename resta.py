def resta(op1, op2):
	resta = ""
	op1_index = op1.index(".") 
	op2_index = op2.index(".")

	op1_a = len(op1[op1_index + 1:])
	op2_b = len(op2[op2_index + 1:])
	op1_punto = op1[op1_index + 1:] 
	op2_punto = op2[op2_index + 1:]

	operador1 = op1[::-1]
	operador2 = op2[::-1]

	a_op1 = op1[:op1_index]
	b_op1 = op1_punto

	a_op2 = op2[:op2_index]
	b_op2 = op2_punto

	mayor = 0
	up = ""
	down = ""

	if len(a_op1) == len(a_op2):
		if float(op1) - float(op2) > 0:
			mayor = 0
		else:
			mayor = 1
	elif len(a_op1) > len(a_op2):
		a_op2 = a_op2.zfill(len(a_op1))
		mayor = 0 #Saber si el operador 1 es mayor en longitud
	elif len(a_op2) > len(a_op1):
		a_op1 = a_op1.zfill(len(a_op2))
		mayor = 1 #Saber si el operador 2 es mayor en longitud

	if len(b_op1) > len(b_op2):
		b_op2 = b_op2[::-1]
		b_op2 = b_op2.zfill(len(b_op1))
		b_op2 = b_op2[::-1]
	elif len(b_op2) > len(b_op1):
		b_op1 = b_op1[::-1]
		b_op1 = b_op1.zfill(len(b_op2))
		b_op1 = b_op1[::-1]

	c_op1 = a_op1 + "." + b_op1
	c_op2 = a_op2 + "." + b_op2

	#Numero de mayor largo antes del punto queda como up
	if mayor == 0:
		up = c_op1[::-1]
		down = c_op2[::-1]
	else:
		up = c_op2[::-1]
		down = c_op1[::-1]

	acarreo = 0
	for z in range(len(up)):
		if up[z] != '.':
			if acarreo == 0:
				x = int(up[z]) - int(down[z])
				if x == -1:
					acarreo = 1
					resta = resta + "1"
				elif x == 1:
					resta = resta + "1"
				elif x == 0:
					resta = resta + "0"
			elif acarreo == 1:
				x = int(up[z]) - 1
				acarreo = 0
				if x == -1:
					x = 1
					acarreo = 1
					x = x - int(down[z])
					if x == 1:
						resta = resta + "1"
					elif x == 0:
						resta = resta + "0"
				elif x == 0:
					x = x - int(down[z])
					if x == -1:
						acarreo = 1
						resta = resta + "1"
					elif x == 0:
						resta = resta + "0"
		else:
			resta = resta + '.'
	#print(up[::-1],down[::-1],sep="\n")
	resta = resta[::-1]
	while(resta[0] == "0"):
		resta = resta[1:]
		if resta[0] == ".":
			resta = "0" + resta
			break
	if float(operador1[::-1]) - float(operador2[::-1]) < 0:
		resta = "-" + resta
	return resta
if __name__ == '__main__':
	print(resta("10101.101", "1011.11"))
	print(resta("1101011.1100001", "11010101.101"))
	print(resta("1001.111", "1011111.1111111"))
	print(resta("1111.01", "1111.11"))
	print(resta("111.111", "1111.111"))