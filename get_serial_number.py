# wmic bios get serialnumber#Windows
# hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid#Linux
# ioreg -l | grep IOPlatformSerialNumber#Mac OS X
import os, sys
def getMachine_addr():
	os_type = sys.platform.lower()
	
	if "linux" == os_type:
		command = "hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid"
	elif "darwin" == os_type:
		command = "ioreg -c IOPlatformExpertDevice -d 2 | awk -F\\\" '/IOPlatformSerialNumber/{print $(NF-1)}'"
	elif "win" in os_type:
		command = "wmic baseboard get serialnumber"
	
	return os.popen(command).read().replace("\n","").replace("	","").replace(" ","").replace("SerialNumber","")

#output machine serial code: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXX
