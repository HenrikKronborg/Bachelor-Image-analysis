#!/urs/bin/python
import threading
import time
import sys
import os
import cv2
import numpy as np

running = True
changed = False
resolutionX = resolutionY = 0
formatV = ""
formatX = ""

<<<<<<< Updated upstream
filmIntervall = 0
currentTime = 0
startTrim = 0
stopptrim = 0
duration = 0
counter = 0


# "Main"
=======
#"Main"
>>>>>>> Stashed changes
def StartProgram():
    #Run this once at "startup"
#Starup start
<<<<<<< Updated upstream
	print("Initializing system...")
	time.sleep(0.1)
	#TODO: Initialize camera
	#Read configfile and set the values in the program
	#^TODO: Set
	ReadSettingsAndSet()
	#Start the 0-60s timer that is unaffected by all other code(thread)
	example = ThreadingExample()
################################################# Startup end #################################################

#Do this continiously
	while(running):
		#_Only at start(?)
		#CheckConfiguration()
		print("")
		print("Filming...")
		#print("Filming...")
		#print("Filming...")
		#os.system("date")
			  
		time.sleep(1)

		#Simulert deteksjon som varer i 7 sek
		#1 og 0 vil evt komme ut(return) fra grupperings-algoritmen
		if counter == 5:
			AlarmPhase(1)

		if counter == 12:
			AlarmPhase(0)
                #Om counter har gått i 60 sekunder: stopp å filme(?), lagre video, trim og send til server, start å filme ny sekvens.
			#evt: film i 1 time, lagre alle steder som skal trimmes.
		if counter == 15:
			#print(startTrim, ", ", stoppTrim, ",", duration)
			print(startTrim)
			print(duration)
			os.system("ffmpeg -i test15.mp4 -ss 00:00:" + str(startTrim) + " -t 00:00:" + str(duration) + " -async 1 -strict -2 test51.mp4")

			
	#TODO: Continiously camera-algorithm after the configuration.
	#Start filming, each frame goes through ...
	

	
	
	

	
		  
def AlarmPhase(isDetect):
	#Variabler som holder styr på tiden
	#ta inn filmetid (0-60s), 
	#variabel som sjekker om det fortsatt er alarmstatus /boo
		#isDetect er enten 0 eller 1 --> kommer fra grupperings-algo
		#Så lenge isDetect er sann 
	global stoppTrim
	global startTrim
	global duration

	if isDetect == 1:
		print("")
		print(" *** DETEKSJON ***")
		startTrim = counter
	else:
		print("")
		print(" *** Deteksjon avsluttet ***")
		stoppTrim = counter
		duration = stoppTrim - startTrim
		print("Trim videoen på tidspunk: ", startTrim)
		print("Slutt trimmingen på tidspunkt: ", stoppTrim)
		#^ Har nå parametre vi kan sende inn i os.system()-trim kommandoen --> (feedes startpunkt og varighet)
		print("Varighet: ", duration)
	
	


class ThreadingExample(object):
	""" Threading example class: The run() method will be started and it will run in the background until the application exits.	"""
	def __init__(self, interval=1):
		""" Constructor | :type interval: int  | :param interval: Check interval, in seconds"""
		self.interval = interval
		thread = threading.Thread(target=self.run, args=())
		thread.daemon = True		# Daemonize thread
		thread.start()			# Start the execution

	def run(self):
		""" Method that runs forever """
		while True:
			global counter
			if counter < 15:
				counter += 1
			else:
				counter = 0
			print(counter)
			time.sleep(self.interval)



#Kjører en gang, sjekker en configfil og setter innstillingene
=======
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
        print()
        print("Filming...")
        print("Filming...")
        print("Filming...")
        #os.system("date")
              
        time.sleep(6)
        


    #TODO: Continiously camera-algorithm after the configuration.
        #Start filming, each frame goes through ...
    
>>>>>>> Stashed changes
#Does this once at start and once a change has been detected
def ReadSettingsAndSet():
    print("Reading configfile...")

<<<<<<< Updated upstream
#'with' makes sure to close the resource after # Note it ads a \n for each line(?)
	with open("config.txt", "r") as file: 
		lines = file.readlines()
		#file.close()
	
	resolutionX = lines[0].strip()  #Reso X
	resolutionY = lines[1].strip()  #Reso Y
	formatV = lines[2].strip()	#YUY2, GREY8
	formatX = lines[3].strip()	#x-raw, bayern
        #TODO: faktisk sette instillingene på kameraet.
	
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
	#print(type(changedValue))
	print(changedValue)
	if changedValue == "1\n":
		print("Change deteced.")
		global changed
		changed = True
		#startTrim = "03"
		#stoppTrim = "01"
	#AlarmPhase()
	#global startTrim
	#print(startTrim)
	
	#os.system("ffmpeg -i test.mp4 -ss 00:00:"+ startTrim + " -t 00:00:" + stoppTrim + " -async 1 -strict -2 test3.mp4")

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

=======
#'with' makes sure to close the resource after
    with open("config.txt", "r") as file: 
        lines = file.readlines()
        #file.close()
    
    resolutionX = lines[0].strip()  #Reso X
    resolutionY = lines[1].strip()  #Reso Y
    formatV = lines[2].strip()      #YUY2, GREY8
    formatX = lines[3].strip()      #x-raw, bayern

    time.sleep(0.1)
    print()
    print()
    print()
    print()
    print()
    print()
    print("******** Settings ********")
    print()
    print("Resolution:",resolutionX,"x",resolutionY + ".")
    print("Format: " + formatV + ", " + formatX + ".")
    print()
    print("**************************")
    print()
    print()
    print()
    print()
    print()
    
    
    
#At the start of each "loop" check if there is a new configuration change    
def CheckConfiguration():
    print()
    print("Checking changed.txt")
    with open("changed.txt", "r") as check:
        changedValue = check.readline()

    print("Read value: " + changedValue)
    if changedValue == "1":
        print("Change deteced.")
        global changed
        changed = True

        

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
    
          
>>>>>>> Stashed changes

	

#       #       #       #       #       #       #       #
#                       Start of program                #
#	#       #       #       #       #       #       #

print("Starting up Hessdalen_2.0 ...")

#FrameOption = input('Enter framerate (7.5 / 15): ')

#print("Framerate set to", FrameOption + ".")

<<<<<<< Updated upstream
print("")
=======
#print()
#FormatOption = input('Enter format (GREY8 / YUY2): ')
#print()
#print("Format set to",FormatOption + ".")
print()
>>>>>>> Stashed changes

#Calls the "main"
StartProgram()
