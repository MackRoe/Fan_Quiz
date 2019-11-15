# fan quiz to run in Terminal

def question1():
    # print(str(number_the_question()) + get_question())
    question1_text = "1. Name the park where most of the vampires hang out."
    question1_answers = ['a) Fair Oaks Park', 'b) Weatherly Park', 'c) Mission City Memorial Park']
    question1_trivia = "In 'The Pack', the pack minus Xander slept there after they ate Principal Flutie. According to the book 'The Watcher's Guide Volume 1', the gates to Weatherly Park are closed at 10 p.m."
    print(question1_text)
    for answer in question1_answers:
        print(answer)
    # print(question_answers(question_number))
    response = input("Enter one letter for your answer [A, B, or C]:")
    print('You answered: ' + str(response))
    if response.upper() == 'B':
        print("Your answer is CORRECT")
        print(question1_trivia)
        correct = 1
    elif response.upper() == 'A' or upper(response) == 'C':
        print("The correct answer was B (Weatherly Park)")
        print(question1_trivia)
        correct = 0
    else:
        print("Try Again!")
        response = input("Enter one letter for your answer [A, B, or C]: ")
    return correct


def question2():
    pass


def question3():
    pass


def question4():
    pass


def question5():
    pass


def start_quiz():
    question1()


start_quiz()
