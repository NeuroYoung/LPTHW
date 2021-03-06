# first to learn how to store the results of loops somewhere
# that is an important property in Python
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this fruit kind of for-loop goes through a list
for number in the_count:
    print ("this is count {!r}" .format(number))

# same as above
for fruit in fruits:
    print ("A fruit of type: {!s}" .format(fruit))

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print ("I got {!r}" .format(i))

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print ("Adding {!r} to the list." .format(i))
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print ("Element was: {!r}" .format(i))

ele = []
ele = range(0,6)
for i in ele:
    print ("ele was: {!r}" .format(i))
