Project Overview:
	The big project I proposed was something that would calculate the user's carbon footprint and then compare
that footprint to the footprint created by major industries. While the initial intention was to create
as accurate of a carbon footprint as possible, it quickly became clear that unless the user wanted to spend
twenty minutes answering multiple choice questions, it would have to be scaled down dramatically. The questions
were sampled from teachengineering.org because they struck a balance between simplicity and complexity.The completed
project still fulfills the goals from the big project proposal, but at a much smaller scale. 

Project Narrative:
	 The process of creating the project was actually relatively smooth. My idea to use a class to format all
of the questions from the carbon footprint worksheet that I sampled online went very smoothly, and before milestone
1 I had a functioning carbon footprint calculator that used a class and function to generate questions and store the
values from the answers. The first python project milestone had been met if not exceeded, with the class functioning.
There were still some kinks to work out though and some inefficiencies to chew through, this became the major challenge
in the second milestone. The code was going into action, calculating and outputting the user's carbon footprint exactly 
how I wanted it to. However, the lack of any resiliency created major issues for the user, who would have to start over 
if there were any errors on their end. Implementing this reliency is what proved to be the biggest challenge. While the
code I had written was efficient, it was spaghetti. Changing one part of it seemed to consistently break the entire 
project every single time. Thankfully, concepts from the lectures, specifically when, if and range were the 
solution to the problem. If there were anything I would do differently, it would be to have resiliency in mind as
I was writing the code rather than having to implement it after the fact. 

Corrections:
	The main concern in milestone 1 was the resiliency. This issue was eventually solved, but it took until after
milestone 2 for all of the bugs to be worked out completely. After Milestone 2 is where most of my changes were. One of
the issues was an "out of range" error that would occur if the user inputted an answer that was 2 or more outside of
the answer numbers. This problem was thankfully completely solved in line 22 just by changing 
if int(useranswer) in range(1, len(self.answer)):
  to          
if int(useranswer) in range(1, len(self.answer) + 1):
now if the user's answer is ANYTHING other higher or lower than what it is supposed to be the program will re-ask the question.
The secnd major criticism was a lack of emphasis on the the corporate part of the carbon footprint. To add to the impact of this part
I decided to import turtle to create a rough visualization of a user's carbon output. Every time the arrow rounds a corner it represents
their entire life's worth of carbon emissions and only one second of emissions from the global energy sector. This really 
adds to the impact of the project. With all known bugs solved and a more unique spin put on the final part of the project, I really do
feel that it is complete. It was a lot of fun to work on and I feel that I have a good basic understanding of Python now. 