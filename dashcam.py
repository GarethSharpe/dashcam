import os
import calendar
import datetime

import dashcam_utilities as util

if not os.path.exists("/home/pi/dashcam/Video"):
	os.makedirs("/home/pi/dashcam/Video")

if not os.path.exists("/home/pi/dashcam/Video/January"):
	util.make_dirs("/home/pi/dashcam/Video")

size = util.get_dir_size("/home/pi/dashcam/Video")

if size >= 7.5:
	util.rm_dirs("/home/pi/dashcam/Video")
	util.make_dirs("/home/pi/dashcam/Video")

camera = util.get_camera()
now = datetime.datetime.now()
month = calendar.month_name[now.month]
path = os.path.join("/home/pi/dashcam/Video", month, now.strftime('%Y-%m-%d %H:%M:%S')) + util.ext
camera.start_recording(path)
# camera.start_preview()

try:
	while True:
		now = datetime.datetime.now()
		camera.annotate_text = now.strftime('%Y-%m-%d %H:%M:%S')
		camera.wait_recording(0.2)
finally:
	camera.stop_recording()
	# camera.stop_preview()
