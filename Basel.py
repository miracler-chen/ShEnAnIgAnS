def basel():
	inte = 0
	eq = 0
	ask = int(input("How many time do you want n to iterate(Please type an integer): "))
	while inte != ask:
		inte += 1
		eq += (1 / (inte **2 ))
	
	return eq

print(basel())