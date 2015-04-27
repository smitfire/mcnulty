import csv
import sys

our_file = sys.argv[1]
longest_word = ''
def longest_word (fname):
    with open(fname) as f:
        content = f.readlines()
    longest_list = content[0].split(' ')
    longest = len(sorted(longest_list, key=len)[-1])
    # print longest
    for l in longest_list:
        if len(l) == longest:
            return l


print longest_word(our_file)