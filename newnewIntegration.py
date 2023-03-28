# Ryley Wright
# Sorry I ended up doing a quiz.
# All code is made up by me based on experience in the classroom and doing the POGIL worksheets

# needed to use the square root function
import math


# creating a function to be used in one of the questions later
def get_half_of_root(x):
    squareRoot = math.sqrt(x)
    half_of_root = squareRoot / 2
    return half_of_root


def main():
    # defining variable to be adjusted based on their results
    grade = 0
    # Looping them back through if they do poorly to try again
    while grade < 75:
        # keeping track of the number of questions they get correct by adding one to the variable each time
        answersCorrect = 0
        numberofQuestions = 0
        print("Thank you for taking this quiz it will be 8 questions long")

        # asking question and getting answer then casting that answer as an integer
        answer1 = float(input("What is 4 plus 5?"))
        numberofQuestions = numberofQuestions + 1
        # If they answer (using an integer) it tells them if they are right or wrong.
        # First question is addition
        if answer1 == 4 + 5:
            answersCorrect = answersCorrect + 1
            print("That's correct!")
        else:
            print("Sorry that's incorrect")

        # second question uses subtraction.
        answer2 = float(input("What is 17 minus 12"))
        numberofQuestions = numberofQuestions + 1
        if answer2 == 17 - 12:
            answersCorrect = answersCorrect + 1
            print("Way to go!")
        else:
            print("Sorry that's not right")

        # Third question uses multiplication
        answer3 = float(input("What is 3 times 15"))
        numberofQuestions = numberofQuestions + 1
        if answer3 == 3 * 15:
            answersCorrect = answersCorrect + 1
            print("Nice job!")
        else:
            print("Maybe next time...")

        # Fourth question taking the power of something
        answer4 = float(input("What is 5 to the 3rd power?"))
        numberofQuestions = numberofQuestions + 1
        if answer4 == 5 ** 3:
            answersCorrect = answersCorrect + 1
            print("Excellent!")
        else:
            print("Not quite")

        # Fifth question involves taking floor division
        answer5 = float(input("If you have 10 batteries and a flashlight uses 3, how many can you fill?"))
        numberofQuestions = numberofQuestions + 1
        if answer5 == 10 // 3:
            answersCorrect = answersCorrect + 1
            print("Genius!")
        else:
            print("Wrong answer")

        # Sixth question uses modulus
        answer6 = float(input("From the previous question, how many batteries would you have remaining?"))
        numberofQuestions = numberofQuestions + 1
        if answer6 == 10 % 3:
            answersCorrect = answersCorrect + 1
            print("Good job!")
        else:
            print("Not right this time...")

        answer7 = float(input("If I have $25 and spend $1.50 how much do I have?"))
        numberofQuestions = numberofQuestions + 1
        if answer7 == 25 - 1.5:
            answersCorrect = answersCorrect + 1
            print("Thats right!", end=" ")
        else:
            print("Rough question...")
        # Added end so that it would appear in the same line as the next section.
        print("Don't give up yet!")

        answer8 = input("What has a mouth but never eats, and has a bed but never sleeps?")
        numberofQuestions = numberofQuestions + 1
        # Providing two possible answers depending on whether or not they capitalize.
        if answer8 == "river" or answer8 == "River":
            answersCorrect = answersCorrect + 1
            print("Keep it up!")
        else:
            print("Better luck next time!")

        # This question uses the function get_half_of_root that was made at the beginning
        answer9 = int(input("What is half of the square root of 36?"))
        numberofQuestions = numberofQuestions + 1
        if answer9 == get_half_of_root(36):
            answersCorrect = answersCorrect + 1
            print("Fantastic!")
        else:
            print("Thats not it")

        # uses for loop in range to perform print a certain number of times
        numberofQuestions = numberofQuestions + 1
        for x in range(0, 6):
            print("x")
        answer10 = int(input("How many times did you just see the letter x?"))
        if answer10 == 6:
            answersCorrect = answersCorrect + 1
            print("Way to finish strong!")

        # used this instead of else for requirements.
        elif answer10 != 6:
            print("Sorry not right")

        # Creating another variable for the percentage and setting it to one decimal place.
        grade = float(format(answersCorrect / numberofQuestions * 100, ".1f"))
        # Stating their grade for them and using the sep= argument to separate strings
        if answersCorrect >= 9 and not answersCorrect > 10:
            print("You scored: " + str(grade), " nice job!", sep="%")
        elif 7 <= answersCorrect < 9:
            print("You scored: " + str(grade), " Not bad but you can do better!", sep="%")
        else:
            print("You scored: " + str(grade), " Try again!", sep="%")
    # Last line is just decoration and to meet the requirements
    print("Congrats" * 10)


main()
