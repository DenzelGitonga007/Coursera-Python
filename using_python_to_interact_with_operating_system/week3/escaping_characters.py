# Matching special characters using the escape backslash
import re
def check_character_groups(text):
  result = re.search(r"[\w*][\s*]", text) # \w matches all the alphanumeric texts, \s matches all the whitespaces
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False