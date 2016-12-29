from sys import argv

script, input_file = argv

def print_all(f):   # define a function to read the file
    print f.read()

def rewind(f): # define a function to rewind the file to its byte 0
    f.seek(0)

def print_a_line(line_count, f): # define a function to print certain line from a file
    print line_count, f.readline()

current_file = open(input_file) # open the input file

print "First let's print the whole file:\n"

print_all(current_file) # print all the contents in the input file

print "Now let's rewind, kind of like a tape."

rewind(current_file)   # rewind the opened file to the start

print "Let's print three lines:"

current_line = 1                          # print the first line of the input file
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
