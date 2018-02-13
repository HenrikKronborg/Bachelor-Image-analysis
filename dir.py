#!/urs/bin/python
import os
import datetime
from time import gmtime, strftime
deteksjonArray = []


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
