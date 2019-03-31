#!/usr/bin/env python3

import os
'''
import sys
import gi
gi.require_version("Tcam", "0.1")
gi.require_version("Gst", "1.0")

from gi.repository import Tcam, Gst
'''

if __name__ == "__main__":
	os.system("rm -r Videos/*")
	os.system("rm -r Detections/Pictures/*")
	os.system("rm -r Detections/Trims/*")
	'''
	Gst.init(sys.argv)
	pipeline = Gst.Pipeline.new()
	pipeline.set_state(Gst.State.NULL)
	'''
