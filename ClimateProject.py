#Cameron Simms
#Started Working on This 10/21/21
#This will output the user's carbon footprint. The majority of it is something they cannot affect themeselves and it static
#This static value of 13000 will be the focus, and the rest of the project will demonstrate how insignificant their personal output is
Footprint = 0
#A loop that asks the user a series of questions to calculate carbon footprint
class ClimateQuery:
    def __init__(self, question, answer, carbonvalue):
        self.question = question
        self.answer = answer
        self.carbonvalue = carbonvalue
    def mquery(self):
            print("I'm at the beginning of mquery")
            global Footprint
            loopnum = 0
            useranswer = 0
            mchoice = range(1, len(self.answer))
            print('Do you ' + self.question)
            for item in self.answer:
                print(str(mchoice[loopnum]) + ': ' + self.answer[loopnum])
                loopnum = loopnum + 1
#This while loop adds resiliency so the code does not instantly break if the user messes up
            useranswer = input("Choose The Number That Applies to You: ")
            print("After user answer.")
            if useranswer in range(1, len(self.carbonvalue)):
                Footprint += self.carbonvalue[useranswer - 1]
            else:
                print("Sorry, that answer does not work, try again")
                self.mquery()

            print(' ')
            pass

# qtemplate: q = ClimateQuery('', [''], []) THe template for all the questions
q_1 = ClimateQuery('commute by', ['walking', 'biking', 'driving', 'public transit', 'carpooling'], [0, 0, 1115, 131, 459])
q_2 = ClimateQuery('eat mostly', ['fast food', 'home cooked meals'], [4818, 629])
q_3 = ClimateQuery('eat mostly', ['vegetables/fruit', 'meat', 'breads'], [153, 644, 364])
q_4 = ClimateQuery('turn off the lights when you leave a room?', ['yes', 'no'], [133, 268])
q_5 = ClimateQuery('unplug appliances and chargers when they are not in use?', ['yes', 'no'], [9, 18])
q_6 = ClimateQuery('dry clothes by', ['hanging to dry', 'a dryer', 'both'], [0, 750, 375])
q_7 = ClimateQuery('turn off the water when brushing your teeth?', ['yes', 'no'], [34, 274])
q_8 = ClimateQuery('turn off the tv while watching it?', ['yes', 'no'], [47, 140])
q_9 = ClimateQuery('turn off computers while not in use?', ['yes', 'no'], [29, 90])
q_10 = ClimateQuery('you recycle to the best of your ability?', ['yes', 'no'], [-150, 20])
qList = [q_1, q_2, q_3, q_4, q_5, q_6, q_7, q_8, q_9, q_10]
loop = 0
for element in qList:
    qList[loop].mquery()
    loop = loop + 1
print('Your Carbon Footprint is ' + str(Footprint + 22000) + ' pounds of CO2 a year')
