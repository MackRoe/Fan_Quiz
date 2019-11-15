# fan quiz to run in Terminal
import random


# def random_question():
#     """ STRETCH - get a random question from list of questions """
#     pass


def get_question():
    ''' read question from file to variable
        return a string '''
#     """ STRETCH - return a random question """
#     new_question = random_question()
    return "GOT"


def number_the_question():
    question_number = "#"
    """ assign the sequential numbering of a question """
    return question_number


def test_answer():
    """ determine if correct answer to question was givin """
    pass


def question_answers():
    list_answers = ['a', 'b', 'c']
    return list_answers

''' -- STRETCH --
# def automate_questions():
#     pass

# --Concatonate the function call from variables --
# def call_question():
#     pass '''

def question1():
    print(str(number_the_question()) + get_question())
    print(question_answers())
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
