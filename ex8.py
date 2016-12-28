formatter = "%r %r %r %r" # assign a string consisting of four formatters to the variable "formatter"

print formatter % (1, 2, 3, 4) # print formatter in which four integers in parenthesis replace the %r in the variable "formatter"
print formatter % ("one", "two", "three", "four") # print formatter in which four strings in parenthesis replace the %r in the variable "formatter"
print formatter % (True, False, False, True) # print formatter in which four boolean values in parenthesis replace the %r in the variable "formatter"
print formatter % (formatter, formatter, formatter, formatter) # print formatter in which four formatter-transformed strings in parenthesis replace the %r in the variable "formatter"
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
# print formatter in which four strings in parenthesis replace the %r in the variable "formatter"
