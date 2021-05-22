import regex as re
import os

# set path to files to unzipped articles folder
path_to_files = r'#YOUR PATH#'  # e.g. r'C:\Users\Doron[...]\data\articles'

# create regex that separates full document incl. all information
doc_re = re.compile(r'YOUR REGEX HERE', re.DOTALL)

# create regex for each sub-information
"""
YOUR REGEXES HERE
"""

# iterate through folder
for fname in os.listdir(path_to_files):

    # print file name for debugging
    print(fname)

    # open set of articles of company file
    docs = open(os.path.join(path_to_files, fname)).read()

    # if you get a UnicodeDecodeError here - that's life, deal with it :)
    # https://www.youtube.com/watch?v=HluANRwPyNo&ab_channel=Jombo

    """
    YOUR CODE HERE
    """
