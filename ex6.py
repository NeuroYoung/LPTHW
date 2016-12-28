x = "There are %d types of people." % 10 # assign a string to x, using formatter %d, %d = 10
binary = "binary" # assign a string to binary
do_not = "don't" # assign a string to do_not
y = "Those who know %s and those who %s." % (binary, do_not)  # assign a string to y, using formatter %s, %s = (binary, do_not)

print x # print x
print y

print "I said: %r." % x # print a string, using formatter %r, %r = x
print "I also said: '%s'." % y

hilarious = False # assign boolean value False to variable hilarious
joke_evaluation = "Isn't that joke so funny?! %r" # assign a string to joke_evaluation, using formatter %r, but no designation of the formatter

print joke_evaluation % hilarious # print the string the joke_evaluation stands for, and using variable hilarious to replace the %r in joke_evaluation

w = "This is the left side of ..."  # assign a string to w
e = "a string with a right side." # assign a string to e

print w + e # print a string combination of w and e
