import matplotlib.pyplot as plt
import time

def main():
    styles = list(plt.style.available)
    x = [3,1,6,5,7,8,5,4,10, 11] #for line and scatter plots
    y = [9,5,11,2,4,55,26,65,72, 80]
    n = [10,11,12]   #for bar plots
    m = [10, 30, 60] 
    styLen = len(styles)
    print("Welcome to Cyrus's matplotlib style program!")
    while True:
        userInput = int(input('''
        You can run 1 of two programs!
        Press 1 for the Style Browser
        Press 2 for the Style Examiner
        >>>>> '''))
        if userInput not in (1,2):
            print("ERROR: YOU DIDN'T PRESS 1 OR 2!!!!!")
            continue
        else:
            break

    if userInput == 1 :
        styleBrowser(styles, styLen, x, y, n, m)
        
    if userInput == 2:
        styleExamine(styles, styLen, x, y, n, m)
    return

def styleBrowser(styles, styLen, x, y, n, m):
    print("This is the style browser. Close each window for each graph to get to next one. ")
    for i in range(styLen):
        print("Testing: ", styles[i])
        plt.style.use(styles[i])
        plt.plot(x,y)
        plt.scatter(x,y)
        plt.bar(n,m)
        plt.title(styles[i])
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
        time.sleep(.2)

def styleExamine(styles, styLen, x, y, n, m):
    print("Welcome to the style examiner! Here are the 26 matplotlib styles: ")
    printList(styles, styLen)
    styleInput = str(input("What graphed style would you like to see? >> "))
    lowStyleInput = styleInput.lower()
    print(lowStyleInput)
    isStyle = styleInput.lower() in styles
    if isStyle: #trying to search through entire list to see if it matches up with input
        print("Testing: " + lowStyleInput)
        plt.style.use(styles[styles.index(lowStyleInput)])
        plt.plot(x,y)
        plt.title(styles[styles.index(lowStyleInput)])
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
        plt.pause(0.9)
        plt.close() #doesn't work
        styleExamine(styles, styLen, x, y, n, m)      
    else:
        print("Invalid style, try again.")
        styleExamine(styles, styLen, x, y, n, m) #RECURSION :D

def printList(styles, styLen):
    for i in range(styLen):
        print(styles[i])
if __name__ == '__main__':      
    main()        

#styleBrowser()
#styleExamine()
