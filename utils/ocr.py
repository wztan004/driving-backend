def ocr_write():
    import easyocr
    from utils import constants

    reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
    result = reader.readtext('s2.jpg')
    f = open("demofile3.txt", "a")
    exclude_text = []
    include_text = []
    all_text = []
    for box, text, level in result:
        # if text in constants.SKIP_WORDS:
        #     continue
        # if text_to_replace:
        #     text1 = replace_header(text)
        #     text2 = replace_filler(text1)

        all_text.append(text)
        # if search_text(constants.HEADER_REGEX, text):
        #     exclude_text.append(text)
        # else:
        #     include_text.append(text)

    print(all_text)
        
    # f.write(''.join(arr))

    # f.close()

def search_text(expr, text):
    import re
    from utils import constants
    return re.search(expr, text)

def replace_header(txt):
    import re
    from utils import constants
    return re.sub(constants.HEADER_REGEX, "", txt)

def replace_filler(txt):
    import re
    from utils import constants
    return re.sub(constants.FILLER_REGEX, "", txt)




def pr():
    arr = [['QUESTION 4 of 50', 'If you cannot steer straight because the road surface is not even, you', 'should'], ['Loosen your grip on the steering wheel.', 'Increase speed', 'Correct', 'Rduce speed.', 'answer']]
    from utils import constants
    new_arr = []
    for a in arr:
        new_arr_e = []
        for v in a:
            if not search_text(constants.HEADER_REGEX, v):
                new_arr_e.append(v)
        new_arr.append(new_arr_e)

    print(new_arr)
    return new_arr


def get_button_position(arr):
    button_arr = ['Question', 'Previous', 'Next', 'Index', 'Question', 'Question']
    for pos, value in enumerate(arr):
        if pos + 6 < len(arr) + 1:
            if arr[pos:pos+6] == button_arr:
                start, end = pos , pos+6
                return [i for i in range(pos, pos + 6)]