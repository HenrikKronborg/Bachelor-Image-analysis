#!/urs/bin/python
import time

running = True
changed = False
resolutionX = 0
resolutionY = 0
formatV = ""
formatX = ""
def StartProgram():
    #Run this once at "startup"
    print("Initializing system...")
    time.sleep(0.1)
    ReadSettingsAndSet()            #Read configfile and use the values in the program
    #Startup end
    #while(running):
    with open("changed.txt", "r") as check:
        changedValue = check.readline()
        print(changedValue)
        if changedValue == "1":
            print("ALERT")
    if changed != True:
        print("Implementing new configurations...")



        changed = False
    else:
        print("sann")
    
    #If changed.txt contains the value "1",

    
    print("File read. " + FormatOption + " is chosen.")
    

def ReadSettingsAndSet():
    print("Reading configfile...")

    with open("config.txt", "r") as file: #Lukker filen etter operasjonene
        lines = file.readlines()
        #file.close()
    
    resolutionX = lines[0].strip()  #Reso X
    resolutionY = lines[1].strip()  #Reso Y
    formatV = lines[2].strip()      #YUY2, GREY8
    formatX = lines[3].strip()      #x-raw, bayern

    time.sleep(0.1)
    print()
    print("**** Settings ****")
    print()
    print("Resolution:",resolutionX,"x",resolutionY + ".")
    print("Format: " + formatV + ", " + formatX + ".")
    print()
    print("******************")
    print()
print("Starting up Hessdalen_2.0 ...")

print()
FrameOption = input('Enter framerate (7.5 / 15): ')
print()

print("Framerate set to", FrameOption + ".")

print()
FormatOption = input('Enter format (GREY8 / YUY2): ')
print()
print("Format set to",FormatOption + ".")
print()
StartProgram()
