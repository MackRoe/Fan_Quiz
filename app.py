# fan quiz to run in Terminal

def question1():
    # print(str(number_the_question()) + get_question())
    question1_text = "1. Name the park where most of the vampires hang out."
    question1_answers = ['a) Fair Oaks Park', 'b) Weatherly Park', 'c) Mission City Memorial Park']
    print(question1_text)
    for answer in question1_answers:
        print(answer)
    # print(question_answers(question_number))
    response = input("Enter one letter for your answer [A, B, or C]:")
    print('You answered: ' + str(response))


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
