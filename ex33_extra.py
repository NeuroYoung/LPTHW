def nwhile(*args):
    up, increment = args
    i = 0
    result = []
    while i <= up:
        result.append(i)
        i = i + increment
    print(result)

# notice how to import the functions in Python: import ***
# notice how to avoid the "ex" when recall the certain function: from *** import ***
