# Searching for special characters
import re
print(re.search(r"a", "alpha"))
print(re.search(r"[a-z].*[a-z]", "Denzel Python")) # Return lowercase letters from the 1st lowercase to the last