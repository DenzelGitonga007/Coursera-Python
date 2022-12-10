# Accessing files in Python

# There are two ways to open a file:
# - Manual open
# - Using the "with" method

# Manual way
my_file = open("week2\sample_file") # the current directory is week2, and then the file name is "sample_file"
print(my_file.readline()) # readline() reads the contents on one line
print("...")
print(my_file.read()) # read() reads from the current position, to the end of the file
