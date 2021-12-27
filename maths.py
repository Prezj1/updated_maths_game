import random

MIN_NUMBER = 1
MAX_NUMBER = 10
NB_QUESTIONS = 5
nb_points = 0

def ask_question():
    count = 1
    while count < NB_QUESTIONS + 1:
        o = random.randint(0,1)
        a = random.randint(MIN_NUMBER, MAX_NUMBER)
        b = random.randint(MIN_NUMBER, MAX_NUMBER)
        global nb_points
        average = int(NB_QUESTIONS / 2)
        operator_str = "+"
        if o == 1:
            operator_str = "*"
        print(f"Question no {count} out of {NB_QUESTIONS}")
        print(" ")
        answer_str = input(f"Please compute the numbers {a} {operator_str} {b}: ")
        answer_int = int(answer_str)
        compute = a+b
        if o == 1:
            compute = a*b
        if answer_int == compute:
            nb_points += 1
            print(f"You are correct. Your current points are {nb_points} out of {NB_QUESTIONS}")
        else:
            print(f"You are wrong. You current points are {nb_points} out of {NB_QUESTIONS}")
        
        count += 1
        print("")
    
    if nb_points == NB_QUESTIONS:
        print("Excellent work")
    elif nb_points > average:
        print("Good result")
    elif nb_points < average:
        print("You can do better")
    elif nb_points == 0:
        print("You need to improve your maths")


ask_question()
