
question_bank = {
    "easy": {
        "maths": [
            {
                "question": "Which of these is the percentage symbol?",
                "options": ["$", "%", "&", "#"],
                "correct": 1
            },
            {
                "question": "How many sides does an octagon have?",
                "options": ["6", "7", "8", "9"],
                "correct": 2
            },
            {
                "question": "What is 25 x 4?",
                "options": ["50", "75", "100", "125"],
                "correct": 2
            },
            {
                "question": "What is the square root of 121?",
                "options": ["9", "10", "11", "12"],
                "correct": 2
            },
            {
                "question": "How many degrees do the angles of a triangle add up to?",
                "options": ["90", "180", "270", "360"],
                "correct": 1
            },
            {
                "question": "If it is currently 8 a.m, in how many hours will it be 5 p.m?",
                "options": ["7", "8", "9", "10"],
                "correct": 2
            },
            {
                "question": "What is the area of a square with width and length of 6cm?",
                "options": ["12", "24", "36", "48"],
                "correct": 2
            }
        ],

        "science": [
            {
                "question": "How many chambers does the heart have?",
                "options": ["2", "3", "4", "5"],
                "correct": 2
            },
            {
                "question": "Which of these is a noble gas?",
                "options": ["Oxygen", "Nitrogen", "Helium", "Hydrogen"],
                "correct": 2
            },
            {
                "question": "What is the pH of pure water?",
                "options": ["5", "6", "7", "8"],
                "correct": 2
            },
            {
                "question": "What is the biggest organ of the human body?",
                "options": ["Spleen", "Heart", "Brain", "Skin"],
                "correct": 3
            },
            {
                "question": "What letter is missing in the formula ' =mc**2'",
                "options": ["R", "E", "V", "T"],
                "correct": 1
            },
            {
                "question": "Which of these is a characteristic of a *malleable* metal?",
                "options": ["Soft", "Brittle", "Dull", "Shiny"],
                "correct": 0
            },
            {
                "question": "What mineral are bones made of?",
                "options": ["Carbon", "Sodium", "Adamantium", "Calcium"],
                "correct": 3
            }
        ],

        "general": [
            {
                "question": "How many colours are there in a rainbow?",
                "options": ["5", "6", "7", "8"],
                "correct": 2
            },
            {
                "question": "Which of these is NOT a desert?",
                "options": ["Sahara", "Gobi", "Amazon", "Kalahari"],
                "correct": 2
            },
            {
                "question": "How many continents are there?",
                "options": ["7", "5", "6", "9"],
                "correct": 0
            },
            {
                "question": "What Video Game character loves mushrooms, saves a princess and hates turtles?",
                "options": ["Sonic", "Pac-Man", "Mario", "Link"],
                "correct": 2
            },
            {
                "question": "What is the biggest planet in our solar system?",
                "options": ["Mars", "Jupiter", "Saturn", "Pluto"],
                "correct": 1
            },
            {
                "question": "What do pandas like to eat?",
                "options":  ["Seaweed", "People", "Bamboo", "Humans"],
                "correct": 2
            },
            {
                "question": "How many legs does a centipede have?",
                "options": ["100", "50", "250", "500"],
                "correct": 0
            }
        ]
    },

    "hard": {
        "maths": [
            {
                "question": "If 13x + 6 = 123, what is the value of x?",
                "options": ["7", "8", "9", "10"],
                "correct": 2
            },
            {
                "question": "What is 5 x 6 + (45 - 13) / 4?",
                "options": ["39", "41", "42", "45"],
                "correct": 1
            },
            {
                "question": "Using the the pythagorean theorem, what is the value of b if a = 2 and c = 9 rounded to the nearest whole number?",
                "options": ["9", "6", "10", "3"],
                "correct": 0
            },
            {
                "question": "There are 49 dogs in a park. There 36 more small dogs than large dogs. how many small dogs are there?",
                "options": ["43", "48.7", "39", "42.5"],
                "correct": 3
            },
            {
                "question": "What is 3/8 x 8/3?",
                "options": ["2", "64/9", "1", "4"],
                "correct": 2
            },
            {
                "question": "What is 15% of 255?",
                "options": ["38.25", "75", "55.35", "23.74"],
                "correct": 0
            }
        ],

        "science": [
            {
                "question": "How many alleles are needed for a recessive trait?",
                "options": ["2", "6", "2", "4"],
                "correct": 1
            },
            {
                "question": "What does an individual carry if they are positive for 'RF'?",
                "options": ["Red-less Factor", "Rhymestyle Factor", "Rheumatoid Factor", "Richtereon Factor"],
                "correct": 2
            },
            {
                "question": "True or false: Our solar system would be completely fine if the suns gravitational pull were to become stronger or weaker.",
                "options": ["True", "False"],
                "correct": 1
            },
            {
                "question": "Which of these is the cause of a black hole?",
                "options": ["A drill that pierces heaven", "The inverse rotation of a suns core", "A collapsing star", "The collision of 2 stars"],
                "correct": 2
            },
            {
                "question": "What is the speed of light?",
                "options": ["3x10^8", "3x10^9", "2X10^10", "4x10^4"],
                "correct": 0
            },
            {
                "question": "What is the process in which metal becomes rusty due to oxygen?",
                "options": ["Corrosion", "Reduction", "Rustification", "Oxidation"],
                "correct": 3
            },
            {
                "question": "Which of these are the bases within the DNA's structure?",
                "options": ["B,U,D,H", "A,R,S,P", "A,T,C,G", "J,Z,L,E"],
                "correct": 2
            }
        ]
    }
}

previous_score = []
def quiz(question_bank, difficulty, topic):
    import random

    selected_pool = question_bank[difficulty][topic]
    num_questions = min(5, len(selected_pool))
    quiz_questions = random.sample(selected_pool, num_questions)

    score = 0

    for i, q in enumerate(quiz_questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")

        for index, option in enumerate(q["options"], start=1):
            print(f"{index}. {option}")

        while True:
            try:
                user_answer = int(input("Enter your answer (1–4): "))
                if 1 <= user_answer <= 4:
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")

        user_answer -= 1

        if user_answer == q["correct"]:
            print("Correct! ")
            score += 1
        else:
            print(f"Wrong...")

    print(f"\nQuiz complete! Final score: {score}/{num_questions}\n")
    if score <3:
        print("Maybe pick a different topic next time...")
    elif score == 3:
        print("Aye, you did pretty good!")
    else:
        print("Wow, maybe you should've made this quiz instead! You really know your stuff!!!")
    previous_score.append(score)
    return score

while True:
    menu_choice = int(input("Welcome to the Quiz!\nPlease select if you'd like to (1-3): \n1. Start quiz\n2. See previous Scores\n3. Quit Program\n"))
    if menu_choice == 1:
        difficulty = input("Select your difficulty: \nEasy \nHard\n")
        difficulty = difficulty.lower()
        if difficulty == "easy":
            print("Wow so you just dont want to try huh? Ok... ")
        else:
            print("Good luck, have fun!")
        topic = input("Select your topic (please note that hard mode does not have general questions): \nMaths \nScience \nGeneral\n")
        topic = topic.lower()
        quiz(question_bank, difficulty, topic)
    elif menu_choice == 2:
        print(f"Here are your previous scores: {previous_score}")
    elif menu_choice == 3:
        print("Thanks for playing if ya' did :D! Cya!")
        break
    else:
        print("Doesnt really look like a valid number now does it. -_-\n Lets try that again\n")

