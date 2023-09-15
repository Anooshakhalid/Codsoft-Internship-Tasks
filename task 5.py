# Task 5
# Quiz Game

# function for store the variables
def quiz_questions(question=0, options=0, right_answer=0):
    return question, options, right_answer


# function to check the player answer with correct answer
def check_answer(player_answer, right_answer):
    return player_answer == right_answer


# function to create a list and append questions in it
def quizz_score(question):
    mcqs = []
    mcqs.append(question)


# function to keep track the score and give the feedback
def play_quiz(questions):
    quiz_score = 0
    total_ques = len(questions)

    for i, (question, options, right_answer) in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question}")
        for j, user_choice in enumerate(options, 1):
            print(f"{j}. {user_choice}")
        player_answer = int(input("Enter the right option number: "))

        if 1 <= player_answer <= len(options):
            if check_answer(right_answer, player_answer):
                print(f"Good job {user_name}\nCorrect Answer!")
                quiz_score += 1
            else:
                print(f"Oops! That's the Incorrect Answer.\nThe correct answer is option {right_answer}")
        else:
            print("Invalid option!\nPlease select a option number.")
    print(f"\nQuiz Finished. Your score: {quiz_score}/{total_ques}")

    if quiz_score == 6:
        print(f'Well done!! You did it {user_name}')

    elif quiz_score == 5:
        print(f'Nice!...Keep it up {user_name}')

    elif quiz_score == 1 or quiz_score == 0:
        print(f"Don't be disheart {user_name}.You can do it!")

    elif 2<= quiz_score <= 4:
        print(f'Not bad! Better luck next time {user_name}')

    print('Thanks for playing!!')


# main program
# quiz questions
gk_questions = [("Rainbows consist of how many colors?", ["Six colors", "Seven colors", "Eight colors"], 2),
                ("Name the smallest continent?", ["Africa", "Europe", "Australia"], 3),
                ("How many days a February month has in the leap year?", ["29", "30", "28"], 1),
                ("Name a bird that lays the largest eggs?", ["Hen", "Duck", "Ostrich"], 3),
                ("What is the capital of Japan?", ["Rome", "Baku", "Tokyo"], 3),
                ("Which is the longest River in the world?", ["Amazon", "Nile", "Indus"], 2)]

maths_questions = [("What is 121 x 0 x 20 x 2.5?", ["0", "132", "50"], 1),
                   ("What is 7 + 3?", ["8", "10", "11"], 2),
                   ("What is the value of pi?", ["2.144", "3.678", "3.142"], 3),
                   ("What is 10% of 100?", ["12", "20", "10"], 3),
                   ("121 Divided by 11 is?", ["11", "19", "10"], 1),
                   ("The perfect cube of 27 is?", ["4", "3", "6"], 2)]

islamic_questions = [("How many daily prayers are there in Islam?", ["Three", "Four", "Five"], 3),
                     ("What is the Muslims' special festival", ["Holi", "Eid", "Christmas"], 2),
                     ("What is the name of the month of fasting in Islam?", ["Ramadan", "Shawwal", "Muharram"], 1),
                     ("Holy Kaaba is situated in which country?", ["Saudi Arabia", "India", "Pakistan"], 1),
                     ("What is the meaning of the word 'Salaam' in Islam?", ["Prayer", "Fasting", "Peace"], 3),
                     ("How many Pillars of Islam are there?", ["5", "4", "3"], 1)]

# main interface
print("**---*---** WELCOME TO QUIZ GAME **---*---**\n")
print("Game Rules:")
print('* The quiz consists of six multiple-choice options.')
print('* Players must select one option for each question.')
print('* Each question has only one correct answer.')
print('* Players are awarded points for correct answers and there is no negative marking.')

user_name = input('\nEnter your name:')

# loop to choose the quiz which the player want to play
while True:
    print('Which topic do you prefer to play?')
    print("1- General Knowledge")
    print("2- Maths")
    print("3- Islamic")
    choice = int(input('Please Enter your choice:'))
    print(f'\nGoodluck {user_name}!')

    if choice == 1:
        play_quiz(gk_questions)

    elif choice == 2:
        play_quiz(maths_questions)

    elif choice == 3:
        play_quiz(islamic_questions)

    else:
        print('Pls choose a right option!')
        continue

# restart the game if the user wants
    replay = input('\nDo you wanna play again?\nPress "y" for YES or Press any other key for EXIT: ')
    if replay == 'y' or replay=='Y':
        print("\nLet's play again!!")
        continue

    else:
        print(f'Goodbye {user_name}!\nHope you enjoyed it:)')
        exit()



