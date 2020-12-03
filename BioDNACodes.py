empty = ""
source = input("Your code:")
for i in source:
	if i == "A":
		empty += "U"
	if i == "T":
		empty += "A"
	if i == "C":
		empty += "G"
	if i == "G":
		empty += "C"

print("This is your code --> " + empty)