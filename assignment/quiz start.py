
question_bank = {
    "easy" : {
        "Maths" : "Hallo",
        "Science" : "Evry",
        "General" : "Nyan"
    },
    "hard" : {
        "Maths" : "How r yu?",
        "Science" : "Fine sank yu"
    }
}
def question_select():
    for i in questions:
      answer = int(input(f"{i}\n"))

def quiz():
    print (f"Question {question_counter}:\n 1")

score = 0
question_counter = 1
choice = int(input("Type the number of your choice: \n 1. Start Quiz, 2. See Scores\n"))
if choice == 2:
        print(f"Here are is previous score previous score\n")
elif choice == 1:
    difficulty_choice = int(input("Select difficulty by typing 1,2 or 3: \n 1. Easy, 2. Hard\n"))
    match difficulty_choice:
        case 1:
            print ("So you decided to take the easy route...")
            difficulty = question_bank.get["easy"]
            topic_choice = int(input("Select a topic by typing 1,2 or 3 \n 1. Maths\n 2. Science/Body \n 3. General Knowledge\n"))
        case 2:
            print ("Your road may be treacherous and hard...")
            difficulty = question_bank.get["hard"]
            topic_choice = int(input("Select a topic by typing 1 or 2.\n 1. Maths\n 2. Science/Body\n"))
            match topic_choice:
                case 1:
                    print ("You have chosen Maths as your topic")
                    questions = question_bank.ge["Maths"]
                case 2:
                    print ("You have chosen geography as your topic")
                    questions = question_bank.get["Science"]
                case 3:
                    print ("You have chosen General Knowledge as your topic")
                    questions = question_bank.get["General"]
while question_counter < len(question_bank):
    quiz()
else:
    print("Does that look like one of the the options -_-...")