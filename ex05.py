your_name = 'Zed A. Shaw'
your_age = 35 # not a lie
your_height = 74 # inches
your_height_cm = your_height * 2.54
your_weight = 180 # lbs
your_weight_kg = your_weight * 0.453592
your_eyes = 'Blue'
your_teeth = 'White'
your_hair = 'Brown'

print "Let's talk about %s." % your_name
print "He's %d centimeters tall." % your_height_cm
print "He's %d kilograms heavy." % your_weight_kg
print "Actually that's not too heavey."
print "He's got %s eyes and %s hair." % (your_eyes, your_hair)
print "His teeth are usually %s depending on the coffee." % your_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    your_age, your_height, your_weight, your_age + your_height + your_weight)
