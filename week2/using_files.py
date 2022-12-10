# Accessing files in Python

# There are two ways to open a file:
# - Manual open
# - Using the "with" method

# Manual way
file_path = "week2\sample_file"
my_file = open(file_path) # the current directory is week2, and then the file name is "sample_file"
print(my_file.readline()) # readline() reads the contents on one line
print("...")
print(my_file.read()) # read() reads from the current position, to the end of the file
# Close the file
my_file.close()
print("...")

# Using the with method
with open(file_path) as file: # I used file here, instead of the "my_file", but it's the same file
    print(file.read())