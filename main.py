from utils.ocr import ocr_write, pr 
from utils.constants import DELIMITER
# replace_combination(['Question', 'Previous', 'Next', 'Index', 'Question', 'Question'])
# ocr_write()



TEXT = ['QUESTION 4 of 50', 'If you cannot steer straight because the road surface is not even, you', 'should', 'Question', 'Previous', 'Next', 'Index', 'Question', 'Question', 'Loosen your grip on the steering wheel.', 'Increase speed', 'Correct', 'Rduce speed.', 'answer']
HEADER = 'QUESTION 4 of 50'



def match_header(text):
    import re
    from utils import constants
    if re.search(constants.HEADER_REGEX, text):
        return True
def get_header_position(arr):
    for pos, value in enumerate(arr):
        if match_header(value):
            return [pos]



def get_button_position(arr):
    button_arr = ['Question', 'Previous', 'Next', 'Index', 'Question', 'Question']
    for pos, value in enumerate(arr):
        if pos + 6 < len(arr) + 1:
            if arr[pos:pos+6] == button_arr:
                start, end = pos , pos+6
                return [i for i in range(pos, pos + 6)]


def get_answer_filler_position(arr):
    for pos, value in enumerate(arr):
        if arr[pos] in ['Correct','Wrong'] and arr[pos + 2] == 'answer':
            return [pos, pos + 2]



def get_question_position(arr, header_arr, button_arr):
    pos = 0
    result = []
    while pos < len(arr):
        if pos in header_arr:
            pos += 1
            continue
        if pos in button_arr:
            break
        result.append(pos)
        pos += 1
    return result


def get_option_position(arr, button_arr, get_answer_filler_position):
    pos = button_arr[-1] + 1
    result = []
    while pos < len(arr):
        if pos in get_answer_filler_position:
            pos += 1
            continue
        result.append(pos)
        pos += 1
    return result


def clean_question_text(text, arr):
    question_text = ''
    for question in arr:
        s = text[question]
        question_text += ' ' + s
    question_text += ':'
    question_text = question_text.strip()
    return question_text

def clean_option_text(text, arr):
    options_text = ''
    for option in arr:
        s = text[option]
        option1 = s+'.' if s[-1] != '.' else s
        options_text += option1 + DELIMITER
    return options_text
        

def combine(text):
    header_arr = get_header_position(text)
    button_arr = get_button_position(text)

    question_arr = get_question_position(text, header_arr, button_arr)
    answer_filler_arr = get_answer_filler_position(text)
    options_arr = get_option_position(text, button_arr, answer_filler_arr)

    question_text = clean_question_text(text, question_arr)
    options_text = clean_option_text(text, options_arr)

    return question_text, options_text
    


print(combine(TEXT))