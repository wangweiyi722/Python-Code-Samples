#  File: htmlChecker.py
#  Description:
#  Student's Name:
#  Student's UT EID:
#  Course Name: CS 313E 
#  Unique Number: 
#
#  Date Created: 7/4/2016
#  Date Last Modified:


# Define a class Stack and class methods
class Stack (object):
   def __init__(self):
      self.items = [ ]

   def isEmpty (self):
      return self.items == [ ]

   def push (self, item):
      self.items.append (item)

   def pop (self):
      return self.items.pop ()

   def peek (self):
      return self.items [len(self.items)-1]

   def size (self):
      return len(self.items)

# The function getTag gets the text between the < >
# Input parameters are the text file and the start index
def getTag(text,index):

    tag = ''
    # End the loop if it reaches the end of the text
    while index<len(text):

        if text[index] == '>':
            return tag

        tag = tag + text[index]
        index = index + 1




def main():
    in_file = open('htmlfile.txt','r')

    # Read in all the lines of the html file
    lines = in_file.readlines()

    # Take all of the lines and compile them into one string
    # Easier to work with
    inputString = ''
    for line in lines:
        inputString = inputString + line



    # List for storing tags
    tagList = []
    index = 0

    # Go through the input String
    while index < len(inputString):

        # Any time a '<' is encountered, call getTag to get a tag
        if inputString[index] == '<':
            tagList.append(getTag(inputString,index+1))

        index = index + 1
        
    # Now we have a list of tags
    print(tagList)

    # Keep track of whether or not there is an error
    error = False

    # Create a new stack used for verifying tags
    tagStack = Stack()

    # VALIDTAGS is a list of all the unique tags in the html file
    VALIDTAGS = []

    # Exceptions are tags that do not need closing tags
    EXCEPTIONS = ['br','meta http-equiv="content-type" content="text/html; charset=windows-1252"','hr']

    # Go through the tagList
    ind = 0

    
    while ind < len(tagList):


        tag = tagList[ind]

        # If the tag is in the list of EXCEPTIONS, don't do anything with it
        if tag in EXCEPTIONS:
            print('Tag',tag,'does not need to match: stack is still',tagStack.items)
        
        # If the tag is not an end tag and not in the list of exceptions, then it must be a start tag.
        # Push it onto the stack
        elif (not tag.startswith('/')) and (tag not in EXCEPTIONS):
            tagStack.push(tag)

            # If this tag is not in VALIDTAGS, then add it to VALIDTAGS
            if tag not in VALIDTAGS:
                VALIDTAGS.append(tag)

                
            print('Tag',tag,'is pushed: stack is now',tagStack.items)

        # If the tag is an end tag, check to see if it has a matching start tag
        elif tag.startswith('/'):

            # If there is, pop off the start tag
            if ('/'+str(tagStack.peek()))==tag:
                
                tagStack.pop()
                print('Tag',tag,'matches top of the stack: stack is now',tagStack.items)

            # If the tag does not match, then there is an error
            else:

                print('Error: tag is',tag,'but top of stack is',str(tagStack.peek()))
                error = True
                break
                
        

        ind = ind + 1


    if not error and tagStack.isEmpty():
        print('Processing complete.  No mismatches found.')

    elif not error and not tagStack.isEmpty():
        print('Processing complete.  Unmatched tags remain on stack:',tagStack.items)


    print()
    print('Valid tags')
    print(VALIDTAGS)
    print()
    print('Exceptions')
    print(EXCEPTIONS)
    print()
main()
