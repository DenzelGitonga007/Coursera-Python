# Accessing strings in a text without regex/regexp
log_text = "July : 34839 computer dell inspiron [3583] working 24/7"
# Get the index
index = log_text.index("[")
# Print the value at the index
# print(log_text[index+1:index+5])

# Using regex
import re
print(re.search(r"en", "Denzel", re.IGNORECASE))