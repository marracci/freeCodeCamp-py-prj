
# Using functions with lists
luckyNumbers = [4,6,44,22,87,66,68]     # Lists can be modified. use [] to declare
friends = ["Jenna", "Jon", "Eric", "Adam"]
print(friends)
friends.extend(luckyNumbers)            # add items from a different declared list to 'friends' list
friends.append("Mario")                 # add item to end of list
print(friends)
friends.insert(1, "Jaromir")            # add this value and push other values one to right in list
friends.remove("Eric")                  # remove a specific element within the list
friends.pop()                           # removes final item from list
print(friends)
print(friends.index("Adam"))            # returns index of specific items
friends.count("Adam")                   # return a count of specific value
luckyNumbers.sort()                     # sorts list in alphabetical or numerical
print(luckyNumbers.reverse())           # reverse the order of the list

friends2 = friends.copy()               # copy items from one list into another
print(friends2)
friends.clear()                         # clear all items within the list


