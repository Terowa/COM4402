choice = int(input("Type the number of your choice: \n 1. Start Quiz, 2. See Scores"))
if choice == 2:
        print(f"Here are is previous score previous score")
elif choice == 1:
    topic_choice = int(input("Select a topic by typing 1,2 or 3 \n 1. Maths, 2. Geography or 3. General Knowledge"))
    match topic_choice:
        case 1: print ("You have chosen Maths as your topic")
        case 2: print ("You have chosen geography as your topic")
        case 3: print ("You have chosen General Knowledge as your topic")
    difficulty_choice = int(input("Select difficulty by typing 1,2 or 3: \n 1. Easy, 2. Hard "))
    match difficulty_choice:
        case 1: print ("So you decided to take the easy route...")
        case 2: print ("Your road may be treacherous and hard...")
else:
    print ("Does that look like one of the the options -_-...")