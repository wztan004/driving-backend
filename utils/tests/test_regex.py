import unittest
from utils.ocr import get_button_position
TEXT = ['QUESTION 4 of 50', 'If you cannot steer straight because the road surface is not even, you', 'should', 'Question', 'Previous', 'Next', 'Index', 'Question', 'Question', 'Loosen your grip on the steering wheel.', 'Increase speed', 'Correct', 'Rduce speed.', 'answer']
TEXT2 = ['Question', 'Previous', 'Next', 'Index', 'Question', 'Question']

class TestRegex(unittest.TestCase):
    def test_button_position(self):
        self.assertEqual(get_button_position(TEXT), [3,4,5,6,7,8])
        self.assertEqual(get_button_position(TEXT2), [0,1,2,3,4,5])



# if __name__ == '__main__':
#     unittest.main()