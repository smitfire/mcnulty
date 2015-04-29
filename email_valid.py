#  we need @ char
#  we need no spaces
#  we need text before and after @

import re 

def email_valid(the_string):
  the_string = the_string.strip()
  if "@" in the_string:
    first_s = the_string.split("@")[0]
    second_s = the_string.split("@")[1]
    if "." in second_s and " " not in the_string and len(first_s)>0 and len(second_s) > 1 and "@" not in first_s:
      third_s = second_s.split('.')[-1]
      if len(third_s) > 1:
        return True
  else:
    return False



def email_valid2(the_string):
  if not re.match(r"/\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]{2,})\Z/i", the_string):
    return False
  else:
    return True

m="nick.smit@gmail.com"

m1="foo@bar.com"
m2="this is not an email id"
m3="admin#codeeval.me"
m4="good123@bad.com"

print email_valid2(m1)
print email_valid2(m1)
print email_valid2(m2)
print email_valid2(m3)
print email_valid2(m4)