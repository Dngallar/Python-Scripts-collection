#python 2
#
# TT SECURITIES, INCORPORATED
#
# Domingo Gallardo Saavedra

import math

def menu():
    """ a function that simply prints the menu """
    print "(0) Input a new list"
    print "(1) Print the current list"
    print "(2) Find the average price"
    print "(3) Find the standard deviation"
    print "(4) Find the min and its day"
    print "(5) Find the max and its day"
    print "(6) Your TT investment plan"
    print "(9) Quit"

def printList(L):
    print "Day Price"
    print "--- -----"
    for i in range(len(L)):
        print "", i, round(float(L[i]),2)
    print ""
    
def averagePrice(L):
    cant = len(L)
    suma = 0.0
    for i in L:
        suma += i
    return suma/cant
    
def standardDev(L):
    Lav = averagePrice(L)
    suma_sqr = 0
    largo = len(L)
    for i in L:
        suma_sqr += (i - Lav)**2
    return math.sqrt(suma_sqr/largo)
    
def minDay(L):
    min_in = L[0]
    indx_min = 0
    for i in range(1,len(L)):
        if L[i] < min_in:
            min_in = L[i]
            indx_min = i
    minimos = [min_in, indx_min]
    return minimos
    
def maxDay(L):
    max_in = L[0]
    indx_max = 0
    for i in range(1,len(L)):
        if L[i] > max_in:
            max_in = L[i]
            indx_max = i
    maximos = [max_in, indx_max]
    return maximos
    
def TTPlan(L):
    maxim = maxDay(L)
    minim = minDay(L)
    profit = maxim[0] - minim[0]
    TT_Plan = [minim[1], maxim[1], profit]
    return TT_Plan
    
def main():
    """ the main user-interaction loop """

    L = [20,10,30] # an initial list
    #L = [1,2,1,5,9]

    while True:   # the user-interaction loop9
        menu()
        uc = raw_input( "Enter your choice: " )
        print ""

        if uc == '9': # we want to quit
            break

        elif uc == '0': # we want to enter a new list
            numString = raw_input("Enter a new list: ")
            L = makeList(numString)
            
        elif uc == '1': # Print the current list
            printList(L)

        elif uc == '2': # average
            aveg = averagePrice(L)
            print "The average price is", aveg
            print ""
            
        elif uc == '3': # stardar deviation
            sdv = standardDev(L)
            print "The st. deviation is", sdv
            print ""
            
        elif uc == '4': # min Day
            min_day = minDay(L)
            print "The min is", min_day[0], "on day", min_day[1]
            print ""
            
        elif uc == '5': # max Day
            max_day = maxDay(L)
            print "The max is", max_day[0], "on day", max_day[1]
            print ""
        
        elif uc == '6': # TTS investment strategy
            TT_Plan = TTPlan(L)
            print "Your TTS investment strategy is to"
            print ""
            print "Buy on day",TT_Plan[0], "at price", L[TT_Plan[0]]
            print "Sell on day",TT_Plan[1], "at price", L[TT_Plan[1]]
            print ""
            print "For a total profit of", TT_Plan[2]
            print ""
            
        else:
            print "The choice",uc,"is not an option."
            print "Try again"

    print
    print "I knew you were going to quit!"

def makeList(numString):
    numString = numString.replace('[', '')
    numString = numString.replace(']', '')
    numList = numString.split(',')
    L = []
    for x in numList:
        L.append(float(x.strip()))
    return L