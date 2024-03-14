questions=("How many elements in the periodic table?:",
           "which animal lays the largest eggs?:",
           "How many planets are in solar system?:",
           "How many bones are their in human body",
           "which planet in the solar system is the largest?:")

options=(("A.116","B.117","C.118","D.119"),
         ("A.Whale","B.Elephant,","C.Fish","D.Ostrich"),
         ("A.6","B.7,","C.8","D.9"),
         ("A.202","B.204,","C.206","D.208"),
         ("A.Venus","B.Earth,","C.Mars","D.Jupiter"))
answer=("C","D","C","C","D")
guesses=[]
score=0
question_num=0

for question in questions:
    print("-----------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("Enter(A,B,C,D):").upper()
    guesses.append(guess)
    if guess==answer[question_num]:
        score+=1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answer[question_num]} is the correct answer")
    question_num+=1

print("---------------")
print("     RESULTS   ")
print("----------------")    

print("answers:",end="")
for answer in answer:
    print(answer,end=" ")
print()
print("guesses:",end="")
for guess in guesses:
    print(guess,end=" ")
print()
score=int(score/len(questions)*100)
print(f"your score is:{score}%")
