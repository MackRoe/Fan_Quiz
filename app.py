# fan quiz to run in Terminal


def question1():
    rating = 0
    question1_text = "1. Name the park where most of the vampires hang out."
    question1_answers = ['a) Fair Oaks Park', 'b) Weatherly Park', 'c) Mission City Memorial Park']
    question1_trivia = "In 'The Pack', the pack minus Xander slept there after they ate Principal Flutie. According to the book 'The Watcher's Guide Volume 1', the gates to Weatherly Park are closed at 10 p.m."
    print(question1_text)
    print('')
    for answer in question1_answers:
        print(answer)
    print('')
    # print(question_answers(question_number))
    response = input("Enter one letter for your answer [A, B, or C]:")
    print('')
    print('You answered: ' + str(response))
    if response.upper() == 'B':
        print("Your answer is CORRECT")
        print('')
        print(question1_trivia)
        rating += 1
    elif response.upper() == 'A' or response.upper() == 'C':
        print("The correct answer was B (Weatherly Park)")
        print('')
        print(question1_trivia)

    else:
        print("Try Again!")
        response = input("Enter one letter for your answer [A, B, or C]: ")
    print("rating: " + str(rating))
    return rating


def question2():

    question2_text = "2. What is the name of the city where the show takes place?"
    question2_answers = ['a) Sunnyvale', 'b) Sunnyville', 'c) Sunnydale']
    question2_trivia = "The show is set in the fictional California town of Sunnydale, whose suburban Sunnydale High School sits on top of a 'Hellmouth', a gateway to demon realms."
    print(question2_text)
    print('')
    for answer in question2_answers:
        print(answer)
    print('')
    # print(question_answers(question_number))
    response = input("Enter one letter for your answer [A, B, or C]:")
    print('')
    print('You answered: ' + str(response))
    if response.upper() == 'C':
        print("Your answer is CORRECT")
        print('')
        print(question2_trivia)
        rating = 1
    elif response.upper() == 'A' or response.upper() == 'B':
        print("The correct answer was C (Sunnydale)")
        print('')
        print(question2_trivia)
        rating = 0
    else:
        print("Try Again!")
        response = input("Enter one letter for your answer [A, B, or C]: ")
    print("rating: " + str(rating))
    return rating


def question3():

    question3_text = "3. Buffy's group of friends was called 'Scooby Snacks'"
    question3_trivia = "The group was first referred to as the SCOOBY GANG by Xander Harris in the Season Two episode 'What's My Line, Part One' as a reference to the group of monster-hunting teenagers from the Hanna-Barbera animated series Scooby-Doo"
    print(question3_text)
    print('')
    response = input("True or False? [T or F]:")
    print('')
    print('You answered: ' + str(response))
    if response.upper() == 'F':
        print("Your answer is CORRECT")
        print('')
        print(question3_trivia)
        rating = 1
    elif response.upper() == 'T':
        print("The correct answer was F (False)")
        print('')
        print(question3_trivia)
        rating = 0
    else:
        print("Try Again!")
        response = input("Enter one letter for your answer [T or F]: ")
    print("rating: " + str(rating))
    return rating


def question4():
    question4_text = "4. How many Slayers are there?"
    question4_answers = ['a) one girl in all the world', 'b) two', 'c) at least 1800']
    question4_trivia = "The mystical 'rules' governing the Calling of Slayers changed in 2003. Willow Rosenberg uses magic to tap into the Slayer's Scythe's essence at Buffy's request, and performs a spell that calls every living Potential Slayer at once, thus ending the legacy of 'one girl in all the world'. \n After taking the time to find and count them, Buffy states that there are at least 1800 Slayers in the world"
    print(question4_text)
    print('')
    for answer in question4_answers:
        print(answer)
    print('')
    # print(question_answers(question_number))
    response = input("Enter one letter for your answer [A, B, or C]:")
    print('')
    print('You answered: ' + str(response))
    if response.upper() == 'C':
        print("Your answer is CORRECT")
        print('')
        print(question4_trivia)
        rating = 1
    elif response.upper() == 'A' or response.upper() == 'B':
        print("The correct answer was C (at least 1800)")
        print('')
        print(question4_trivia)
        rating = 0
    else:
        print("Try Again!")
        response = input("Enter one letter for your answer [A, B, or C]: ")
    print("rating: " + str(rating))
    return rating


def question5():
    question5_text = "5. Willow, during her dark phase, was refered to as 'Dark Pheonix'."
    question5_trivia = "Buffy's plan (in episode: Two to Go), to run away from Evil Willow, doesn't fly with Andrew, who replies, 'Are you kidding? She's like Dark Phoenix up there!' "
    print(question5_text)
    print('')
    response = input("True or False? [T or F]:")
    print('')
    print('You answered: ' + str(response))
    if response.upper() == 'T':
        print("Your answer is CORRECT")
        print('')
        print(question5_trivia)
        rating = 1
    elif response.upper() == 'F':
        print("The correct answer was T (True)")
        print('')
        print(question5_trivia)
        rating = 0
    else:
        print("Try Again!")
        response = input("Enter one letter for your answer [T or F]: ")
    print("rating: " + str(rating))
    return rating


def calc_rating():
    rating = 0
    if question1() == 1:
        rating += 1
    if question2() == 1:
        rating += 1
    if question3() == 1:
        rating += 1
    if question4() == 1:
        rating += 1
    if question5() == 1:
        rating += 1
    print("Calculated Rating is: " + str(rating))
    return rating


def fan_rating():
    rating = calc_rating()
    print("You've answered all the questions and have earned the title:")
    if rating == 5:
        title = "SOVEREIGN You've seen maximum Buffy"
    elif rating == 4:
        title = "ROYALTY You've seen a lot of Buffy"
    elif rating == 3:
        title = "ELITE You've seen a significant amount of Buffy"
    elif rating == 2:
        title = "COMMONER You've seen some Buffy"
    else:
        title = "PAUPER You should watch Buffy. It's a good series."
    print(title)


def run_quiz():
    print('##################################')
    print('########  Buffy Fan Quiz  ########')
    print('##################################')

    fan_rating()


run_quiz()
