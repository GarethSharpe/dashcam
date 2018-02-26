# @file:			dashcam.py
# @author: 			Gareth Sharpe
# @created:			2/21/2018
# @modified:		2/25/2018
# @description: 	A dashcam application to store footage.	

# imports #
import os
import calendar
import datetime
import dashcam_utilities as util

# verify Video directory exists, otherwise create it
if not os.path.exists("/home/pi/dashcam/Video"):
	os.makedirs("/home/pi/dashcam/Video")

# verify Video subdirectories exist, otherwise create them
if not os.path.exists("/home/pi/dashcam/Video/January"):
	util.make_dirs("/home/pi/dashcam/Video")

# get the size of all files in subdirectories of the Video directory
size = util.get_dir_size("/home/pi/dashcam/Video")

# if the file system size exceeds threashold of 7.5GB, delete
# the files and recreate their parent folders
if size >= 7.5:
	util.rm_dirs("Video")
	util.make_dirs("Video")

camera = util.get_camera()											# get the camera object
now = datetime.datetime.now()										# get the current date
month = calendar.month_name[now.month]								# get the current month

# create a path to the desired file and timestamp the filename 
path = os.path.join("/home/pi/dashcam/Video", month, now.strftime('%Y-%m-%d %H:%M:%S')) + util.ext

# start recording video to the specified path
camera.start_recording(path)
# camera.start_preview()

try:
	# loop forever
	while True:		
		now = datetime.datetime.now()								# get the current date
		camera.annotate_text = now.strftime('%Y-%m-%d %H:%M:%S')	# annotate the video with the current date
		camera.wait_recording(0.2)									# annotate the video every 0.2 seconds
finally:
	camera.stop_recording()											# stop recording on error								
	# camera.stop_preview()
