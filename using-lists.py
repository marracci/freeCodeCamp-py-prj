# Lists example -- using open/closed square brackets means lists
friends = ["Jenna", "Jon", "Eric"]
friends1 = ["Jenna", 4, True]           # can input strings, numbers, booleans into lists
print(friends[0])                       # use brackets with index value to select a specific item in the list
print(friends[-1])                      # starting at beginning = 0; starting at end = -1
print(friends[1:])                      # grab all index values after a number, use [1:] where the colon signifies everything after
print(friends[0:1])                     # specify range
friends[1] = "mike"                     # change a specific item in the list


