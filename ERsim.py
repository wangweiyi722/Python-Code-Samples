#  File: ERsim.py
#  Description: Simulate an ER waiting room
#  Student's Name: Weiyi Wang
#  Student's UT EID: ww6874
#  Course Name: CS 313E 
#  Unique Number: 87530
#
#  Date Created: 7/8/2016
#  Date Last Modified: 7/9/2016

class Queue (object):
   def __init__(self):
      self.items = [ ]

   def isEmpty (self):
      return self.items == [ ]

   def enqueue (self, item):
      self.items.insert(0,item)

   def dequeue (self):
      return self.items.pop ()

   def size (self):
      return len(self.items)

   def peek (self):
      return self.items [len(self.items)-1]

# Input parameters are the three different queues
def treatNext(critical,serious,fair):
    # If there are people in the critical queue, treat them first
    if not critical.isEmpty():
        print('Treating',critical.peek(),'from the critical queue')
        critical.dequeue()

    # Else treat the serious queue
    elif not serious.isEmpty():
        print('Treating',serious.peek(),'from the serious queue')
        serious.dequeue()

    # If all three queues are empty, there are no patients
    elif fair.isEmpty():
        print('No patients in queue')

    # Else treat the fair queue
    else:
        print('Treating',fair.peek(),'from the fair queue')
        fair.dequeue()

        
def main():

    
    ER_file = open('ERsim.txt','r')

    # Read in the lines
    commands = ER_file.readlines()

    # Set up the different queues
    critical = Queue()
    serious = Queue()
    fair = Queue()

    # Go through the commands
    for command in commands:

        # Split each commands into words to make it easier to work with
        command = command.strip().split()

        # Add people to queues
        if command[0]=='add':

            # Add patients to different queues based on condition
            if command[2]=='Critical':
                print('Add patient',command[1],'to critical queue')
                critical.enqueue(command[1])
                
            elif command[2]=='Serious':
                print('Add patient',command[1],'to serious queue')
                serious.enqueue(command[1])

            elif command[2]=='Fair':
                print('Add patient',command[1],'to fair queue')
                fair.enqueue(command[1])

            print('Queues are:')
            print('Critical: ',end = '')
            print(critical.items)
            print('Serious: ',end = '')
            print(serious.items)
            print('Fair: ',end = '')
            print(fair.items)
            print()


        # Treat people in queues
        if command[0]=='treat':

            if command[1]=='next':

                print('Treat next patient')
                treatNext(critical,serious,fair)
                
                print('Queues are:')
                print('Critical: ',end = '')
                print(critical.items)
                print('Serious: ',end = '')
                print(serious.items)
                print('Fair: ',end = '')
                print(fair.items)
                print()
                
            elif command[1]=='all':

                print('Treat all patients')

                # Keep going until all the queues are empty
                while not(critical.isEmpty() and serious.isEmpty() and fair.isEmpty()):
                    treatNext(critical,serious,fair)
                    print('Queues are:')
                    print('Critical: ',end = '')
                    print(critical.items)
                    print('Serious: ',end = '')
                    print(serious.items)
                    print('Fair: ',end = '')
                    print(fair.items)
                    print()


        if command[0] =='exit':
            print('exit')
    


    

main()
