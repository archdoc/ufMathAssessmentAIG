# OBJECTIVE 2 - Solve quadratic equations using the zero-factor principle
    # [if $ab=0$, then either $a=0$ or $b=0$].
# Types of problems:
    # Type 1 - a=p and c=q where p, q prime
    # Type 2 - a and c are fairly composite (ac has at least 8 factors)

from sympy.abc import x
import random

print "I have begun running Objective 2 Type 1"

#load("../Code/generalPurposeMethods.sage")
#load("generalPurposeMethods.sage")
def generateFactors(minimumPrime, maximumPrime, numberOfFactors):
    listPrimes = prime_range(minimum, maximum)
    aFactors = [random.sample(listPrimes, 1) for i in xrange(numberOfFactors)]
    cFactors = [random.sample(listPrimes, 1) for i in xrange(numberOfFactors)]
    return [aFactors, cFactors]
def generateSolution(minimum, maximum, factors):
    aFactors = factors[0]
    cFactors = factors[1]
    a = numpy.prod(aFactors)
    c = numpy.prod(cFactors)
    b = maybeMakeNegative(random.randint(minimum, maximum))
    d = maybeMakeNegative(random.randint(minimum, maximum))
    #This will guarantee that we always generate solutions with b < d
    if(b < d):
        return [a, b, c, d]
    else:
        return [c, d, a, b]
def generateSolutionInterval(solution, intervalRange):
    intervalList = [[]]*len(solution)
    for i in xrange(0, len(solution)):
        intervalList[i] = createInterval(solution[i], intervalRange)
    return intervalList
def generateProblem(solution):
    a, b, c, d = solution
    return [a*c, a*d + b*c, b*d]
def distractorA1(solution):
    a = float(solution[0])
    b = float(solution[1])
    c = float(solution[2])
    d = float(solution[3])

    z1 = float(-b)
    z2 = float(-d/(a*c))

    if (z1<=z2):
        return [z1, z2]
    else:
        return[z2, z1]
def distractorC1(solution):
    a = float(solution[0])
    b = float(solution[1])
    c = float(solution[2])
    d = float(solution[3])

    z1 = float(-b/(a*c))
    z2 = -d

    if (z1<=z2):
        return [z1, z2]
    else:
        return[z2, z1]

def distractorLumpedCFactors(solution, factors):
    aFactors = factors[0]
    cFactors = factors[1]
    a = float(solution[0])
    b = float(solution[1])
    c = float(solution[2])
    d = float(solution[3])

    index = random.randint(0,len(aFactors)-1)
    a = float(a/(aFactors[index][0]))
    c = c*aFactors[index][0]

    z1 = float(-b/a)
    z2 = float(-d/c)

    if (z1<=z2):
        return [z1, z2]
    else:
        return[z2, z1]

def distractorLumpedAFactors(solution, factors):
    aFactors = factors[0]
    cFactors = factors[1]

    a = float(solution[0])
    b = float(solution[1])
    c = float(solution[2])
    d = float(solution[3])

    index = random.randint(0,len(aFactors)-1)
    c = float(c/(cFactors[index][0]))
    a = a*cFactors[index][0]

    z1 = float(-b/a)
    z2 = float(-d/c)

    if (z1<=z2):
        return [z1, z2]
    else:
        return[z2, z1]

def generateProblemDisplay(problem):
    a, b, c = problem
    if b < 0:
        if c < 0:
            display = "%s x^2 - %s x - %s" %(a, -b, -c)
        else:
            display = "%s x^2 - %s x + %s" %(a, -b, c)
    else:
        if c < 0:
            display = "%s x^2 + %s x - %s" %(a, b, -c)
        else:
            display = "%s x^2 + %s x + %s" %(a, b, c)
    return display

# Type 3 - a and c are fairly composite (ac has at least 6 factors)
intervalRange = 5
minimum = 2
maximum = 5
numberOfFactors = 2

factors = generateFactors(minimum, maximum, numberOfFactors)
solution = generateSolution(minimum, maximum, factors)
distractor1 = distractorA1(solution)
distractor2 = distractorC1(solution)
distractor3 = distractorLumpedCFactors(solution, factors)
distractor4 = distractorLumpedAFactors(solution, factors)

