import random
import time
import sys
sys.setrecursionlimit(10000)

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
        sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue

def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

def almostSort(alist):

    # Number of swaps = 10% of list size
    for i in range(len(alist)//10):
        randNumA = random.randint(0,len(alist)-1)
        randNumB = random.randint(0,len(alist)-1)
        alist[randNumA],alist[randNumB] = alist[randNumB],alist[randNumA]

def main():
    print('Input type = Random')
    print('                    avg time   avg time   avg time')
    print('Sort function        (n=10)    (n=100)    (n=1000)')
    print('-----------------------------------------------------')

    # Store lists of 10, 100, 1000 random numbers
    randListS = [i for i in range(10)]
    randListM = [i for i in range(100)]
    randListL = [i for i in range(1000)]
    
    random.shuffle(randListS)    
    random.shuffle(randListM)
    random.shuffle(randListL)

    # bubbleSort
    print('bubbleSort'.rjust(13),end = '')

    avgS = 0
    avgM = 0
    avgL = 0

    for i in range(5):
        startTime = time.perf_counter()
        bubbleSort(randListS)
        endTime = time.perf_counter()
        avgS = avgS + endTime - startTime

        startTime = time.perf_counter()
        bubbleSort(randListM)
        endTime = time.perf_counter()
        avgM = avgM + endTime - startTime

        startTime = time.perf_counter()
        bubbleSort(randListL)
        endTime = time.perf_counter()
        avgL = avgL + endTime - startTime

    avgS = avgS/5
    avgM = avgM/5
    avgL = avgL/5
    print('{:8f}'.format(avgS).rjust(15),'{:8f}'.format(avgM).rjust(10),'{:8f}'.format(avgL).rjust(10),)

    random.shuffle(randListS)    
    random.shuffle(randListM)
    random.shuffle(randListL)

    # selectionSort
    print('selectionSort'.rjust(13),end = '')

    avgS = 0
    avgM = 0
    avgL = 0

    for i in range(5):
        startTime = time.perf_counter()
        selectionSort(randListS)
        endTime = time.perf_counter()
        avgS = avgS + endTime - startTime

        startTime = time.perf_counter()
        selectionSort(randListM)
        endTime = time.perf_counter()
        avgM = avgM + endTime - startTime

        startTime = time.perf_counter()
        selectionSort(randListL)
        endTime = time.perf_counter()
        avgL = avgL + endTime - startTime

    avgS = avgS/5
    avgM = avgM/5
    avgL = avgL/5
    print('{:8f}'.format(avgS).rjust(15),'{:8f}'.format(avgM).rjust(10),'{:8f}'.format(avgL).rjust(10),)

    random.shuffle(randListS)    
    random.shuffle(randListM)
    random.shuffle(randListL)

    # insertionSort
    print('insertionSort'.rjust(13),end = '')

    avgS = 0
    avgM = 0
    avgL = 0

    for i in range(5):
        startTime = time.perf_counter()
        insertionSort(randListS)
        endTime = time.perf_counter()
        avgS = avgS + endTime - startTime

        startTime = time.perf_counter()
        insertionSort(randListM)
        endTime = time.perf_counter()
        avgM = avgM + endTime - startTime

        startTime = time.perf_counter()
        insertionSort(randListL)
        endTime = time.perf_counter()
        avgL = avgL + endTime - startTime

    avgS = avgS/5
    avgM = avgM/5
    avgL = avgL/5
    print('{:8f}'.format(avgS).rjust(15),'{:8f}'.format(avgM).rjust(10),'{:8f}'.format(avgL).rjust(10),)

    random.shuffle(randListS)    
    random.shuffle(randListM)
    random.shuffle(randListL)

    # shellSort
    print('shellSort'.rjust(13),end = '')

    avgS = 0
    avgM = 0
    avgL = 0

    for i in range(5):
        startTime = time.perf_counter()
        shellSort(randListS)
        endTime = time.perf_counter()
        avgS = avgS + endTime - startTime

        startTime = time.perf_counter()
        shellSort(randListM)
        endTime = time.perf_counter()
        avgM = avgM + endTime - startTime

        startTime = time.perf_counter()
        shellSort(randListL)
        endTime = time.perf_counter()
        avgL = avgL + endTime - startTime

    avgS = avgS/5
    avgM = avgM/5
    avgL = avgL/5
    print('{:8f}'.format(avgS).rjust(15),'{:8f}'.format(avgM).rjust(10),'{:8f}'.format(avgL).rjust(10),)

    random.shuffle(randListS)    
    random.shuffle(randListM)
    random.shuffle(randListL)

    # mergeSort
    print('mergeSort'.rjust(13),end = '')

    avgS = 0
    avgM = 0
    avgL = 0

    for i in range(5):
        startTime = time.perf_counter()
        mergeSort(randListS)
        endTime = time.perf_counter()
        avgS = avgS + endTime - startTime

        startTime = time.perf_counter()
        mergeSort(randListM)
        endTime = time.perf_counter()
        avgM = avgM + endTime - startTime

        startTime = time.perf_counter()
        mergeSort(randListL)
        endTime = time.perf_counter()
        avgL = avgL + endTime - startTime

    avgS = avgS/5
    avgM = avgM/5
    avgL = avgL/5
    print('{:8f}'.format(avgS).rjust(15),'{:8f}'.format(avgM).rjust(10),'{:8f}'.format(avgL).rjust(10),)

    random.shuffle(randListS)    
    random.shuffle(randListM)
    random.shuffle(randListL)

    # quickSort
    print('quickSort'.rjust(13),end = '')

    avgS = 0
    avgM = 0
    avgL = 0

    for i in range(5):
        startTime = time.perf_counter()
        quickSort(randListS)
        endTime = time.perf_counter()
        avgS = avgS + endTime - startTime

        startTime = time.perf_counter()
        quickSort(randListM)
        endTime = time.perf_counter()
        avgM = avgM + endTime - startTime

        startTime = time.perf_counter()
        quickSort(randListL)
        endTime = time.perf_counter()
        avgL = avgL + endTime - startTime

    avgS = avgS/5
    avgM = avgM/5
    avgL = avgL/5
    print('{:8f}'.format(avgS).rjust(15),'{:8f}'.format(avgM).rjust(10),'{:8f}'.format(avgL).rjust(10),)


    print()
    print()
#---------------------------------------------------------------------
    print('Input type = Sorted')
    print('                    avg time   avg time   avg time')
    print('Sort function        (n=10)    (n=100)    (n=1000)')
    print('-----------------------------------------------------')

    # Store lists of 10, 100, 1000 sorted numbers
    randListS = [i for i in range(10)]
    randListM = [i for i in range(100)]
    randListL = [i for i in range(1000)]


    # bubbleSort
    print('bubbleSort'.rjust(13),end = '')

    avgS = 0
    avgM = 0
    avgL = 0

    for i in range(5):
        startTime = time.perf_counter()
        bubbleSort(randListS)
        endTime = time.perf_counter()
        avgS = avgS + endTime - startTime

        startTime = time.perf_counter()
        bubbleSort(randListM)
        endTime = time.perf_counter()
        avgM = avgM + endTime - startTime

        startTime = time.perf_counter()
        bubbleSort(randListL)
        endTime = time.perf_counter()
        avgL = avgL + endTime - startTime

    avgS = avgS/5
    avgM = avgM/5
    avgL = avgL/5
    print('{:8f}'.format(avgS).rjust(15),'{:8f}'.format(avgM).rjust(10),'{:8f}'.format(avgL).rjust(10),)



    # selectionSort
    print('selectionSort'.rjust(13),end = '')

    avgS = 0
    avgM = 0
    avgL = 0

    for i in range(5):
        startTime = time.perf_counter()
        selectionSort(randListS)
        endTime = time.perf_counter()
        avgS = avgS + endTime - startTime

        startTime = time.perf_counter()
        selectionSort(randListM)
        endTime = time.perf_counter()
        avgM = avgM + endTime - startTime

        startTime = time.perf_counter()
        selectionSort(randListL)
        endTime = time.perf_counter()
        avgL = avgL + endTime - startTime

    avgS = avgS/5
    avgM = avgM/5
    avgL = avgL/5
    print('{:8f}'.format(avgS).rjust(15),'{:8f}'.format(avgM).rjust(10),'{:8f}'.format(avgL).rjust(10),)



    # insertionSort
    print('insertionSort'.rjust(13),end = '')

    avgS = 0
    avgM = 0
    avgL = 0

    for i in range(5):
        startTime = time.perf_counter()
        insertionSort(randListS)
        endTime = time.perf_counter()
        avgS = avgS + endTime - startTime

        startTime = time.perf_counter()
        insertionSort(randListM)
        endTime = time.perf_counter()
        avgM = avgM + endTime - startTime

        startTime = time.perf_counter()
        insertionSort(randListL)
        endTime = time.perf_counter()
        avgL = avgL + endTime - startTime

    avgS = avgS/5
    avgM = avgM/5
    avgL = avgL/5
    print('{:8f}'.format(avgS).rjust(15),'{:8f}'.format(avgM).rjust(10),'{:8f}'.format(avgL).rjust(10),)



    # shellSort
    print('shellSort'.rjust(13),end = '')

    avgS = 0
    avgM = 0
    avgL = 0

    for i in range(5):
        startTime = time.perf_counter()
        shellSort(randListS)
        endTime = time.perf_counter()
        avgS = avgS + endTime - startTime

        startTime = time.perf_counter()
        shellSort(randListM)
        endTime = time.perf_counter()
        avgM = avgM + endTime - startTime

        startTime = time.perf_counter()
        shellSort(randListL)
        endTime = time.perf_counter()
        avgL = avgL + endTime - startTime

    avgS = avgS/5
    avgM = avgM/5
    avgL = avgL/5
    print('{:8f}'.format(avgS).rjust(15),'{:8f}'.format(avgM).rjust(10),'{:8f}'.format(avgL).rjust(10),)



    # mergeSort
    print('mergeSort'.rjust(13),end = '')

    avgS = 0
    avgM = 0
    avgL = 0

    for i in range(5):
        startTime = time.perf_counter()
        mergeSort(randListS)
        endTime = time.perf_counter()
        avgS = avgS + endTime - startTime

        startTime = time.perf_counter()
        mergeSort(randListM)
        endTime = time.perf_counter()
        avgM = avgM + endTime - startTime

        startTime = time.perf_counter()
        mergeSort(randListL)
        endTime = time.perf_counter()
        avgL = avgL + endTime - startTime

    avgS = avgS/5
    avgM = avgM/5
    avgL = avgL/5
    print('{:8f}'.format(avgS).rjust(15),'{:8f}'.format(avgM).rjust(10),'{:8f}'.format(avgL).rjust(10),)

   


    # quickSort
    print('quickSort'.rjust(13),end = '')

    avgS = 0
    avgM = 0
    avgL = 0

    for i in range(5):
        startTime = time.perf_counter()
        quickSort(randListS)
        endTime = time.perf_counter()
        avgS = avgS + endTime - startTime

        startTime = time.perf_counter()
        quickSort(randListM)
        endTime = time.perf_counter()
        avgM = avgM + endTime - startTime

        startTime = time.perf_counter()
        quickSort(randListL)
        endTime = time.perf_counter()
        avgL = avgL + endTime - startTime

    avgS = avgS/5
    avgM = avgM/5
    avgL = avgL/5
    print('{:8f}'.format(avgS).rjust(15),'{:8f}'.format(avgM).rjust(10),'{:8f}'.format(avgL).rjust(10),)


    print()
    print()
#----------------------------------------------------------------------
    print('Input type = Reverse')
    print('                    avg time   avg time   avg time')
    print('Sort function        (n=10)    (n=100)    (n=1000)')
    print('-----------------------------------------------------')

    # Store lists of 10, 100, 1000 reverse sorted numbers
    randListS = [i for i in range(10,0,-1)]
    randListM = [i for i in range(100,0,-1)]
    randListL = [i for i in range(1000,0,-1)]
    


    # bubbleSort
    print('bubbleSort'.rjust(13),end = '')

    avgS = 0
    avgM = 0
    avgL = 0

    for i in range(5):
        startTime = time.perf_counter()
        bubbleSort(randListS)
        endTime = time.perf_counter()
        avgS = avgS + endTime - startTime

        startTime = time.perf_counter()
        bubbleSort(randListM)
        endTime = time.perf_counter()
        avgM = avgM + endTime - startTime

        startTime = time.perf_counter()
        bubbleSort(randListL)
        endTime = time.perf_counter()
        avgL = avgL + endTime - startTime

    avgS = avgS/5
    avgM = avgM/5
    avgL = avgL/5
    print('{:8f}'.format(avgS).rjust(15),'{:8f}'.format(avgM).rjust(10),'{:8f}'.format(avgL).rjust(10),)

    randListS = [i for i in range(10,0,-1)]
    randListM = [i for i in range(100,0,-1)]
    randListL = [i for i in range(1000,0,-1)]

    # selectionSort
    print('selectionSort'.rjust(13),end = '')

    avgS = 0
    avgM = 0
    avgL = 0

    for i in range(5):
        startTime = time.perf_counter()
        selectionSort(randListS)
        endTime = time.perf_counter()
        avgS = avgS + endTime - startTime

        startTime = time.perf_counter()
        selectionSort(randListM)
        endTime = time.perf_counter()
        avgM = avgM + endTime - startTime

        startTime = time.perf_counter()
        selectionSort(randListL)
        endTime = time.perf_counter()
        avgL = avgL + endTime - startTime

    avgS = avgS/5
    avgM = avgM/5
    avgL = avgL/5
    print('{:8f}'.format(avgS).rjust(15),'{:8f}'.format(avgM).rjust(10),'{:8f}'.format(avgL).rjust(10),)

    randListS = [i for i in range(10,0,-1)]
    randListM = [i for i in range(100,0,-1)]
    randListL = [i for i in range(1000,0,-1)]

    # insertionSort
    print('insertionSort'.rjust(13),end = '')

    avgS = 0
    avgM = 0
    avgL = 0

    for i in range(5):
        startTime = time.perf_counter()
        insertionSort(randListS)
        endTime = time.perf_counter()
        avgS = avgS + endTime - startTime

        startTime = time.perf_counter()
        insertionSort(randListM)
        endTime = time.perf_counter()
        avgM = avgM + endTime - startTime

        startTime = time.perf_counter()
        insertionSort(randListL)
        endTime = time.perf_counter()
        avgL = avgL + endTime - startTime

    avgS = avgS/5
    avgM = avgM/5
    avgL = avgL/5
    print('{:8f}'.format(avgS).rjust(15),'{:8f}'.format(avgM).rjust(10),'{:8f}'.format(avgL).rjust(10),)

    randListS = [i for i in range(10,0,-1)]
    randListM = [i for i in range(100,0,-1)]
    randListL = [i for i in range(1000,0,-1)]

    # shellSort
    print('shellSort'.rjust(13),end = '')

    avgS = 0
    avgM = 0
    avgL = 0

    for i in range(5):
        startTime = time.perf_counter()
        shellSort(randListS)
        endTime = time.perf_counter()
        avgS = avgS + endTime - startTime

        startTime = time.perf_counter()
        shellSort(randListM)
        endTime = time.perf_counter()
        avgM = avgM + endTime - startTime

        startTime = time.perf_counter()
        shellSort(randListL)
        endTime = time.perf_counter()
        avgL = avgL + endTime - startTime

    avgS = avgS/5
    avgM = avgM/5
    avgL = avgL/5
    print('{:8f}'.format(avgS).rjust(15),'{:8f}'.format(avgM).rjust(10),'{:8f}'.format(avgL).rjust(10),)

    randListS = [i for i in range(10,0,-1)]
    randListM = [i for i in range(100,0,-1)]
    randListL = [i for i in range(1000,0,-1)]

    # mergeSort
    print('mergeSort'.rjust(13),end = '')

    avgS = 0
    avgM = 0
    avgL = 0

    for i in range(5):
        startTime = time.perf_counter()
        mergeSort(randListS)
        endTime = time.perf_counter()
        avgS = avgS + endTime - startTime

        startTime = time.perf_counter()
        mergeSort(randListM)
        endTime = time.perf_counter()
        avgM = avgM + endTime - startTime

        startTime = time.perf_counter()
        mergeSort(randListL)
        endTime = time.perf_counter()
        avgL = avgL + endTime - startTime

    avgS = avgS/5
    avgM = avgM/5
    avgL = avgL/5
    print('{:8f}'.format(avgS).rjust(15),'{:8f}'.format(avgM).rjust(10),'{:8f}'.format(avgL).rjust(10),)

    randListS = [i for i in range(10,0,-1)]
    randListM = [i for i in range(100,0,-1)]
    randListL = [i for i in range(1000,0,-1)]

    # quickSort
    print('quickSort'.rjust(13),end = '')

    avgS = 0
    avgM = 0
    avgL = 0

    for i in range(5):
        startTime = time.perf_counter()
        quickSort(randListS)
        endTime = time.perf_counter()
        avgS = avgS + endTime - startTime

        startTime = time.perf_counter()
        quickSort(randListM)
        endTime = time.perf_counter()
        avgM = avgM + endTime - startTime

        startTime = time.perf_counter()
        quickSort(randListL)
        endTime = time.perf_counter()
        avgL = avgL + endTime - startTime

    avgS = avgS/5
    avgM = avgM/5
    avgL = avgL/5
    print('{:8f}'.format(avgS).rjust(15),'{:8f}'.format(avgM).rjust(10),'{:8f}'.format(avgL).rjust(10),)

    print()
    print()
#-----------------------------------------------------------------------

    print('Input type = Almost sorted')
    print('                    avg time   avg time   avg time')
    print('Sort function        (n=10)    (n=100)    (n=1000)')
    print('-----------------------------------------------------')

    # Store lists of 10, 100, 1000 sorted numbers
    randListS = [i for i in range(10)]
    randListM = [i for i in range(100)]
    randListL = [i for i in range(1000)]

    almostSort(randListS)
    almostSort(randListM)
    almostSort(randListL)
    
    # bubbleSort
    print('bubbleSort'.rjust(13),end = '')

    avgS = 0
    avgM = 0
    avgL = 0

    for i in range(5):
        startTime = time.perf_counter()
        bubbleSort(randListS)
        endTime = time.perf_counter()
        avgS = avgS + endTime - startTime

        startTime = time.perf_counter()
        bubbleSort(randListM)
        endTime = time.perf_counter()
        avgM = avgM + endTime - startTime

        startTime = time.perf_counter()
        bubbleSort(randListL)
        endTime = time.perf_counter()
        avgL = avgL + endTime - startTime

    avgS = avgS/5
    avgM = avgM/5
    avgL = avgL/5
    print('{:8f}'.format(avgS).rjust(15),'{:8f}'.format(avgM).rjust(10),'{:8f}'.format(avgL).rjust(10),)

    almostSort(randListS)
    almostSort(randListM)
    almostSort(randListL)

    # selectionSort
    print('selectionSort'.rjust(13),end = '')

    avgS = 0
    avgM = 0
    avgL = 0

    for i in range(5):
        startTime = time.perf_counter()
        selectionSort(randListS)
        endTime = time.perf_counter()
        avgS = avgS + endTime - startTime

        startTime = time.perf_counter()
        selectionSort(randListM)
        endTime = time.perf_counter()
        avgM = avgM + endTime - startTime

        startTime = time.perf_counter()
        selectionSort(randListL)
        endTime = time.perf_counter()
        avgL = avgL + endTime - startTime

    avgS = avgS/5
    avgM = avgM/5
    avgL = avgL/5
    print('{:8f}'.format(avgS).rjust(15),'{:8f}'.format(avgM).rjust(10),'{:8f}'.format(avgL).rjust(10),)

    almostSort(randListS)
    almostSort(randListM)
    almostSort(randListL)

    # insertionSort
    print('insertionSort'.rjust(13),end = '')

    avgS = 0
    avgM = 0
    avgL = 0

    for i in range(5):
        startTime = time.perf_counter()
        insertionSort(randListS)
        endTime = time.perf_counter()
        avgS = avgS + endTime - startTime

        startTime = time.perf_counter()
        insertionSort(randListM)
        endTime = time.perf_counter()
        avgM = avgM + endTime - startTime

        startTime = time.perf_counter()
        insertionSort(randListL)
        endTime = time.perf_counter()
        avgL = avgL + endTime - startTime

    avgS = avgS/5
    avgM = avgM/5
    avgL = avgL/5
    print('{:8f}'.format(avgS).rjust(15),'{:8f}'.format(avgM).rjust(10),'{:8f}'.format(avgL).rjust(10),)

    almostSort(randListS)
    almostSort(randListM)
    almostSort(randListL)

    # shellSort
    print('shellSort'.rjust(13),end = '')

    avgS = 0
    avgM = 0
    avgL = 0

    for i in range(5):
        startTime = time.perf_counter()
        shellSort(randListS)
        endTime = time.perf_counter()
        avgS = avgS + endTime - startTime

        startTime = time.perf_counter()
        shellSort(randListM)
        endTime = time.perf_counter()
        avgM = avgM + endTime - startTime

        startTime = time.perf_counter()
        shellSort(randListL)
        endTime = time.perf_counter()
        avgL = avgL + endTime - startTime

    avgS = avgS/5
    avgM = avgM/5
    avgL = avgL/5
    print('{:8f}'.format(avgS).rjust(15),'{:8f}'.format(avgM).rjust(10),'{:8f}'.format(avgL).rjust(10),)

    almostSort(randListS)
    almostSort(randListM)
    almostSort(randListL)

    # mergeSort
    print('mergeSort'.rjust(13),end = '')

    avgS = 0
    avgM = 0
    avgL = 0

    for i in range(5):
        startTime = time.perf_counter()
        mergeSort(randListS)
        endTime = time.perf_counter()
        avgS = avgS + endTime - startTime

        startTime = time.perf_counter()
        mergeSort(randListM)
        endTime = time.perf_counter()
        avgM = avgM + endTime - startTime

        startTime = time.perf_counter()
        mergeSort(randListL)
        endTime = time.perf_counter()
        avgL = avgL + endTime - startTime

    avgS = avgS/5
    avgM = avgM/5
    avgL = avgL/5
    print('{:8f}'.format(avgS).rjust(15),'{:8f}'.format(avgM).rjust(10),'{:8f}'.format(avgL).rjust(10),)

    almostSort(randListS)
    almostSort(randListM)
    almostSort(randListL)

    # quickSort
    print('quickSort'.rjust(13),end = '')

    avgS = 0
    avgM = 0
    avgL = 0

    for i in range(5):
        startTime = time.perf_counter()
        quickSort(randListS)
        endTime = time.perf_counter()
        avgS = avgS + endTime - startTime

        startTime = time.perf_counter()
        quickSort(randListM)
        endTime = time.perf_counter()
        avgM = avgM + endTime - startTime

        startTime = time.perf_counter()
        quickSort(randListL)
        endTime = time.perf_counter()
        avgL = avgL + endTime - startTime

    avgS = avgS/5
    avgM = avgM/5
    avgL = avgL/5
    print('{:8f}'.format(avgS).rjust(15),'{:8f}'.format(avgM).rjust(10),'{:8f}'.format(avgL).rjust(10),)


    print()
    print()
    

    
main()
