# Accessing the contents of a file, line by line
with open("week2/sample_file") as text:
    # Iterate now
    for lines in text:
        print(lines.upper()) # Print them in upper case
        