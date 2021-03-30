while True:
    print("1.Breakfast ")
    print("2.Dinner")
    print("3.Drinks")
   

    choice = int(input("Enter Your Choice: "))

    if (choice == 1):
        print("\n 1. pohe")
        print("\n 2. upma")
        select = int(input("\n\n enter breakfast u want: "))
        if select == 1:
            print("\n pohe: 20 Rs plate\n\n")
        elif select == 2:
            print("\n upma: 30 Rs plate\n\n")
        
       
    elif(choice == 2):
        print("\n 1. chikan")
        print("\n 2. biryani")
        select = int(input("\n\n enter dinner u want: "))
        if select == 1:
            print("\n chikan: 120 Rs plate\n\n")
        elif select == 2:
            print("\n biryani: 135 Rs plate\n\n")
        
    elif(choice == 3):
        print("\n 1. tea")
        print("\n 2. coffee")
        select = int(input("\n\n enter drink u want: "))
        if select == 1:
            print("\n tea: 10 Rs\n\n")
        elif select == 2:
            print("\n coffee: 15 Rs\n\n")
        
            
   
    else:
        print("\n\n Sorry, Your Choice Is Wrong")
    
    
