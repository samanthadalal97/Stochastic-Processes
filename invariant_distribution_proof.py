import numpy
#make matrix

myMatrix = numpy.matrix([[1/3,1/2,1/6,0],[1/2,1/8,1/4,1/8],[1/4,1/2,0,1/4],[0,0,1/2,1/2]])

invariantDist = [.304, .297, .216, .182]

#find the invariant distribution

A = numpy.linalg.matrix_power(myMatrix,100)[0]  #use built in numpy function to raise matrix to 100th power to see invariant distribution

print("The invariant distribution that can be found by raising P to the 100th power is: ", A)

# part b return time
s = [1,2,3,4]


invariant_list_1 = []

for i in range(4):  # for each of the states 1,2,3,4
    count_for_return_time = []
    move = i
    for a in range(10000):  # run simulation
        count = 0   # counter for how plays it takes to return to state
        while move != i or count==0:
            move = numpy.random.choice(len(s), p=myMatrix.tolist()[move])
            count += 1  # how many moves until I return to my state
        count_for_return_time.append(count)             # for each of the 10,000 simulations keep a list of how long it takes to return to state i
    print("The mean return time for from state %s is %.3f" %(s[i], sum(count_for_return_time)/10000.0))
    invariant_list_1.append(1 / (sum(count_for_return_time) / 10000))# part c: invariant distribution is the inverse of the expected value of return time
print("The invariant distribution is: ", invariant_list_1) # print invariant distribution



'''
find invariant distrbution (1/meancounter)

part d do the same thing as part c but 100,000 times
goal is to show as m approaches a very large number, the probabilities converge to the invariant distribution given the
process is positive recurrent, closed, finite, and aperiodic. 

'''

for i in range(4):  # for each of the states 1,2,3,4
    move = i
    count_return_time = []
    for a in range(100000):   #run simulation to mimic going to infinitiy
        count = 0
        while move != i or count==0:
            move = numpy.random.choice(len(s), p=myMatrix.tolist()[move])
            count += 1  # counter for how plays it takes to return to state
        count_return_time.append(count) #append count to list for each trial after you've returned to starting state
    print("The long term frequency of hitting state %s is %.3f" %(s[i], 1/(sum(count_return_time)/100000)))
