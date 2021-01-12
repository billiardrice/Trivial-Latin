# Import Libs
from random import *
import csv
from tkinter import *


# Declare Variables
vocabDerivQuestions = []
vocabDerivQCount = 0
nounQuestions = []
nounQCount = 0
verbQuestions = []
verbQCount = 0
cultureQuestions = []
cultureQCount = 0
historyQuestions = []
historyQCount = 0
adjAdvPrepClauseQuestions = []
adjAPCQCount = 0
constructionQuestions = []
constructionQCount = 0

vocabDerivAnswers = []
nounAnswers = []
verbAnswers = []
cultureAnswers = []
historyAnswers = []
adjAdvPrepClauseAnswers = []
constructionAnswers = []

# Random question number picker
def randomQuestion(totalLength):
    return randint(0, totalLength - 1)

# Reding file
def readFile():

    global vocabDerivQuestions
    global vocabDerivQCount
    global nounQuestions
    global nounQCount
    global verbQuestions
    global verbQCount
    global cultureQuestions
    global cultureQCount
    global historyQuestions
    global historyQCount
    global adjAdvPrepClauseQuestions
    global adjAPCQCount
    global constructionQuestions
    global constructionQCount

    global vocabDerivAnswers
    global nounAnswers
    global verbAnswers
    global cultureAnswers
    global historyAnswers
    global adjAdvPrepClauseAnswers
    global constructionAnswers

    count = 0

    vocabDerivQuestions.clear()
    nounQuestions.clear()                
    verbQuestions.clear()
    cultureQuestions.clear()
    historyQuestions.clear()
    adjAdvPrepClauseQuestions.clear()
    constructionQuestions.clear()

    vocabDerivAnswers.clear()
    nounAnswers.clear()
    verbAnswers.clear()
    cultureAnswers.clear()
    historyAnswers.clear()
    adjAdvPrepClauseAnswers.clear()
    constructionAnswers.clear()

    vocabDerivQCount = 0
    nounQCount = 0
    verbQCount = 0
    cultureQCount = 0
    historyQCount = 0
    adjAPCQCount = 0
    constructionQCOunt = 0

    with open('questions.csv','r',encoding='utf-8') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            if count > 0:
                vocabDerivQuestions.append(row[0])
                nounQuestions.append(row[2])                
                verbQuestions.append(row[4])
                cultureQuestions.append(row[6])
                historyQuestions.append(row[8])
                adjAdvPrepClauseQuestions.append(row[10])
                constructionQuestions.append(row[12])

                vocabDerivAnswers.append(row[1])
                nounAnswers.append(row[3])
                verbAnswers.append(row[5])
                cultureAnswers.append(row[7])
                historyAnswers.append(row[9])
                adjAdvPrepClauseAnswers.append(row[11])
                constructionAnswers.append(row[13])

                if row[0] != '':
                    vocabDerivQCount += 1
                if row[2] != '':
                    nounQCount += 1
                if row[4] != '':
                    verbQCount += 1
                if row[6] != '':
                    cultureQCount += 1
                if row[8] != '':
                    historyQCount += 1
                if row[10] != '':
                    adjAPCQCount += 1
                if row[12] != '':
                    constructionQCOunt += 1

            count += 1      

def randVocabQuestion():

    global vocabDerivQCount

    z = randomQuestion(vocabDerivQCount)

    x.set(vocabDerivQuestions[z])
    textQuestion.config(bg="cyan", fg="black")
    y.set(vocabDerivAnswers[z])
    textAnswer.config(bg="cyan", fg="black")

    vocabDerivQuestions.append(vocabDerivQuestions[z])
    del vocabDerivQuestions[z]
    vocabDerivAnswers.append(vocabDerivAnswers[z])
    del vocabDerivAnswers[z]
    vocabDerivQCount -= 1

    if vocabDerivQCount == 0:
        readFile()

def randNounQuestion():

    global nounQCount

    z = randomQuestion(nounQCount)

    x.set(nounQuestions[z])
    textQuestion.config(bg="green", fg="black")
    y.set(nounAnswers[z])
    textAnswer.config(bg="green", fg="black")

    nounQuestions.append(nounQuestions[z])
    del nounQuestions[z]
    nounAnswers.append(nounAnswers[z])
    del nounAnswers[z]
    nounQCount -= 1

    if nounQCount == 0:
        readFile()

def randVerbQuestion():

    global verbQCount

    z = randomQuestion(verbQCount)

    x.set(verbQuestions[z])
    textQuestion.config(bg="yellow", fg="black")
    y.set(verbAnswers[z])
    textAnswer.config(bg="yellow", fg="black")
    
    verbQuestions.append(verbQuestions[z])
    del verbQuestions[z]
    verbAnswers.append(verbAnswers[z])
    del verbAnswers[z]
    verbQCount -= 1

    if verbQCount == 0:
        readFile()

