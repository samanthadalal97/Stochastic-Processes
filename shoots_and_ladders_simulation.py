#Samantha Dalal
#Section: Wednesday @ 11am
import numpy

#note matrix excludes states 2, 5, 8. This is because you will never actual "be" at these states because they automatically take you to a different position
myMatrix = numpy.matrix([[0,.25,.25,.25,0,.25,0],[0,0,.5,.25,0,.25,0],[0,0,.25,.25,.25,.25,0],[0,0,.25,.25,.25,.25,0],[0,0,0,.5,0,.25,.25],[0,0,0,.5,0,.25,.25],[0,0,0,0,0,0,1]])

game_slots = [0,1,3,4,6,7,9]

wins = [] #counts how many times you play until you hit state 9 for each trial


for i in range(10000):

    count = 0
    move = 0    #you start off the board

#while you are not at the 6th position in game_slots - i.e state 9 - pick the next move from a list ranging from 0 - 6,
    #where each of these numbers corresponds to the index of a state in game_slots with the respective probabilities
    #from the row of your matrix that corresponds to the previous move
    #everytime you run the while loop, count will increment by 1, indicating 1 move. Once you win the game (you hit 6),
    #the value in count gets appended to the list wins and that represents how many rounds you played until you won in
    #the ith simulation
    while move != 6:
        move = numpy.random.choice(len(game_slots), p=myMatrix.tolist()[move])  #pick next move with prob corresponding
        #to the row of the transition matrix from the previous move
        count += 1  #increment rounds played by 1


    wins.append(count)


expectedNumberOfMoves = (sum(wins)/10000.0) #find average

print("The average number of moves before a game is finished is %s\n" %expectedNumberOfMoves)


#Part b
#want the prob off getting to 2 before 6 given you started at 4, where 2 is the index corresponding to state 3 and
#6 is the index corresponding to state 9 and 4 is the index corresponding to state 6

successfulTrials = 0    #counter for number of successful trials - i.e you hit 3 before 9

for i in range(10000):

    hasBeenAtThree = False  #checks whether or not you hit state 3

    newMove = 4

#while you have not hit state 9, keep playing - using the same logic as above in part a. Except now you want to check if
    #your newMove hits state 3 WHILE IT HAS NOT HIT STATE 9, and if so you say you had a successful trial and increment
    #the counter by 1.
    while newMove != 6:
        newMove = numpy.random.choice(len(game_slots), p=myMatrix.tolist()[newMove])    #pick next move with prob
        # corresponding to the row of the transition matrix from the previous move
        if newMove == 2:    #check if newMove hits state 3, if so say you had a successful trial
            hasBeenAtThree = True
    if hasBeenAtThree:
        successfulTrials += 1   #if you had a successful trial, increment your count by 1

probability3Before9 = (successfulTrials/10000.0)

print("The probability that Chidi hits state 3 before state 9, given that he started at state 6 is %s" %probability3Before9)
