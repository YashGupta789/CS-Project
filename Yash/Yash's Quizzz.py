#Welcome Code
print("Welcome to my Yash's quizz Game!")

playing = input("Do you want to play?(y/n): ")

if playing.lower() == "n":
    print("Your Wish")
    quit()

if playing.lower() == "y":
    score = 0
else:
    quit()

print("Let's Start :)")
score = 0
question = 0 

answer = input("Question 1: Series of well defined Steps to Solve A Problem - ")
if answer.lower() == "algorithm":
    print('Correct!!')
    score += 5
    question += 1 
else:
    print("Incorrect!!!")

answer = input("Question 2: Property that defines a class that inherits all the methods and properties from another class - ")
if answer.lower() == "inheritance":
    print('Correct!!')
    score += 5
    question += 1
else:
    print("Incorrect!!!")

answer = input("Question 3: What is the built-in module used for working with mathematical functions in Python? - ")
if answer.lower() == "math":
    print('Correct!!')
    score += 5
    question += 1 
else:
    print("Incorrect!!!")


answer = input("Question 4: What is the built-in data type in Python that holds key-value pairs? - ")
if answer.lower() == "dictionary":
    print('Correct!!')
    score += 5
    question += 1 
else:
    print("Incorrect!!!")


answer = input("Question 5: What error will come if we forget to write parenthesis or colon - ")
if answer.lower() == "syntax error":
    print('Correct!!')
    score += 5
    question += 1 
else:
    print("Incorrect!!!")

displayscore = str(score)
print("             Your Score: "+displayscore)

if score == 25:
    print("             !!Hurrey!! You got all 5 questions correct!!")
else:
    print("             You got " + str(question) + " questions correct!")

print("             You got " + str((question / 5) * 100) + "%")
