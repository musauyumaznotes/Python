class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.answer = answer
        self.choices = choices
    def checkAnswer(self,answer):
        return self.answer==answer


# print(q1.checkAnswer("Python"))
# print(q2.checkAnswer("C#"))
import random
class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
    def getQuestion(self):
        return self.questions[self.questionIndex]
    def display(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex + 1} : {question.text}")

        for q in question.choices:
            print("-"+q),

        answer = input("Cevap : ")
        print(question.checkAnswer(answer))
    def guess(self,answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score +=1
        self.questionIndex +=1

        self.displayQuestion()

q1 = Question("En iyi programlama dili hangisidir?",["C#","Python","JavaScript","Java"],"Python")
q2 = Question("En popüler programlama dili hangisidir?",["C#","Python","JavaScript","Java"],"Python")
q3 = Question("En çok kazandıran programlama dili hangisidir?",["C#","Python","JavaScript","Java"],"Python")
questions = [q1,q2,q3]

quiz = Quiz(questions)
# question = quiz.getQuestion()
# print(question.text)