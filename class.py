#!/urs/bin/python

class VideoObject(object):
		start = 0
		slutt = 0
		def __init__(self, name, Sta,Sto):
			self.name = name
			self.start = Sta
			self.slutt = Sto
			

objectArray = []
			
			
vid1 = VideoObject("v1",2,6)
print(vid1.name, "-", vid1.start, "_",vid1.slutt)
objectArray.append(vid1)
vid2 = VideoObject("v2", 11,25)
print(vid2.name, "-", vid2.start, "_",vid2.slutt)
objectArray.append(vid2)

for obj in objectArray:
	print(obj.name, "yas")

	
print(objectArray[0].name)
print("ola "+str(2))
tall = 1
print(tall)
tall += 1
print(tall)
tall += 1
print(tall)
bokstav = "hei"+"[Trimmed]"
print(bokstav)