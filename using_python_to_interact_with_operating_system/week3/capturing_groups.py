# Return format
# Returning first and last name
import re
# firstName = input("Enter your first name: ")
# lastName = input("Enter your last name: ")
# name = firstName + lastName
def fullName(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    print("The text under search is: "+ str(result.groups()))
    # print(result[0]) -- prints the whole text
    # print(result[1]) -- prints the first word
    if result is None:
        return name
    return "I have nicknamed you: {} {}".format(result[2], result[1])
print(fullName("Gitonga, Denzel"))
