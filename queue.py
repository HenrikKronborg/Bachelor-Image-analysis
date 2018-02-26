#!/urs/bin/python
import numpy as np
import cv2




cv2.VideoCapture("test.mp4")


'''
#os.system("rm -rv /home/nvidia/Bachelor/Videoer/"+testFolder) # Benytt -rf til slutt
#os.system("rm -v /home/nvidia/Bachelor/Trims/*")
#orgVideo = "slettmeg.mp4"
#os.system("rm -rv /home/nvidia/Bachelor/Videoer/"+orgVideo) # Benytt -rf til slutt
#os.system("rm -v /home/nvidia/Bachelor/Trims/*")
#os.system("rm -rv /home/nvidia/Bachelor/Frames/"+orgVideo)

i = datetime.now()
CurrentVideo = str(i.strftime('%Y_%m_%d_%H:%M:%S:%f'))
curr = CurrentVideo + ".mp4"
#Kutter ned timestamp til hrs:min:sek:milli
#print("FrameName:", curr)
#frameName = curr[11:]
#curr = frameName[:15]
#print("hei: "+curr)
videoName = "2018_02_21_09:42:30.mp4"
print(videoName)
videoNameNoDate = videoName[11:]
print("NoDate: "+videoNameNoDate)
videoNameNoMP = videoNameNoDate[:8]
print("NoMP4: "+videoNameNoMP)
time,min,sek = videoNameNoMP.split(':')
print(time)
print(min)
print(sek)
#frameName2 = frameName1[:15]
#print(frameName2)

#Splitter tiden opp i fire variabler (hrs,min,sec, milli)   Trenger ikke millisekunder i tidsberegning, kun i frame-navn(unik)
time,min,sek, milli = frameName.split(':')
print(time)
print(min)
print(sek)
print(milli)

stime = int(time)*60*60
print(stime)
smin = int(stime)+(int(min)*60)
print(smin)
ssek = smin + int(sek)
#Setter "orginaltid"
startTid = ssek
print("Orgvideo tidsstempel:",ssek)

ssek +=1
print("Neste frame1",ssek)
ssek +=1
print("Neste frame2",ssek)
ssek +=1
print("Neste frame3",ssek)
#Denne frames tid - orginaltid
ssek -= startTid

print("Duration siden første frame: ",ssek)




flyt = 12.3245
print(str(flyt))

'''


#clip = VideoFileClip("test.mp4").cutout(0, 1)
#clip.write_videofile("testet.mp4")
#os.system("ffmpeg -loglevel quiet -i test.mp4 -ss 00:00:1 -t 00:00:2 -async 1 -strict -2 trimmet.mp4")
#https://community.linuxmint.com/software/view/gstreamer0.10-gnonlin
#
#frameCount=0

#while(True):

#frameCount += 1
#capture.read(frame) 
#if(frameCount>=start_frame_count&&frameCount<stop_frame_count):
#VideoWriter.write(frame)
#	else if(frameCount == stop_frame_count)
#    break;




'''
sudo add-apt-repository ppa:ozmartian/apps
sudo apt update
sudo apt install vidcutter
'''
			'''videoNameNoDate = videoName[11:]
			print("NoDate: "+videoNameNoDate)
			videoNameNoMP = videoNameNoDate[:8]
			print("NoMP4: "+videoNameNoMP)
			time,min,sek = videoNameNoMP.split(':')
			print(time)
			print(min)
			print(sek)
			#print(milli)
			
			hoursInSec = int(time)*60*60
			print(hoursInSec)
			minInSec = int(hoursInSec)+(int(min)*60)
			print(minInSec)
			ssek = minInSec + int(sek)
			#Setter "orginaltid"'''


""""
			videoName = "test15.mp4"
			trimmedVideo = "[TRIMMED]"+videoName
			#Videoen som tak tas i heter ikke altid "test15.mp4"
			#-loglevel quiet fjerner ALL output fra ffmpeg
			########Ikke behandle det her; vent til alle detekteringssteder fra array er med. 1x60s loop
			os.system("ffmpeg -loglevel quiet -i " + videoName + " -ss 00:00:" + str(startTrim) + " -t 00:00:" + str(duration) + " -async 1 -strict -2 " + trimmedVideo)
			#Lage objekter som har dette som properties, lagre objektene i en array(?), foreach/in
			"""



