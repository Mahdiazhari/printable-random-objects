# Printable Random Objects

This Python Application creates printable random objects of four categories, writes them into a txt file and then parses/categorizes them.
There are two main python scripts: generator.py and main.py. generator.py contains the Generator class.
The Generator class will generate 4 kinds of alphanumeric strings:

1. Alphabets
2. Alphanumerics
3. Integers
4. Real Numbers

These strings will be appended to a file called test.txt. It is possible to set the size of the txt file depending on our requirements. Just put in the target filesize in the target_size parameter (set the size in Megabytes) of the generate_file method.
The Generator also comes with a unittest which we can use with the command "python -m unittest".

The main driver for the whole package of applications is available in main.py.
