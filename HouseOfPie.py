pieList = ["Pecan", "Apple Crisp", "Bean", "Banoffee","Black Bun","Blueberry", "Buko","Burek","Tamale","Steak"]

piePurchase=[]
print("Welcome to the House of Pies! Here are our pies:")
print("-----------------------------------------------------")
entry=""
for pie in pieList:
	entry =  entry +  ("(" + str(pieList.index(pie)+1) + ") " + pie+ ",")


print (entry)

order = "y"
while order =="y":
	pie_choice = input("Which pie would you like to order?")
	print ("Great! We'll have that " + pieList[int(pie_choice)-1] + " right out for you.")
	piePurchase.append(pie_choice-1)
	order = input("Would you like to order another pie?")

print ("you purchased total "+ str(len(piePurchase)) +" pies")

#for pie_index in range 