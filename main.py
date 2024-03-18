#Defining function that eliminates the between spaces

def remove_between_space(answer):
    after_removing_space=answer.replace(" ","")
    return after_removing_space


print("Welcome to my Quiz!!")
decision = input("Are you wanted to play the game? (Yes or No) ")
decision = remove_between_space(decision)
correctAnswerCount = 0
totalQuestion = 5

if decision.lower() == "yes":
    print(''' You Have to Answer 5 Questions
              Each Question has 2 points
              0.25 marks cut if answer is negative
              Lets go........ 
          ''')
else:
    quit()

answer = input("Question: What is the capital city of France? - ")
answer=remove_between_space(answer)
if answer.lower().strip() == "paris":
    print("correct")
    correctAnswerCount += 1
else:
    print("wrong")

answer = input("Question:  Which planet is known as the Red Planet? - ")
answer=remove_between_space(answer)
if answer.lower().strip() == "mars":
    print("correct")
    correctAnswerCount += 1
else:
    print("wrong")

answer = input("Question: Who painted the Mona Lisa? - ")
answer=remove_between_space(answer)
if answer.lower().strip() == "leonardo da vinci":
    print("correct")
    correctAnswerCount += 1
else:
    print("wrong")

answer = input("Question: What is the largest organ in the human body? - ")
answer=remove_between_space(answer)
if answer.lower().strip() == "skin":
    print("correct")
    correctAnswerCount += 1
else:
    print("wrong")

answer = input("Question: Which country is famous for the Taj Mahal? - ")
answer=remove_between_space(answer)
if answer.lower().strip() == "india":
    print("correct")
    correctAnswerCount += 1
else:
    print("wrong")

print("The number of correct Answers is - ", str(correctAnswerCount))
wrongAnswer = totalQuestion - correctAnswerCount
print("Your Obtain Marks Is - ", str(correctAnswerCount * 2 - wrongAnswer * 0.25))
print("your obtain marks in percentage is", str((correctAnswerCount / totalQuestion) * 100) + "%")
