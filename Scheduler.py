#  File: Scheduler.py
#  Description: Simulate a processor
#  Student's Name: Weiyi Wang
#  Student's UT EID: ww6874
#  Course Name: CS 313E 
#  Unique Number: 87530
#
#  Date Created: 7/16/2016
#  Date Last Modified: 7/20/2016


# Use nodes to generate the queues
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


# Queue is just a linked list with FIFO properties
class Queue(object):
    def __init__(self):
        sentinel = Node(None)
        self.head = sentinel

    def isEmpty(self):
        return self.head.getNext() == None


    # Insert an item as the last node
    def enqueue(self,item):

        temp = Node(item)
        temp.setNext(None)

        # Check through the nodes
        current = self.head
        # Search for the end of the list, where the next pointer is None
        while current.getNext() != None:
            current = current.getNext()

        current.setNext(temp)

    # Take the first item from the front of the queue
    def dequeue(self):
        self.head = self.head.getNext()
        
    
    def __str__(self):
        llString = ''
        lineCount = 0
        current = self.head.getNext()
        while current != None:

            if lineCount == 10:
                llString = llString + '\n'
                lineCount = 0
            llString = llString +'->' + '[P'+str(current.getData().ID) + ']'
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

# Input parameters are the IDs, duration of the process, and the list of I/O timestamps
class Process(object):
    def __init__(self,process_ID,duration,timeStamps):
        self.ID = process_ID
        self.duration = duration
        self.timeStamps = timeStamps


    def __str__(self):
        return str(self.ID)+str(self.duration)+str(self.timeStamps)

def displayQueues(top,mid,bot):
    print('top level:',top)
    print('mid level:',mid)
    print('bot level:',bot)
    print()

