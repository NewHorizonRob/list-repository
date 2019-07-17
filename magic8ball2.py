import random

#a list stored into the varible messages (remeber list indexes are separated by commas)
messages = ['It is certain',
        'It is decidely so ',
         'Yes definetly ',
         'Reply hazy try again ',
         'Ask again later',
         'Concentrate and ask again',
         'My reply is no',
         'Outlook not so good',
         'Very doubtful']

print(messages[random.randint(0,len(messages))-1]) 
# must use  brackets when dealing with list and other mehtods outside of list methods
#the randint is passed 0 and length if messages - 1
# must include the -1 due to the possibility of being out of range 