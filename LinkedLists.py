#  File: LinkedLists.py
#  Description: Simulate a list of utilities
#  Student's Name: Weiyi Wang
#  Student's UT EID: ww6874
#  Course Name: CS 313E 
#  Unique Number: 87530
#
#  Date Created: 7/12/2016
#  Date Last Modified: 7/15/2016

class Node(object):
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newData):
        self.data = newData

    def setNext(self,newNext):
        self.next = newNext


class LinkedList(object):

    def __init__(self):
        sentinel = Node(None)
        self.head = sentinel

    def isEmpty(self):
        return self.head.getNext() == None

    def remove(self,item):
        current = self.head.getNext()
        previous = self.head
        found = False

        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        previous.setNext(current.getNext())

    # Assume the original list is already in order
    def addInOrder (self,item):

        current = self.head.getNext()
        previous = self.head
        stop = False

        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        temp.setNext(current)
        previous.setNext(temp)

    # Check if the linked list contains item
    def findUnordered(self,item):
        current = self.head.getNext()
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    # Check if the linked list contains item
    # This time assume the list is in order
    def findOrdered(self,item):
        current = self.head.getNext()
        found = False

        # If the current value ever exceeds the value of the item
        # then the item is not in the list
        while current != None and not found:
            if current.data == item:
                found = True

            # Once the current data value is greater than the item
            # the search has failed
            elif current.data > item:
                return found
            else:
                current = current.getNext()

        return found


    # Insert an item as the first node following the head
    # Utilize the sentinel node
    def addFirst(self,item):

        temp = Node(item)
        temp.setNext(self.head.getNext())
        self.head.setNext(temp)

    # Add an item as the last node of the linked list
    def addLast(self,item):

        temp = Node(item)
        temp.setNext(None)

        # Check through the nodes
        current = self.head
        # Search for the end of the list, where the next pointer is None
        while current.getNext() != None:
            current = current.getNext()

        current.setNext(temp)

        
        

    def __str__(self):
        llString = ''
        lineCount = 0
        current = self.head.getNext()
        while current != None:

            if lineCount == 10:
                llString = llString + '\n'
                lineCount = 0
            llString = llString + current.getData() + '  '
            current = current.getNext()

            lineCount += 1

        return (llString)
        
    def getLength (self):
        current = self.head.getNext()
        count = 0

        while current != None:
            count += 1
            current = current.getNext()

        return count

    # Delete an item from an unordererd list
    # Return true if the item is in it, 
    def delete(self,item):
        current = self.head.getNext()
        prev = self.head
        found = False

        while current != None and not found:
            if current.getData() == item:

                # Check if item is at the end of the list
                if current.getNext() == None:
                    prev.setNext(None)

                # Else, set previous to skip to the node following current
                else:
                    
                    prev.setNext(current.getNext())
                    
                found = True
            else:
                prev = current
                current = current.getNext()

        return found


    # Makes a copy of the list
    def copyList(self):

        # Start with a blank linked list
        copy = LinkedList()

        current = self.head.getNext()
        while current != None:
            copy.addLast(current.data)
            current = current.getNext()

        return copy
            
    # Makes a reverse copy of the list
    # Same code as copyList except add nodes to beginning instead of end
    def reverseList(self):

        # Start with a blank linked list
        reverseCopy = LinkedList()

        current = self.head.getNext()
        while current != None:
            reverseCopy.addFirst(current.data)
            current = current.getNext()

        return reverseCopy

    # Make a new sorted list out the original linked list
    # Same code as copyList except add nodes in order
    def sortList(self):

        # Start with a blank linked list
        sortedCopy = LinkedList()

        current = self.head.getNext()
        while current != None:
            sortedCopy.addInOrder(current.data)
            current = current.getNext()

        return sortedCopy   

    # Checks if the list is sorted or not
    def isSorted(self):

        # By default the list is sorted
        sort = True

        current = self.head.getNext()
        prev = self.head

        # Skip the first first node because first node can't possibly be out of order
        # This avoids the hassle with the head
        prev = current
        current = current.getNext()

        
        while current != None and sort == True:

            # If the previous value is ever greater than the current value
            # then the list is out of order
            if prev.getData() > current.data:
                sort = False
            prev = current
            current = current.getNext()

        return sort
                

    # Merges two lists together
    def mergeList(self,b):

        mergedList = LinkedList()

        # Copy the first list to mergedList in sorted order
        current = self.head.getNext()
        while current != None:
            mergedList.addInOrder(current.data)
            current = current.getNext()
        
        # Set the last node of the first list
        # to point to the first node of the second list
        current = b.head.getNext()        

        currentb = b.head.getNext()
        while currentb != None:
            mergedList.addInOrder(currentb.data)
            currentb = currentb.getNext()
        

        return mergedList


    def isEqual(self,b):

        
        # Go through self and see if b matches at every node
        current = self.head.getNext()
        currentb = b.head.getNext()

        # If the lengths aren't equal, they are not the same
        # Also prevents the lists from going next when one is already finished
        if self.getLength() != b.getLength():
            return(False)

        
        
        while current != None and (current!=None or currentb!=None):

            # Compare the data for each Node
            if current.data != currentb.data:
                return (False)

            # If one linked list reaches the end while the other keeps going
            # then they are not equal

            

            

            current = current.getNext()
            currentb = currentb.getNext()

        return (True)

    def removeDuplicates(self):

        # Glean a copy
        gleanedCopy = LinkedList()
    
        # First handle the empty case
        if self.isEmpty():
            return self

        # If the data is not in the list, add it to dataList
        dataList = []

        current = self.head.getNext()
        while current != None:
            if current.data not in dataList:
                dataList.append(current.data)
                gleanedCopy.addLast(current.data)
                current = current.getNext()


            # If it's in the dataList, keep going, just don't add to the copy
            else:
                current = current.getNext()

        
        return gleanedCopy
    


