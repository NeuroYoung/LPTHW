from sys import argv # import argv from sys(module/library) into our enviroment

script, filename = argv # unpack the argv and assign it to 2 variables

txt = open(filename) # open the file you designated to filename

print "Here's your file %r:" % filename # print the file's name you wanna to open
print txt.read() # print the contents in the file

print "Type the filename again:" # suggest to input another file's name
file_again = raw_input(">") # input the name, assign it to the variable file_again

txt_again = open(file_again) # open the file

print txt_again.read() # read it
