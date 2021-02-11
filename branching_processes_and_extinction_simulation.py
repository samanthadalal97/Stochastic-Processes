import numpy

unicorn = 1
for i in range(10):
    unicorn += random.choice((0,1,2,3), p=(.25,.25,.25,.25))