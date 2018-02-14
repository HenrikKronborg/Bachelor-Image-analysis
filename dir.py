#!/urs/bin/python
import os
from datetime import datetime
#from time import gmtime, strftime

deteksjonArray = []



##Gjør noe i oppstarten èn gang
#TODO: def(?) innstillinger, startparametere(?)

#TODO: def
##Egen prosess/tråd som konstant filmer i intervaller, lagrer nye mapper for frames osv(?)
#TODO: Start tråd som kjører independent, kanskje bare på kveldstid(?)
## obs, filstier *kan* variere
##Lag mappe for neste intervall
i = datetime.now()
#_ TODO: Legge til disse i en kø? First in, first out? Array? Noe som holder styr på neste video som kan analyseres ( husk X mappe må være klar->ha alle frames lagd/filmet ferdig)
CurrentVideo = str(i.strftime('%Y_%m_%d_%H:%M:%S'))
os.system("mkdir /home/nvidia/Bachelor/Frames/" + CurrentVideo) #<- Navnet blir brukt i Henrik-funk
#TODO: Film



##Hvis det er to video-intervaller i Videoer-mappen; start analyse på første//Kan byttes ut med noe annet så lenge vi ikke begynner før et helt intervall er ferdig.
if len(os.listdir('/home/nvidia/Bachelor/Videoer')) > 1:
	#todo: for			
		#if end=".mp4"

'''
for video in os.listdir('/home/bachelor/Git/Bachelor/raw'):
	if video.endswith('.mp4'):
		global deteksjonArray
		#//send "video" inn i algoritmen
		#analyseAlgo(video)
		#//Inne i analyseAlgo blir AlarmPhase() kalt --> lagrer alle detek.objekter i deteksjonArray
		os.system("ffmpeg -i /home/bachelor/Git/Bachelor/raw/"+ video + " -ss 00:00:04 -t 00:00:01 -async 1 -strict -2 /home/bachelor/Git/Bachelor/trims/[T]" +  video)
   #^Filnavnet blir allerede lagret som datoen/orginalfil(?)
		

	#//Gå igjennom alle lagrede deteksjoner for denne videoen og lag trims 
	for deteksjon in deteksjonArray:
		
		#os.system("ffmpeg -i " + str(deteksjon.name) + " -ss 00:00:" + str(deteksjon.start) + " -t 00:00:" + str(deteksjon.duration) + " -async 1 strict -2 [Trimmed]" + deteksjon.name + ".mp4")

	#Når analysen er ferdig lager vi 
	#print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
	#print(gmtime())
	

print("Ferdig")
'''