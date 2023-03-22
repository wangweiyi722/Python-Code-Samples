# Input the list of rolls, return total scores for each frame
def convertScores(rollsList):
    
    scoreList = []

    # Create a list of numerically equivalent rolls
    numEq = []
    roll = 0
    while roll < len(rollsList):
        if rollsList[roll] == 'X':
            numEq.append(10)
        elif rollsList[roll] == '-':
            numEq.append(0)
        elif rollsList[roll] == '/':
            numEq.append(10-int(numEq[roll-1]))
        else:
            numEq.append(int(rollsList[roll]))

        roll = roll + 1

    # We can now use the numEq rolls to calculate values for spares and strikes
    roll = 0
    while len(scoreList) < 10:
        if rollsList[roll] == 'X':
            scoreList.append(10+numEq[roll+1]+numEq[roll+2])
        else:
            if rollsList[roll+1] == '/':
                scoreList.append(10+numEq[roll+2])
            else:
                scoreList.append(numEq[roll]+numEq[roll+1])
            roll = roll +1
        roll = roll + 1


    # Now generate a list of cumulative scores from the individual scores
    # Leave index 0 of the list the same. Start from index 1
    ind = 1
    while ind<10:
        scoreList[ind] = scoreList[ind]+scoreList[ind-1]
        ind = ind + 1
        

    
    return scoreList

def main():
    

    inFile = open('scores.txt','r')
    gamesList = inFile.readlines()
    gameNum=0

    # Remove the whitespace at the end of each line and split into individual characters
    while gameNum < len(gamesList):
        gamesList[gameNum] = gamesList[gameNum].rstrip().split()
        gameNum += 1

    allFrames = []
    allScores = []

    
    # Separate the rolls into frames
    for game in gamesList:

        frames = []

        roll = 0

        # First do the first 9 frames
        # Tenth frame is a special case, handled separately
        while len(frames)<9:
            if game[roll] == 'X':

                # For a strike, there is only one roll per frame
                frames.append('X')
                
            else:

                # For other cases there are 2 rolls per frame
                frames.append(game[roll]+' '+game[roll+1])
                roll = roll+1

            roll = roll+1

        # The tenthFrame contains all the remaining rolls.
        tenthFrame = ''
        while roll < len(game):
            
            tenthFrame = tenthFrame + game[roll] + ' '
            roll = roll + 1
            
        tenthFrame = tenthFrame.strip()
        frames.append(tenthFrame)
        scores = convertScores(game)

        allFrames.append(frames)
        allScores.append(scores)

    # Now I have a list of frames and a list of scores
    
    gameCounter = 0

    
    while gameCounter < len(gamesList):
        
        print('  1   2   3   4   5   6   7   8   9    10')
        print('+---+---+---+---+---+---+---+---+---+-----+')

        counter = 0
        while counter < 10:

            print('|',end='')
            print(allFrames[gameCounter][counter],end='')
            
            if (len(allFrames[gameCounter][counter])==1 or (len(allFrames[gameCounter][counter])==3 and counter==9)):
                print('  ',end='')
                
            counter = counter +1

        print('|')

        counter = 0
        while counter < 10:

            print('|',end='')

            if counter == 9:
                print(' '*(5-len(str(allScores[gameCounter][counter]))),end='')
            
            if (allScores[gameCounter][counter])<=9 and counter!=9:
                print('  ',end='')
            elif (10<=allScores[gameCounter][counter]<=99 and counter!=9):
                print(' ',end='')
            else:
                print('',end='')

            print(allScores[gameCounter][counter],end='')
            counter = counter +1

        print('|')
        print('+---+---+---+---+---+---+---+---+---+-----+')
        print()
        gameCounter = gameCounter+1
main()

