#Cameron Simms
#Started Working on This 10/21/21
#This will output the user's carbon footprint. The majority of it is something they cannot affect themeselves and it static
#This static value of 13000 will be the focus, and the rest of the project will demonstrate how insignificant their personal output is
Footprint = 0
import time
import turtle
#A loop that asks the user a series of questions to calculate carbon footprint
class ClimateQuery:
    def __init__(self, question, answer, carbonvalue):
        self.question = question
        self.answer = answer
        self.carbonvalue = carbonvalue
        #mquery generates a question based off the objects in ClimateQUery
    def mquery(self):
            global Footprint
            loopnum = 0
            #mchoice is what the user sees
            mchoice = ['1', '2', '3', '4', '5']
            print('Do you ' + self.question)
        #prints 1. , 2. 3. 4. 5. so the user knows which answer cooresponds to which number.
            for item in self.answer:
                print(mchoice[0 + loopnum] + ': ' + self.answer[0 + loopnum])
                loopnum = loopnum + 1
            useranswer = input("Choose The Number That Applies to You: ")
            if int(useranswer) in range(1, len(self.answer) + 1):
                pass
            else:
                print('Not a Valid Answer, try again')
                self.mquery()
            Footprint += self.carbonvalue[int(useranswer) - 1]
            print(' ')
            pass
# qtemplate: q = ClimateQuery('', [''], []) THe template for all the questions
#first object is the question, second is the answer, and third is the carbon value that cooresponds to the answer
q_1 = ClimateQuery('commute by', ['walking', 'biking', 'driving', 'public transit', 'carpooling'], [0, 0, 1115, 131, 459])
q_2 = ClimateQuery('eat mostly', ['fast food', 'home cooked meals'], [4818, 629])
q_3 = ClimateQuery('eat mostly', ['vegetables/fruit', 'meat', 'breads'], [153, 644, 364])
q_4 = ClimateQuery('turn off the lights when you leave a room?', ['yes', 'no'], [133, 268])
q_5 = ClimateQuery('unplug appliances and chargers when they are not in use?', ['yes', 'no'], [9, 18])
q_6 = ClimateQuery('dry clothes by', ['hanging to dry', 'a dryer', 'both'], [0, 750, 375])
q_7 = ClimateQuery('turn off the water when brushing your teeth?', ['yes', 'no'], [34, 274])
q_8 = ClimateQuery('turn off the tv while not watching it?', ['yes', 'no'], [47, 140])
q_9 = ClimateQuery('turn off computers while not in use?', ['yes', 'no'], [29, 90])
q_10 = ClimateQuery('you recycle to the best of your ability?', ['yes', 'no'], [-150, 20])
#used for a loop and to dtermine which ClimateQUery to call
qList = [q_1, q_2, q_3, q_4, q_5, q_6, q_7, q_8, q_9, q_10]
loop = 0
for element in qList:
    qList[loop].mquery()
    loop = loop + 1
    #Just talks to the user about the insignificance of their personal carbon footprint
print('Your Carbon Footprint is ' + str(Footprint + 22000) + ' pounds of CO2 a year')
time.sleep(3)
print('This is a rough estimate of your carbon footprint')
time.sleep(4)
print('But how much of your carbon footprint can you control?')
time.sleep(5)
print('of the ' + str(Footprint + 22000) + ' pounds of CO2 you generated')
time.sleep(4)
print('You can only control rougly ' + str(Footprint) + ' pounds of it')
time.sleep(6)
print('A New Window Will open showing an arrow moving around a square')
time.sleep(3)
print('Every time this arrow rounds a corner, it represents all the emissions you will ever output in your life')
time.sleep(2)
print('The global energy sector outputs the same amount of emissions that you output in your life time')
print('in the same amount of time it takes from the arrow to move from one side of the square to another')
time.sleep(1)
print('new window opening')
time.sleep(3)
#Visualiation showing the user's carbon output. Every time the arrow hits a corner it represents their entire lifetime of carbon output
#And the same amount of carbon output in the same time it takes the arrow to reach one side of the square to another
t = turtle.Turtle()
while (loop < 999):
    t.fillcolor('blue')
    t.begin_fill()
    for i in range(4):
        t.forward(150)
        t.right(90)
t.end_fill()
