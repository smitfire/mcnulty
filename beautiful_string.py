# Each letter has value between 1 and 26
# abbccc =  152
# Beauty of string is sum of letters in it

# a = 24, b = 25, c =  26

import string
import re
import operator

def string_beauty(s):
  my_dict={}
  vals_list = list(xrange(1,28))
  my_list = list(remove_noise_chars(s))
  for s in my_list:
    if s in my_dict:
      my_dict[s]+=1
    else:
      my_dict[s]=1
  sort_me = sorted(my_dict.items(), key=operator.itemgetter(1))
  num_vals = 26 - len(sort_me)
  new_vals_list = vals_list[num_vals:-1]
  thing_list = zip(sort_me, new_vals_list)
  total = 0
  for index, letter_group in enumerate(sort_me):
    total += letter_group[1]*new_vals_list[index]
  return total

def remove_noise_chars(s):
  exclude = set(string.punctuation)
  return ''.join(ch for ch in s if ch not in exclude).replace(' ', '').lower()


s1 = "Good luck in the Facebook Hacker Cup this year!"


print string_beauty(s1)