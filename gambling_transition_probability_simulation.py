import numpy
z = numpy.zeros((46,46))
myMatrix = numpy.asmatrix(z)

#part a

'''create matrix
- for each of the rows after row 1 and before row 45, change the value to the left and right of index i to reflect 
the probabilities of winning or losing $1
- for position 0,0 in my matrix fill that value with probability = 1 because if you're at zero you stay at zero
-for position 45,45 in my matrix fill that value with probability = 1 because if you're at 45 you end the game and stay
'''

for i in range(1, 45):
    myMatrix[i, i-1] = .51
    myMatrix[i, i+1] = .49
myMatrix[0, 0] = 1
myMatrix[45, 45] = 1

'''
Create my fundamental matrix:
- First making Q - the sub matrix that shows the probability of going from
one transient state to the next
- Doing (I-Q)^-1 so that I have the expected time one is in each of the transient states
'''

myQ = myMatrix[1:45,1:45]


#identity minus Q

identity = numpy.identity(44)

take_inverse = identity - myQ


fundamental = numpy.linalg.inv(take_inverse)

#part b

'''
We are looking for probability of absorption into state 0, given that we started at 15. Thus we want to take our 
fundamental matrix and multiply it by our R matrix and find the 15,0 entry
'''

r_matrix_1 = myMatrix[:, [0,45]]  #select only columns 0 and 45
r_matrix_final = r_matrix_1[1:45]   #select only rows 1-44
absorption_prob = fundamental*r_matrix_final
prob_15_to_0 = absorption_prob[14,0]
print(prob_15_to_0)
#part c

'''
We are looking for probability of absorption into state 45, given that we started at 15. Thus we want to take our 
fundamental matrix and multiply it by our R matrix and find the 15,45 entry
'''
prob_15_to_45 = absorption_prob[14,1]
print(prob_15_to_45)


#Python part a & b

wins = 0    # counts how many wins you have out of 500 trials - i.e how many times you get $45, conversely 500-wins
            # is how many times you go bust (how many times you hit $0)
for i in range(500):
    dollars = 15    #you start with 15 dollars
    while dollars != 0 and dollars != 45:   #while you haven't yet won or lost
        dollars += numpy.random.choice([-1, 1],p=[.51, .49])    #increment or decrease your dollar amount based on p or q
                                                                #note we are only picking from -1 and 1 cause you can
                                                                #only either gain a dollar or loose a dollar
    if dollars == 45:   #if you you've won (dollars = 45), increment your win count
        wins += 1
print("The probability of hitting $0 (losing/going bust) is: %s" % float((500-wins)/500.0)) #part a
print("The probability of hitting $45 (winning) is: %s" % float(wins/500.0))    #part b








