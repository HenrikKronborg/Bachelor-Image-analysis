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

<<<<<<< HEAD:Hessdalen_2.0.py
<<<<<<< Updated upstream
filmIntervall = 0
currentTime = 0
=======
>>>>>>> master:Hess08.py
startTrim = 0
stopptrim = 0
duration = 0
counter = 0
detectionPhase = False
#_Holds objects storing different detections /w startTrim, stoppTrim and duration
detectionArray = []
detectionAmount = 1


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
#//For each video(intervall) som er lagret i mappen(raw video); Gå igjennom hver video, sjekk hver X'te frame.
#//Kjør på dagtid?
	while(running):
		#_Only at start(?)
		#CheckConfiguration()
		print("")
		#print("Filming...")			  
		time.sleep(1)
	
		#Simulert deteksjon som varer i 2 sek (trimmer fra 4 til 8 sekunder (+/- 1)-buffer))
		#1 og 0 vil evt komme ut(return) fra grupperings-algoritmen --> kommer en verdi fra hvert analyserte bilde
		#if detectionPhase == False:
						#AlarmPhase(grupperings-algoritme)
                        #
                        #AlarmPhase(algo)
                        
						#//Loop som går igjennom x frames pr 
						#Filmer kontinuerlig. AlarmPhase tar tak i X frames. Husk: trenger ikke sanntidssystem
						#Er ikke farlig med sanntid
		#_ Simulasjon av hva AlarmPhase får igjen i parameter fra bildealgoritmen
		if counter == 2:
			AlarmPhase(0)
			#for obj in detectionArray:
				#print(obj.name)
				
		if counter == 3:
			#AlarmStart()?
			AlarmPhase(1)
		if counter == 4:
			AlarmPhase(1)	
		if counter == 5:
			AlarmPhase(0)
		if counter == 6:
			AlarmPhase(0)
		if counter == 7:
			AlarmPhase(0)
			
		if counter == 9:
			AlarmPhase(1)
		if counter == 10:
			AlarmPhase(1)
		if counter == 11:
			AlarmPhase(0)
		if counter == 12:
			AlarmPhase(0)
		if counter == 15:	
			for obj in detectionArray:
				print(obj.name, " - Start:", obj.start, ", Stopp:", obj.stopp, ", Duration:", obj.duration)
				#lage trim async
				#https://www.ffmpeg.org/ffmpeg.html#Description ffmpeg options -> 5.4 Main options
				os.system("ffmpeg -i test.mp4 -ss 00:00:" + str(obj.start) + " -t 00:00:" + str(obj.duration) + " -async 1 -strict -2 [Trimmed]" + obj.name+".mp4")
				#os.system("ffmpeg -i test.mp4 -ss 00:00:" + str(obj.start) + " -t 00:00:" + str(obj.duration) + " -vf drawtext=fontfile=/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf: \text='%{localtime\:%T}': fontcolor=white@0.8: x=7: y=700 -async 1 -strict -2 [Trimmed]" + obj.name+".mp4")

			running=False
            #Om counter når 60: stopp å filme(?), lagre video, trim og send til server, start å filme ny sekvens.//<-Ikke sanntid
			#evt: film i 1 time, lagre alle steder som skal trimmes.
			#TODO: [Hvor lange intervaller?]-> sec/min/time -> må pushe inn i "hr:min:sec"
			#TODO: Filnavnet bør ha dagen dato, kommer fra når vi lagrer videoen. Benytte kø for å behandle videoer som skal behandles?
			#Si vi lagrer 30-minutters filmer gjennom nattens løp: det vil ikke nødvendigvis være mange av disse som inneholder deteksjon
			
	#TODO: Continiously camera-algorithm after the configuration.
	#Start filming, each frame goes through ...
	
                #TODO if counter == 60: trim
		  
def AlarmPhase(isDetect):
	#Variabler som holder styr på tiden
	#ta inn filmetid (0-60s), 
	#variabel som sjekker om det fortsatt er alarmstatus /bool
		#isDetect er enten 0 eller 1 --> kommer fra grupperings-algo
		#Så lenge isDetect er sann 
	global stoppTrim
	global startTrim
	global duration
	global detectionPhase
	global detectionArray
	global detectionAmount
	

	if isDetect == 1:
		if detectionPhase == False:
			print(" >[] Detection []<")
			startTrim = counter-1
			detectionPhase = True
		
			
		elif detectionPhase == True:
			print("Currently in detectionPhase, not storing a new startTrim")
			
		
	else:
		if detectionPhase == False:
			print("No detection")

		elif detectionPhase == True:
			print(" >[X] Deteksjon avsluttet [X]< ")
			detectionPhase = False
			stoppTrim = counter+1
			duration = stoppTrim - startTrim
			#Få tak i frame name evt?
			trimName = "Detect_"+str(detectionAmount)
			#dette tallet må resetes ved nytt "intervall"
			detectionAmount += 1
			print("Trim videoen på tidspunk: ", startTrim, " (",startTrim+1,")")
			print("Slutt trimmingen på tidspunkt: ", stoppTrim," (",stoppTrim-1,")")
			print("Varighet: ", duration)
			
			
			
			detectionArray.append(VideoObject(trimName, startTrim, stoppTrim, duration))
			print(detectionArray[(detectionAmount-2)].name, "Added.")
			
			""""
			videoName = "test15.mp4"
			trimmedVideo = "[TRIMMED]"+videoName
			#Videoen som tak tas i heter ikke altid "test15.mp4"
			#-loglevel quiet fjerner ALL output fra ffmpeg
			########Ikke behandle det her; vent til alle detekteringssteder fra array er med. 1x60s loop
			os.system("ffmpeg -loglevel quiet -i " + videoName + " -ss 00:00:" + str(startTrim) + " -t 00:00:" + str(duration) + " -async 1 -strict -2 " + trimmedVideo)
			#Lage objekter som har dette som properties, lagre objektene i en array(?), foreach/in
			"""
 
class VideoObject(object):
		start = 0
		stopp = 0
		duration = 0
		def __init__(self, name, startT, stoppT, dura):
			self.name = name
			self.start = startT
			self.stopp = stoppT
			self.duration = dura
			
			
			
class ThreadingExample(object):
	""" Threading example class: The run() method will be started and it will run in the background until the application exits.	"""
	def __init__(self, interval=1):
		""" Constructor | :type interval: int  | :param interval: Check interval, in seconds"""
		self.interval = interval
		thread = threading.Thread(target=self.run, args=())
		thread.daemon = True		# Daemonize thread
		thread.start()				# Start the execution

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

	#Stores the read settings in variables
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


'''
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
<<<<<<< HEAD:Hessdalen_2.0.py

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
=======
'''
>>>>>>> master:Hess08.py

	

#       #       #       #       #       #       #       #
#                     Start of program                  #
#		#       #       #       #       #       #       #

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