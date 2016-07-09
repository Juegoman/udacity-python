import webbrowser
import time

breakCount = 0 #internal count of breaks taken
totalBreaks = 3 #how many breaks to take before the program completes
breakTime = 10 #time in seconds between each break

print("Execution started on " + time.ctime())
while breakCount < totalBreaks:
    time.sleep(breakTime)
    webbrowser.open("https://www.youtube.com/watch?v=aIZuhiKQlF8")
    breakCount+=1
    print("take it easy!!! breaks left: " + str(totalBreaks - breakCount))
