spam = ['cat', 'bat', 'rat', 'elephant']
print(spam)

# in a list the last value starts the -1 index when looking at it backwards
# ex : spam[-1] will return the 'elephant' string

# slicing is [inclusive:exclusive]
# ex: spam[0:3] will return ['cat', 'bat', 'rat']
# ex: spam[:] will return a COPY of the entire list

# can change indexes in lists by doing the following:
# ex: spam[2] = spam [1] this changes 'rat' to 'bat' or:
# spam [2] = 'Robert' changes the second index to 'Robert'
# spam[2] = 12345
# this method will replace the value at that index

# Lists can be concatenated 
# [1,2,3] + ['A', 'B', 'C'] = [1, 2, 3, 'A', 'B', 'C'] 
# can throw the above into a variable as well as having a list variable plus list
# ex: spam = spam + [1, 2, 3] will return ['cat', 'bat', 'rat', 'elephant', 1, 2, 3] in the spam variable
# * - replicates the index values within the list 
# when concatenating a variable or user input you must use square brackets 
# ex:  
#    name = input()     
#    if name == '': 
#        break 
#    catNames = catNames + [name]  this line concatenates the user input to the list catNames
                            #       [] is used to concatenate all variables to lists

# Values can be removed from lists as well
# ex: del spam[2] will remove the 'rat' from spam - del statement removes by the index value

# for loops can be used with lists - basically will step through every index in the list
# ex: for i in range(len(List)):
#           do something 
# range(len()) - gets the length of the list then turns it into a integer for range to read 
# refer to forlists.py for extra help 

# lists also have methods 
# index() - finds value of a list = spam.index('cat') will return 0
# duplicates values in a list index() will only return the first appearance of the value  
# append() - adds values to the end of a list = spam.append('moose') will add 'moose' to spam list
# insert() - adds values to the list by index = spam.insert(2, 'chicken') will add chicken at the 2nd index
# sort() - sorts the list in ASCIIbetical order = spam.sort() (CANT SORT INTEGERS AND STRINGS TOGETHER)
# spam.sort(reverse=True) - sorts the list in reverse order
# spam.sort(key=str.lower) - sorts the list in Alphebetical order regardless of capitalization 


