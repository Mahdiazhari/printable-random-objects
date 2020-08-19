from generator import Generator #import the Generator class made before this
import pandas as pd
import sys
import os

"""
To run this file, put in the two required parameters [filename] and [target file size] as the 1st and 2nd argument. 
"""

generator = Generator()
filename = sys.argv[1] + '.txt'
target_size = float(sys.argv[2])
generator.generate_file(filename, target_size)

def checkElement(string):
    """This function checks whether a string is an Integer, an Alphabetical String, an Alphanumerical String, or a Real Numbner."""
    def isAlphaNumeric(input_string):
        spaces_flag = False
        if input_string.count(' ') <= 20:
            spaces_flag = True
        return input_string.strip().isalnum() and spaces_flag
    
    def isAlphabet(input_string):
        return input_string.strip().isalpha()

    def isReal(input_string):
        if "." not in input_string.strip():
            return False
        else:
            return True

    def isInteger(input_string):
        try: 
            int(input_string.strip())
            return True
        except ValueError:
            return False

    if isInteger(string):
        print(string + ' - ' + 'integer')
    elif isAlphabet(string):
        print(string + ' - ' + 'alphabetical strings')
    elif isAlphaNumeric(string):
        print(string + ' - ' + 'alphanumeric')
    elif isReal(string):
        print(string + ' - ' + 'real numbers')
        
df = pd.read_csv(sys.argv[1]+ '.txt', header=None, dtype=str)
filesize = os.stat(filename).st_size

df.applymap(checkElement)

print('Generated ' + filename + ' of size ' + str(filesize/1000000) +'MB')