#import random for randomizing questions later
import random

#load the file from the quiz creator
filename = gathered_quiz_data.txt

with open(filename, 'r') as file:
    content = file.read()

#split the questions into blocks
question_blocks = content.strip().split('-' * 40)

#Extract the questions, options, and answers
#randomize the questions
#display and prompt users to answer
#check answer