# + plus + does plus
# - minus  does minus
# / slash  means separation
# * asterisk does multiply
# % percent means the remainder when doing a division operation
# < less-than to check whether the left is less than the right
# > greater-than to check whether the left is greater than the right
# <- less-than-equal to check whether the left is less than or equal to the right
# >- greater-than-equal to check whether the left is greater than or equal to the right

# PEMDAS Parentheses Exponents Multiplication Division Addition Subtraction
# / just drop the fractions, use floating!

print "I will now count my chickens:"

print "Hens", 25.0 + 30.0 / 6.0 # "," means the second command under the "print"
print "Roosters", 100.0 - 25.0 * 3.0 % 4.0

print "Now I will count the eggs:"

print 3.0 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7.0

print "What is 3 + 2?", 3.0 + 2
print "What is 5 - 7?", 5.0 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5.0 > -2 # ">" and other logical operations will output false or true
print "Is it greater or equal?", 5.0 >= -2
print "Is it less or equal?", 5.0 <= -2
