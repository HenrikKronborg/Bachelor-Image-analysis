#!/urs/bin/python

import os
from datetime import datetime

i = datetime.now()


CurrentVideo = str(i.strftime('%Y_%m_%d_%H:%M:%S'))
os.system("mkdir /home/nvidia/Bachelor/Frames/" + CurrentVideo)

