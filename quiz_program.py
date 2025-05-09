#import random for randomizing questions later
import random

#load the file from the quiz creator
filename = "gathered_quiz_data.txt" 

def get_quiz_data(filename):
    with open(filename, 'r') as file:
        content = file.read()

#split the questions into blocks
    question_blocks = content.strip().split('-' * 40)

#Extract the questions, options, and answers
    questions = []

    for block in question_blocks:
        lines = block.strip().split('\n')
        if not lines or 'Question:' not in lines [0]:
            continue

        question_dictionary = {'question': '', 'options': {}, 'answer': ''}
        for line in lines:
            if line.startswith('Question:'):
                question_dictionary['question'] = line[len('Question:'):].strip()
            elif line.startswith("A)"):
                question_dictionary['options']['A'] = line[3:].strip()
            elif line.startswith("B)"):
                question_dictionary['options']['B'] = line[3:].strip()
            elif line.startswith("C)"):
                question_dictionary['options']['C'] = line[3:].strip()
            elif line.startswith("D)"):
                question_dictionary['options']['D'] = line[3:].strip()
            elif line.startswith("Correct Answer:"):
                parts = line[len("Correct Answer:"):].strip().split(':', 1)
                if len(parts) == 2:
                    question_dictionary['answer'] = parts[0].strip()

        if question_dictionary['question'] and question_dictionary['options'] and question_dictionary['answer']:
            questions.append(question_dictionary)

    return questions

#display and prompt users to answer
def start_quiz(questions):
    if not questions:
        print('No Questions')
        return
    
    question = random.choice(questions)
    
    print('\n' + question['question'])
    for key in ['A', 'B', 'C', 'D']:
        print(f"{key}) {question['options'].get(key, '')}")
    
    input_answer = input('Enter answer (A/B/C/D): ').strip.().upper()
    
#check answer