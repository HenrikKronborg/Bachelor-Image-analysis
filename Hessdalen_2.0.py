#!/urs/bin/python
import time
import sys
import os

running = True
changed = False
resolutionX = resolutionY = 0
formatV = ""
formatX = ""

currentTime = 30
startTrim = 0
stopptrim = 0

#"Main"
def StartProgram():
    #Run this once at "startup"
#Starup start
    print("Initializing system...")
    time.sleep(0.1)
    #TODO: Initialize camera
    #Read configfile and set the values in the program
    #^TODO: Set
    ReadSettingsAndSet()
#Startup end

#Do this continiously
    while(running):
        
        CheckConfiguration()
        print("")
        print("Filming...")
        print("Filming...")
        print("Filming...")
        os.system("date")
              
        time.sleep(6)
        


    #TODO: Continiously camera-algorithm after the configuration.
        #Start filming, each frame goes through ...
    
#Does this once at start and once a change has been detected
def ReadSettingsAndSet():
    print("Reading configfile...")

#'with' makes sure to close the resource after
    with open("config.txt", "r") as file: 
        lines = file.readlines()
        #file.close()
    
    resolutionX = lines[0].strip()  #Reso X
    resolutionY = lines[1].strip()  #Reso Y
    formatV = lines[2].strip()      #YUY2, GREY8
    formatX = lines[3].strip()      #x-raw, bayern

    time.sleep(0.1)
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("******** Settings ********")
    print("")
    print("Resolution:",resolutionX,"x",resolutionY + ".")
    print("Format: " + formatV + ", " + formatX + ".")
    print("")
    print("**************************")
    print("")
    print("")
    print("")
    print("")
    print("")
    
    
    
#At the start of each "loop" check if there is a new configuration change    
def CheckConfiguration():
    print("")
    print("Checking changed.txt")
    with open("changed.txt", "r") as check:
        changedValue = check.readline()

    print(type(changedValue))
    print(changedValue)
    if changedValue == "hei\n":
        print("Change deteced.")
        global changed
        changed = True
	startTrim = "03"
	stoppTrim = "01"

	os.system("ffmpeg -i test.mp4 -ss 00:00:"+ startTrim + " -t 00:00:" + stoppTrim + " -async 1 -strict -2 test3.mp4")

    if changed == True:
        print("Implementing new configurations...")
        #TODO: Function that sets the new camerasettings /w config.txt
        #Actually just use ReadSettingsAndSet() :-)
        time.sleep(1)
       
        print("Configurations implemented.")
        changed = False
        with open("changed.txt", "w") as writeFile:
            writeFile.write("0")
        time.sleep(2)
    else:
         print("No changes, keeps running")
    
          


#Start of program
print("Starting up Hessdalen_2.0 ...")

#print()
#FrameOption = input('Enter framerate (7.5 / 15): ')
#print()

#print("Framerate set to", FrameOption + ".")

#print()
#FormatOption = input('Enter format (GREY8 / YUY2): ')
#print()
#print("Format set to",FormatOption + ".")
print("")

#Calls the "main"
StartProgram()