def main():

   print ("\n\n***************************************************************")
   print ("Test of addFirst:  should see 'node34...node0'")
   print ("***************************************************************")
   myList1 = LinkedList()
   for i in range(35):
      myList1.addFirst("node"+str(i))

   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of addLast:  should see 'node0...node34'")
   print ("***************************************************************")
   myList2 = LinkedList()
   for i in range(35):
      myList2.addLast("node"+str(i))

   print (myList2)

   print ("\n\n***************************************************************")
   print ("Test of addInOrder:  should see 'alpha delta epsilon gamma omega'")
   print ("***************************************************************")
   greekList = LinkedList()
   greekList.addInOrder("gamma")
   greekList.addInOrder("delta")
   greekList.addInOrder("alpha")
   greekList.addInOrder("epsilon")
   greekList.addInOrder("omega")
   print (greekList)

   print ("\n\n***************************************************************")
   print ("Test of getLength:  should see 35, 5, 0")
   print ("***************************************************************")
   emptyList = LinkedList()
   print ("   Length of myList1:  ", myList1.getLength())
   print ("   Length of greekList:  ", greekList.getLength())
   print ("   Length of emptyList:  ", emptyList.getLength())

   print ("\n\n***************************************************************")
   print ("Test of findUnordered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'node25' in myList2: ",myList2.findUnordered("node25"))
   print ("   Searching for 'node35' in myList2: ",myList2.findUnordered("node35"))

   print ("\n\n***************************************************************")
   print ("Test of findOrdered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'epsilon' in greekList: ",greekList.findOrdered("epsilon"))
   print ("   Searching for 'omicron' in greekList: ",greekList.findOrdered("omicron"))

   print ("\n\n***************************************************************")
   print ("Test of delete:  should see 'node25 found', 'node34 found',")
   print ("   'node0 found', 'node40 not found'")
   print ("***************************************************************")
   print ("   Deleting 'node25' (random node) from myList1: ")
   if myList1.delete("node25"):
      print ("      node25 found")
   else:
      print ("      node25 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node34' (first node) from myList1: ")
   if myList1.delete("node34"):
      print ("      node34 found")
   else:
      print ("      node34 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node0'  (last node) from myList1: ")
   if myList1.delete("node0"):
      print ("      node0 found")
   else:
      print ("      node0 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node40' (node not in list) from myList1: ")
   if myList1.delete("node40"):
      print ("      node40 found")
   else:
      print ("   node40 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of copyList:")
   print ("***************************************************************")
   greekList2 = greekList.copyList()
   print ("   These should look the same:")
   print ("      greekList before delete:")
   print (greekList)
   print ("      greekList2 before delete:")
   print (greekList2)
   greekList2.delete("alpha")
   print ("   This should only change greekList2:")
   print ("      greekList after deleting 'alpha' from second list:")
   print (greekList)
   print ("      greekList2 after deleting 'alpha' from second list:")
   print (greekList2)
   greekList.delete("omega")
   print ("   This should only change greekList1:")
   print ("      greekList after deleting 'omega' from first list:")
   print (greekList)
   print ("      greekList2 after deleting 'omega' from first list:")
   print (greekList2)

   print ("\n\n***************************************************************")
   print ("Test of reverseList:  the second one should be the reverse")
   print ("***************************************************************")
   print ("   Original list:")
   print (myList1)
   print ("   Reversed list:")
   myList1Rev = myList1.reverseList()
   print (myList1Rev) 

   print ("\n\n***************************************************************")
   print ("Test of sortList:  the second list should be the first one sorted")
   print ("***************************************************************")
   planets = LinkedList()
   planets.addFirst("Mercury")
   planets.addFirst("Venus")
   planets.addFirst("Earth")
   planets.addFirst("Mars")
   planets.addFirst("Jupiter")
   planets.addFirst("Saturn")
   planets.addFirst("Uranus")
   planets.addFirst("Neptune")
   planets.addFirst("Pluto!")
   
   print ("   Original list:")
   print (planets)
   print ("   Sorted list:")
   sortedPlanets = planets.sortList()
   print (sortedPlanets)

   print ("\n\n***************************************************************")
   print ("Test of isSorted:  should see False, True")
   print ("***************************************************************")
   print ("   Original list:")
   print (planets)
   print ("   Sorted: ", planets.isSorted())
   sortedPlanets = planets.sortList()
   print ("   After sort:")
   print (sortedPlanets)
   print ("   Sorted: ", sortedPlanets.isSorted())

   print ("\n\n***************************************************************")
   print ("Test of isEmpty:  should see True, False")
   print ("***************************************************************")
   newList = LinkedList()
   print ("New list (currently empty):", newList.isEmpty())
   newList.addFirst("hello")
   print ("After adding one element:",newList.isEmpty())

   print ("\n\n***************************************************************")
   print ("Test of mergeList")
   print ("***************************************************************")
   list1 = LinkedList()
   list1.addLast("aardvark")
   list1.addLast("cat")
   list1.addLast("elephant")
   list1.addLast("fox")
   list1.addLast("lynx")
   print ("   first list:")
   print (list1)
   list2 = LinkedList()
   list2.addLast("bacon")
   list2.addLast("dog")
   list2.addLast("giraffe")
   list2.addLast("hippo")
   list2.addLast("wolf")
   print ("   second list:")
   print (list2)
   print ("   merged list:")
   list3 = list1.mergeList(list2)
   print (list3)

   print ("\n\n***************************************************************")
   print ("Test of isEqual:  should see True, False, True")
   print ("***************************************************************")
   print ("   First list:")
   print (planets)
   planets2 = planets.copyList()
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print (planets)
   planets2.delete("Mercury")
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print ("   Compare two empty lists:")
   emptyList1 = LinkedList()
   emptyList2 = LinkedList()
   print ("      Equal:  ",emptyList1.isEqual(emptyList2))

   print ("\n\n***************************************************************")
   print ("Test of removeDuplicates:  original list has 14 elements, new list has 10")
   print ("***************************************************************")
   dupList = LinkedList()
   print ("   removeDuplicates from an empty list shouldn't fail")
   newList = dupList.removeDuplicates()
   print ("   printing what should still be an empty list:")
   print (newList)
   dupList.addLast("giraffe")
   dupList.addLast("wolf")
   dupList.addLast("cat")
   dupList.addLast("elephant")
   dupList.addLast("bacon")
   dupList.addLast("fox")
   dupList.addLast("elephant")
   dupList.addLast("wolf")
   dupList.addLast("lynx")
   dupList.addLast("elephant")
   dupList.addLast("dog")
   dupList.addLast("hippo")
   dupList.addLast("aardvark")
   dupList.addLast("bacon")
   print ("   original list:")
   print (dupList)
   print ("   without duplicates:")
   newList = dupList.removeDuplicates()
   print (newList)

main()
