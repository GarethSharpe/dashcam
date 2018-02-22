import os
import calendar
import datetime

import dashcam_utilities as util

if not os.path.exists("Video"):
	os.makedirs("Video")

if not os.path.exists("Video/January"):
	util.make_dirs("Video")

size = get_dir_size("Video")

if size >= 10:
	util.rm_dirs("Video")
	util.make_dirs("Video")

camera = get_camera()
now = datetime.datetime.now()
month = calendar.month_name[now.month]
path = os.join(month, now) + util.ext
camera.start_recording(path)

try:
	while true:
		now = datetime.datetime.now()
		camera.annotate_text = now.strftime('%Y-%m-%d %H:%M:%S')
		camera.wait_recording(0.2)
finally:
	camera.stop_recording()
