import os
import sys
import shutil
import picamera

ext = ".h264"

def get_dir_size(start_path='.'):
    total_size = 0
    bytes_in_gigabyte = 1024 * 1024.0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for file in filenames:
            fp = os.path.join(dirpath, file)
            total_size += os.path.getsize(fp)
    return total_size / bytes_in_gigabyte 

def rm_dirs(start_path='.'):
	for dirpath, dirnames, filenames in os.walk(start_path):
		shutil.rmtree(dirpath)

def make_dirs(start_path='.'):
	for i in range(1, 13):
		directory = os.path.join(start_path, calandar.month_name[i])
		if not os.path.exists(directory):
			os.makedirs(directory)

def get_camera():
	camera = picamera.PiCamera(resolution=(1280, 720), framerate=24)
	camera.annotate_background = picamera.Color('black')
	return camera