def randCultureQuestion():

    global cultureQCount

    z = randomQuestion(cultureQCount)

    x.set(cultureQuestions[z])
    textQuestion.config(bg="red", fg="black")
    y.set(cultureAnswers[z])
    textAnswer.config(bg="red", fg="black")

    cultureQuestions.append(cultureQuestions[z])
    del cultureQuestions[z]
    cultureAnswers.append(cultureAnswers[z])
    del cultureAnswers[z]
    cultureQCount -= 1

    if cultureQCount == 0:
        readFile()

def randHistoryQuestion():

    global historyQCount

    z = randomQuestion(historyQCount)

    x.set(historyQuestions[z])
    textQuestion.config(bg="black", fg="white")
    y.set(historyAnswers[z])
    textAnswer.config(bg="black", fg="white")

    historyQuestions.append(historyQuestions[z])
    del historyQuestions[z]
    historyAnswers.append(historyAnswers[z])
    del historyAnswers[z]
    historyQCount -= 1

    if historyQCount == 0:
        readFile()

def randAdjAPCQCQuestion():

    global adjAPCQCount

    z = randomQuestion(adjAPCQCount)

    x.set(adjAdvPrepClauseQuestions[z])
    textQuestion.config(bg="orange", fg="black")
    y.set(adjAdvPrepClauseAnswers[z])
    textAnswer.config(bg="orange", fg="black")

    adjAdvPrepClauseQuestions.append(adjAdvPrepClauseQuestions[z])
    del adjAdvPrepClauseQuestions[z]
    adjAdvPrepClauseAnswers.append(adjAdvPrepClauseAnswers[z])
    del adjAdvPrepClauseAnswers[z]
    adjAPCQCount -= 1

    if adjAPCQCount == 0:
        readFile()
    
def randConstructionQuestion():

    global constructionQCount

    z = randomQuestion(constructionQCount)

    x.set(constructionQuestions[z])
    textQuestion.config(bg="white", fg="black")
    y.set(constructionAnswers[z])
    textAnswer.config(bg="white", fg="black")

    constructionQuestions.append(constructionQuestions[z])
    del constructionQuestions[z]
    constructionAnswers.append(constructionAnswers[z])
    del constructionAnswers[z]
    constructionQCount -= 1

    if constructionQCount == 0:
        readFile()

def randDieRoll():

    numbers = ["1","2","3","4","5","6"]

    roll.set(numbers[randomQuestion(6)])

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master


# initialize tkinter
root = Tk()
app = Window(root)
root.minsize(width=610, height=240)
root.resizable(False, False)

x = StringVar()
y = StringVar()
roll = StringVar()

# set window title
root.wm_title("Trivial Latin")

readFile()

print(verbQuestions[5])
print(verbAnswers[5])
print(verbQCount)

# creating objects
questionInfo = Message(root, text="Question:", width=500)
textQuestion = Message(root, textvariable = x, width=500)
answerInfo = Message(root, text="Answer:", width=500)
textAnswer = Message(root, textvariable = y, width=500)

vocab = Button(root, text="Vocab", command=lambda:randVocabQuestion(), width=10)
noun = Button(root, text="Noun", command=lambda:randNounQuestion(), width=10)
verb = Button(root, text="Verb", command=lambda:randVerbQuestion(), width=10)
culture = Button(root, text="Culture", command=lambda:randCultureQuestion(), width=10)
history = Button(root, text="History", command=lambda:randHistoryQuestion(), width=10)
adjAPC = Button(root, text="Adjective", command=lambda:randAdjAPCQCQuestion(), width=10)
construction = Button(root, text="Construction", command=lambda:randConstructionQuestion(), width=10)

# packing objects

vocab.pack()
vocab.place(bordermode=OUTSIDE, y=5)
noun.pack()
noun.place(bordermode=OUTSIDE, y=35)
verb.pack()
verb.place(bordermode=OUTSIDE, y=65)
culture.pack()
culture.place(bordermode=OUTSIDE, y=95)
history.pack()
history.place(bordermode=OUTSIDE, y=125)
adjAPC.pack()
adjAPC.place(bordermode=OUTSIDE, y=155)
construction.pack()
construction.place(bordermode=OUTSIDE, y=185)

questionInfo.pack()
questionInfo.place(bordermode=OUTSIDE, x=95)
textQuestion.pack()
textQuestion.place(bordermode=OUTSIDE, x=100, y=25)

answerInfo.pack()
answerInfo.place(bordermode=OUTSIDE, x=95, y=120)
textAnswer.pack()
textAnswer.place(bordermode=OUTSIDE, x=100, y=145)

dieResult = Message(root, textvariable = roll, width=500)

dice = Button(root, text="Roll A Die", command=lambda:randDieRoll(), width=10)
dice.pack()
dice.place(bordermode=OUTSIDE, y=215)

dieResult.pack()
dieResult.place(bordermode=OUTSIDE, x=105, y=210)

root.mainloop()