while ( (distractor1 == distractor2) or (distractor1 == distractor3) or (distractor1 == distractor4) or (distractor2 == distractor3) or (distractor2 == distractor4) or (distractor3 == distractor4) ):
    factors = generateFactors(minimum, maximum, numberOfFactors)
    solution = generateSolution(minimum, maximum, factors)
    distractor1 = distractorA1(solution)
    distractor2 = distractorC1(solution)
    distractor3 = distractorLumpedCFactors(solution, factors)
    distractor4 = distractorLumpedAFactors(solution, factors)

problem = generateProblem(solution)
generalFormTypeOne = problem[0] * x**2 + problem[1] * x + problem[2]
s0 = float(solution[0])
s1 = float(solution[1])
s2 = float(solution[2])
s3 = float(solution[3])
z0 = float(-s1/s0)
z1 = float(-s3/s2)
if (z0 < z1):
    answer = [z0, z1]
else:
    answer = [z1, z0]

generalFormTypeOne = problem[0] * x**2 + problem[1] * x + problem[2]
solutionList = [answer, distractor1, distractor2, distractor3, distractor4]
print solutionList
precision = 1
intervalOptions = createIntervalOptions(solutionList, intervalRange, precision)

solutionInterval = intervalOptions[0]
distractor1Interval = intervalOptions[1]
distractor2Interval = intervalOptions[2]
distractor3Interval = intervalOptions[3]
distractor4Interval = intervalOptions[4]

displayStem = 'Solve the quadratic equation below. Then, choose the intervals that the solutions $x_1$ and $x_2$ belong to, with $x_1 \\leq x_2$.'
displayProblem = "%s = 0" %generateProblemDisplay(problem)
displaySolution = "x_1 = %s \\text{ and } x_2 = %s" %(round(answer[0], 3), round(answer[1], 3))
comments = "General Comments: This may be difficult to guess by looking at it, so you may want to use factoring by grouping."

solutionInterval.append("* Correct option.")
distractor1Interval.append(" Distractor: Corresponds to the pair of solutions $x_1 = %s$ and $x_2 = %s$." %(round(distractor1[0], 3), round(distractor1[1], 3) ) )
distractor2Interval.append(" Distractor: Corresponds to the pair of solutions $x_1 = %s$ and $x_2 = %s$." %(round(distractor2[0], 3), round(distractor2[1], 3) ) )
distractor3Interval.append(" Distractor: Corresponds to the pair of solutions $x_1 = %s$ and $x_2 = %s$." %(round(distractor3[0], 3), round(distractor3[1], 3) ) )
distractor4Interval.append(" Distractor: Corresponds to the pair of solutions $x_1 = %s$ and $x_2 = %s$." %(round(distractor4[0], 3), round(distractor4[1], 3) ) )

answerList = [solutionInterval, distractor1Interval, distractor2Interval, distractor3Interval, distractor4Interval]
random.shuffle(answerList)

c0 = "x_1 \\in [%s, %s] \\text{ and } x_2 \\in [%s, %s]" %(answerList[0][0][0], answerList[0][0][1], answerList[0][1][0], answerList[0][1][1])
c1 = "x_1 \\in [%s, %s] \\text{ and } x_2 \\in [%s, %s]" %(answerList[1][0][0], answerList[1][0][1], answerList[1][1][0], answerList[1][1][1])
c2 = "x_1 \\in [%s, %s] \\text{ and } x_2 \\in [%s, %s]" %(answerList[2][0][0], answerList[2][0][1], answerList[2][1][0], answerList[2][1][1])
c3 = "x_1 \\in [%s, %s] \\text{ and } x_2 \\in [%s, %s]" %(answerList[3][0][0], answerList[3][0][1], answerList[3][1][0], answerList[3][1][1])
c4 = "x_1 \\in [%s, %s] \\text{ and } x_2 \\in [%s, %s]" %(answerList[4][0][0], answerList[4][0][1], answerList[4][1][0], answerList[4][1][1])
choices = [c0, c1, c2, c3, c4]
choiceComments = [answerList[0][2], answerList[1][2], answerList[2][2], answerList[3][2], answerList[4][2]]

writeQuestionToFile(moduleNumber, version, problemNumber, displayStem, displayProblem)
writeSolutionAndOptionsToFile(moduleNumber, version, displaySolution, choices, choiceComments)
writeCommentsToFile(moduleNumber, version, comments)

print "I have finished running Objective 2 Type 1"
