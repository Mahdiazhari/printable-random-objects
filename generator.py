import random
import string
import os


class Generator:
    """This class generates four types of printable random objects and stores them in a single file."""
    
    @staticmethod
    def generate_alphanumerics():
        """This function generates a random alphanumeric which contains a random number of spaces before and after it (not exceeding 10 spaces).
        Assumptions: - There can be 0 spaces
                     - There can be 20 spaces maximum in both before and after the string"""
        spaces_before = random.randint(0, 10)
        spaces_after = random.randint(0,10)
        core_length = random.randint(2,20)
        core_string = ''.join(random.choices(string.ascii_letters +
                             string.digits, k = core_length))
        final_string = ' '*spaces_before + core_string + ' '*spaces_after
        return final_string
    
    @staticmethod
    def generate_alphabetic():
        "This function generates a random alphabetic string."
        core_length = random.randint(1,30)
        core_string = ''.join(random.choices(string.ascii_letters, k=core_length))
        return core_string
    
    @staticmethod
    def generate_integer():
        """This function generates a random integer."""
        core_int = random.randint(0, 1000000000000)
        return str(core_int)
    
    @staticmethod    
    def generate_real():
        """This function generates a random real number."""
        random_float = random.uniform(1, 100000)
        return str(random_float)
    
    @staticmethod 
    def generate_file(filename, target_size):
        """This function generates a printable random object with a given filename and expected size (in Megabytes)."""
        open(filename, "w+") # create file
        file_stat = os.stat(filename)
        filesize = file_stat.st_size
        print('Initial file size: ', filesize)
        with open(filename, 'a') as file:
            print('Writing output to file ' + filename)
            max_size =  target_size * 1000000
            while filesize < max_size:
                functions = [Generator.generate_alphabetic, Generator.generate_alphanumerics, Generator.generate_real, Generator.generate_integer]
                random_data = random.choice(functions)()
                file.write(random_data + ', ')
                filesize += len(random_data) + 2
            print('Generated ' + filename + ' of size ' + str(filesize/1000000) +'MB')
            file.close()
    