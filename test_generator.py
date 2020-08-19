from unittest import TestCase
from generator import Generator

class GeneratorTest(TestCase):
    """Unit testing class for the Generator class. This tests whether the generated alphanumeric, alphabetical, real number or integer follows the specified format."""
    
    generator = Generator()
    
    @staticmethod
    def isAlphaNumeric(input_string):
        spaces_flag = False
        if input_string.count(' ') <= 20:
            spaces_flag = True
        return input_string.strip().isalnum() and spaces_flag
    
    @staticmethod
    def isAlphabet(input_string):
        return input_string.strip().isalpha()
    @staticmethod
    def isReal(input_string):
        if "." not in input_string.strip():
            return False
        else:
            return True
    @staticmethod
    def isInteger(input_string):
        try: 
            int(input_string)
            return True
        except ValueError:
            return False
    
    
    def test_generate_alphanumeric(self):
        self.assertTrue(self.isAlphaNumeric(self.generator.generate_alphanumerics()))
        
    def test_generate_alphabets(self):
        self.assertTrue(self.isAlphabet(self.generator.generate_alphabetic()))

    def test_generate_integer(self):
        self.assertTrue(self.isInteger(self.generator.generate_integer()))
        
    def test_generate_real(self):
        self.assertTrue(self.isReal(self.generator.generate_real()))
        
    if __name__ == '__main__':
        # begin the unittest.main()
        unittest.main()