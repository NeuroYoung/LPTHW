tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "cat dog mine p\aig"
print "cat dog mine p\big"
print "cat dog mine p\fig"
print "cat dog mine p\nig"
print "cat dog mine p\N{name}ig"
print "cat dog mine p\rig"
print "cat dog mine pu'\U0001F47E'ig"
print "cat dog mine pig"
print "cat dog mine p\vig"
print "cat dog mine p\oooig"
print "cat dog mine p\hhig"

print "Do you love %s ?" % "\nDaniel"
