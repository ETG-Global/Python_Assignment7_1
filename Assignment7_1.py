"""
Assignment 7.1: Given a sequence of n values x1, x2, ..., xn and a window size k>0, the k-th moving average of the 
given sequence is defined as follows: The moving average sequence has n-k+1 elements as shown below.
The moving averages with k=4 of a ten-value sequence (n=10) is shown below
i 1 2 3 4 5 6 7 8 9 10
===== == == == == == == == == == ==
Input 10 20 30 40 50 60 70 80 90 100
y1 25 = (10+20+30+40)/4
y2 35 = (20+30+40+50)/4
y3 45 = (30+40+50+60)/4
y4 55 = (40+50+60+70)/4
y5 65 = (50+60+70+80)/4
y6 75 = (60+70+80+90)/4
y7 85 = (70+80+90+100)/4
Thus, the moving average sequence has n-k+1=10-4+1=7 values.
Problem Statement: Write a function to find moving average in an array over a window:
Test it over [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150] and window of 3.
"""
def MovWinAvg(lst,win):         # function definition to calculate and print moving average in an array
    lstlen = lst.__len__()      # finding length of the list array supplied
    i = 0
    while i < (lstlen - win +1):    # looping till last window of elements is reached
        val = 0
        ele = i
        j = 0
        mystr=''
        mytemplst = []
        while j < win:              # looping till each element inside window
            val = lst[ele] + val
            mytemplst.append(lst[ele])      #Preparing a temp list of elements for printing later
            ele = ele+1
            j = j+1
        print(str('Y'+str(i+1)),' ', "{0:.2f}".format(val/win), ' = (', sep = '', end= '') # printing Avg 2 decimal points
        for itm in mytemplst:                                          # looping to print temp list items 
            print(itm,'+' , sep = '', end= '')   # printing each item in templist
        print(str('\b)/'+ str(win)))   # printing window number
        i = i+1

mylst = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]  # List array input
mywin = 3   # Moving window value

MovWinAvg(mylst,mywin)  # calling our function



  