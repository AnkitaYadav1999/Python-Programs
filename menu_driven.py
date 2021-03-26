def mainMenu():
    print("1. For Good")
	print("2. For Bad")
	print("3. Exit")
	selection = int(input("Enter Your Choice: "))
	if selection==1:
		good()
	elif selection==2:
		bad()
	elif selection==3:
		exit()
	else:
		print("Invlaid Choice. Enter 1-3")

    
