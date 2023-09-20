# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.

# It should look like this:

# Sam Harris => S.H

# patrick feeney => P.F
def abbrev_name(name):
    separation = name.split(" ")
    return separation[0][0].upper()+"."+separation[1][0].upper()




abbrev_name("sam harris")