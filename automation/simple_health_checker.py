import shutil
import psutil

du = shutil.disk_usage("/")

def check_disk_usage(disk):
	du = shutil.disk_usage(disk)
	free = du.free / du.total * 100
	return free > 20

def check_cpu_usage():
	usage = psutil.cpu_percent(1)
	return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
	print("ERROR!")
	print("CPU usage: " + str(psutil.cpu_percent(1)))
	print("Free physical memory left: "+ str(du.free / du.total * 100) +"%")
else:
	print("Everything is OK!")
	print("CPU usage: " + str(psutil.cpu_percent(1)))
	print("Free physical memory left: "+ str(du.free / du.total * 100) +"%")