class Scheduler():
    
    def init(self):
        self.processes = []

    def takeProcesses(self,process_list):
        self.processes = process_list


    def run(self):

        # Store the list of processes of the output into a string
        processString = ''

        # Keep track of the number of processes in each row for formatting purposes
        rowCount = 0
        
        # Generate the three different priority queues
        top = Queue()
        mid = Queue()
        bot = Queue()

        

        # Put all the processes into the high priority queue
        # Also calculate total duration
        totalDur = 0
        for process in self.processes:
            top.enqueue(process)
            totalDur += process.duration


        print('Start scheduling...')
        displayQueues(top,mid,bot)

        
        # As long as these queues are not empty, keep going
        while not top.isEmpty() or not mid.isEmpty() or not bot.isEmpty():


            # Add and -> at the beginning of each process
            processString = processString + '->'

            # First execute processes in high priority queue
            if not top.isEmpty():

                print('Running top P',top.head.getNext().data.ID,sep = '')

                print(top.head.getNext().data.duration)
                print(top.head.getNext().data.timeStamps)
                
                # If the duration of the process is less than 10 and no more I/Os are called
                if top.head.getNext().data.duration <= 10 and top.head.getNext().data.timeStamps == []:

                    print('P',top.head.getNext().data.ID,' finished',sep = '')

                    # The process acts for the remainder of its duration
                    processString = processString + 'P' + str(top.head.getNext().data.ID) + '(' + str(top.head.getNext().data.duration)+')'
                    
                    top.dequeue()
                    displayQueues(top,mid,bot)
                    


                # If duration is greater than the 10 ms of time for top queue
                # and there are no I/O timestamps remaining
                # then subtract 10 ms from duration and then move to mid queue
                elif top.head.getNext().data.duration > 10 and top.head.getNext().data.timeStamps == []:

                    print('P',top.head.getNext().data.ID,' is pre-empted',sep = '')

                    # The process acts for 10 ms
                    processString = processString + 'P' + str(top.head.getNext().data.ID) + '(10)'
                    
                    top.head.getNext().data.duration -= 10
                    
                    mid.enqueue(top.head.getNext().data)
                    top.dequeue()

                    displayQueues(top,mid,bot)



                # If the duration and the next time stamp are both greater than 10
                # then subtract 10 from duration and from time stamp values
                # and move to the next queue
                elif top.head.getNext().data.duration > 10 and top.head.getNext().data.timeStamps[0] > 10:

                    print('P',top.head.getNext().data.ID,' is pre-empted',sep = '')

                    # The process acts for 10 ms
                    processString = processString + 'P' + str(top.head.getNext().data.ID) + '(10)'
                    top.head.getNext().data.duration -= 10

                    n=0
                    while n < len(top.head.getNext().data.timeStamps):
                        top.head.getNext().data.timeStamps[n] -= 10
                        n += 1

                    
                    mid.enqueue(top.head.getNext().data)
                    top.dequeue()

                    displayQueues(top,mid,bot)




                # If the duration is greater than the next I/O timestamp, move the process to the back of the top queue
                # Reduce the duration by the amount of time on the timestamp, and remove that used up timestamp
                # Subtract the time used up from each of the rest of the timestamps

                # The previous elif statement guarantees that they will be less than 10
                elif top.head.getNext().data.duration > top.head.getNext().data.timeStamps[0]:

                    print('P',top.head.getNext().data.ID,' blocked for I/O',sep='')

                    # The process acts for the duration until its first timestamp
                    processString = processString + 'P' + str(top.head.getNext().data.ID) + '(' + str(top.head.getNext().data.timeStamps[0])+ ')'
                    
                    top.head.getNext().data.duration -= top.head.getNext().data.timeStamps[0]

                    n=1
                    while n < len(top.head.getNext().data.timeStamps):
                        top.head.getNext().data.timeStamps[n] -= top.head.getNext().data.timeStamps[0]
                        n += 1

                    
                    del top.head.getNext().data.timeStamps[0]
                    
                    top.enqueue(top.head.getNext().data)
                    top.dequeue()

                    displayQueues(top,mid,bot)



            # Then execute processes in mid priority queue
            elif not mid.isEmpty():

                print('Running mid P',mid.head.getNext().data.ID,sep = '')

                print(mid.head.getNext().data.duration)
                print(mid.head.getNext().data.timeStamps)
                
                # If the duration of the process is less than 100 and no more I/Os are called
                if mid.head.getNext().data.duration <= 100 and mid.head.getNext().data.timeStamps == []:

                    print('P',mid.head.getNext().data.ID,' finished',sep='')

                    # Use up the remainder of the duration
                    processString = processString + 'P' + str(mid.head.getNext().data.ID) + '(' + str(mid.head.getNext().data.duration)+ ')'
                    
                    mid.dequeue()
                    displayQueues(top,mid,bot)



                # If duration is greater than the 100 ms of time for mid queue
                # and there are no I/O timestamps remaining
                # then subtract 100 ms from duration and then move to bot queue
                elif mid.head.getNext().data.duration > 100 and mid.head.getNext().data.timeStamps == []:

                    print('P',mid.head.getNext().data.ID,' is pre-empted',sep='')

                    # Process acts for 100 ms
                    processString = processString + 'P' + str(mid.head.getNext().data.ID) + '(100)'

                    
                    mid.head.getNext().data.duration -= 100
                    
                    bot.enqueue(mid.head.getNext().data)
                    mid.dequeue()

                    displayQueues(top,mid,bot)



                # If the next time stamp is greater than 100
                # the duration must automatically be greater than 100 as well.
                # Subtract 100 from duration and from time stamp values
                # and move to the next queue
                elif mid.head.getNext().data.timeStamps[0] > 100:

                    print('P',mid.head.getNext().data.ID,' is pre-empted',sep='')

                    # Process acts for 100 ms
                    processString = processString + 'P' + str(mid.head.getNext().data.ID) + '(100)'
                    
                    mid.head.getNext().data.duration -= 100

                    n=0
                    while n < len(mid.head.getNext().data.timeStamps):
                        mid.head.getNext().data.timeStamps[n] -= 100
                        n += 1

                    
                    bot.enqueue(mid.head.getNext().data)
                    mid.dequeue()

                    displayQueues(top,mid,bot)




                # If the duration is greater than the next I/O timestamp, move the process back to the top queue
                # Reduce the duration by the amount of time on the timestamp, and remove that used up timestamp
                # Subtract the time used up from each of the rest of the timestamps

                # The previous elif statement guarantees that the timestamp value will be less than 100
                elif mid.head.getNext().data.duration > mid.head.getNext().data.timeStamps[0]:

                    print('P',mid.head.getNext().data.ID,' blocked for I/O',sep='')

                    # Process acts for the amount of time until the I/O
                    processString = processString + 'P' + str(mid.head.getNext().data.ID) + '(' + str(mid.head.getNext().data.timeStamps[0])+ ')'
                    
                    mid.head.getNext().data.duration -= mid.head.getNext().data.timeStamps[0]

                    n=1
                    while n < len(mid.head.getNext().data.timeStamps):
                        mid.head.getNext().data.timeStamps[n] -= mid.head.getNext().data.timeStamps[0]
                        n += 1

                    
                    del mid.head.getNext().data.timeStamps[0]
                    
                    top.enqueue(mid.head.getNext().data)
                    mid.dequeue()

                    displayQueues(top,mid,bot)


            # Then execute processes in bot priority queue
            elif not bot.isEmpty():

                print('Running bot P',bot.head.getNext().data.ID,sep = '')

                print(bot.head.getNext().data.duration)
                print(bot.head.getNext().data.timeStamps)
                
                # If the duration of the process is less than 1000 and no more I/Os are called
                if bot.head.getNext().data.duration <= 1000 and bot.head.getNext().data.timeStamps == []:

                    print('P',bot.head.getNext().data.ID,' finished',sep='')

                    # Process acts for remainder of duration
                    processString = processString + 'P' + str(bot.head.getNext().data.ID) + '(' + str(bot.head.getNext().data.duration)+ ')'
                    
                    bot.dequeue()
                    displayQueues(top,mid,bot)



                # If duration is greater than the 1000 ms of time for bot queue
                # and there are no I/O timestamps remaining
                # then subtract 1000 ms from duration and then move to end of bot queue
                elif bot.head.getNext().data.duration > 1000 and bot.head.getNext().data.timeStamps == []:

                    print('P',bot.head.getNext().data.ID,' is pre-empted',sep='')

                    # Process acts for 1000 ms
                    processString = processString + 'P' + str(bot.head.getNext().data.ID) + '(1000)'
                    
                    bot.head.getNext().data.duration -= 1000
                    
                    bot.enqueue(bot.head.getNext().data)
                    bot.dequeue()

                    displayQueues(top,mid,bot)



                # If the next time stamp is greater than 1000
                # the duration must automatically be greater than 1000 as well.
                # Subtract 1000 from duration and from time stamp values
                # and move to the end of the bot queue
                elif bot.head.getNext().data.timeStamps[0] > 1000:

                    print('P',bot.head.getNext().data.ID,' is pre-empted',sep='')

                    # Process acts for 1000 ms
                    processString = processString + 'P' + str(bot.head.getNext().data.ID) + '(1000)'
                    
                    bot.head.getNext().data.duration -= 1000

                    n=0
                    while n < len(bot.head.getNext().data.timeStamps):
                        bot.head.getNext().data.timeStamps[n] -= 1000
                        n += 1

                    
                    bot.enqueue(bot.head.getNext().data)
                    bot.dequeue()

                    displayQueues(top,mid,bot)


                # If the duration is greater than the next I/O timestamp, move the process back to the mid queue
                # Reduce the duration by the amount of time on the timestamp, and remove that used up timestamp
                # Subtract the time used up from each of the rest of the timestamps

                # The previous elif statement guarantees that the timestamp value will be less than 1000
                elif bot.head.getNext().data.duration > bot.head.getNext().data.timeStamps[0]:

                    print('P',bot.head.getNext().data.ID,' blocked for I/O',sep='')

                    # Process acts for the amount of time until the I/O
                    processString = processString + 'P' + str(bot.head.getNext().data.ID) + '(' + str(bot.head.getNext().data.timeStamps[0])+ ')'
                    
                    bot.head.getNext().data.duration -= bot.head.getNext().data.timeStamps[0]

                    n=1
                    while n < len(bot.head.getNext().data.timeStamps):
                        bot.head.getNext().data.timeStamps[n] -= bot.head.getNext().data.timeStamps[0]
                        n += 1

                    
                    del bot.head.getNext().data.timeStamps[0]
                    
                    mid.enqueue(bot.head.getNext().data)
                    bot.dequeue()

                    displayQueues(top,mid,bot)
            rowCount += 1
            if rowCount == 5:
                processString = processString + '\n'
                rowCount = 0

        print()
        print('Total time used to run:',totalDur)
        print()

        print('Resulting Schedule')
        print(processString)


            
def main():

    fh = open("Processes.txt","r")
    process_list = []
    scheduler = Scheduler()

    for line in fh:
        data = line.strip().split(";")
        
        process_list.append(Process(int(data[0]),int(data[1]),eval(data[2])))
        

    
    scheduler.takeProcesses(process_list)
    
    scheduler.run()


    
main()
