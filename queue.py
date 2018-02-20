#!/urs/bin/python
import os
from datetime import datetime


#os.system("rm -rv /home/nvidia/Bachelor/Videoer/"+testFolder) # Benytt -rf til slutt
#os.system("rm -v /home/nvidia/Bachelor/Trims/*")
#orgVideo = "slettmeg.mp4"
#os.system("rm -rv /home/nvidia/Bachelor/Videoer/"+orgVideo) # Benytt -rf til slutt
#os.system("rm -v /home/nvidia/Bachelor/Trims/*")
#os.system("rm -rv /home/nvidia/Bachelor/Frames/"+orgVideo)

i = datetime.now()
CurrentVideo = str(i.strftime('%Y_%m_%d_%H:%M:%S:%f'))

#Kutter ned timestamp til hrs:min:sek:milli
print("FrameName:",CurrentVideo)
frameName = CurrentVideo[11:]
print(frameName)
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






























