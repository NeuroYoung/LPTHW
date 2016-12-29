# There is no end in the way toward brilliant

def cheese_and_crackers(cheese_count, boxes_of_crackers): #define a function
    print "You have %d cheeses!" % cheese_count  # first print related to the first arg
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:" # assign the numbers directly to the function
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:" # assign variables to the function
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # "run" "call" "use" the function


print "We can even do math inside too:" # math process could be done within the arg assignment part
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:" # combination of math and variable in arg assignment part
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
