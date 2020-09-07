pi = [3,1,4,1,5,9]
e = [2,7,1]

# Example problem (problem 0):
answer0 = [ e[0] ] + pi[-2:]     
print answer0
print ""

# Problem 1:
answer1 = e[1:3]
print answer1
print ""

# Problem 2:
answer2 = [pi[-1]] + [e[-1]]*2
print answer2
print ""

# Problem 3:
answer3 = pi[1:7]
print answer3
print ""

# Problem 4:
answer4 = e[2::-2] + pi[0:5:2]
print answer4
print ""


# starting strings for Homework 1

h = 'harvey'
m = 'mudd'
c = 'college'

# Problem 5:
answer5 = h[0] + h[4:] + h[-1] + c[1] + m[1]
print answer5
print ''

# Problem 6:
answer6 = c[0:4] + m[1:3] + h[-2]
print answer6
print ''

# Problem 7:
answer7 = h[1:6] + m[1:4]
print answer7
print ''

# Problem 8:
answer8= h[0:3] + m[-1] + c[-1] + h[0:3]*3
print answer8
print ''

# Problem 9:
answer9 = c[3:6] + c[1] + m[0] + h[-1] + c[4:6] + c[1]
print answer9
print ''

# Problem 10:
answer10 = c[0:6:2] + h[1:3] + c[0] + h[1] + c[2:4]
print answer10