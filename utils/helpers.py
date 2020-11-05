import os
import requests
import sys
import json


def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError:
        return False
    return True

def load_activate_code():
    if os.path.exists('activate_key'):
        f = open('activate_key')
        return f.read()
    return None

def getMachine_addr():
	os_type = sys.platform.lower()
	
	if "linux" == os_type:
		command = "hal-get-property --udi /org/freedesktop/Hal/devices/computer --key system.hardware.uuid"
	elif "darwin" == os_type:
		command = "ioreg -c IOPlatformExpertDevice -d 2 | awk -F\\\" '/IOPlatformSerialNumber/{print $(NF-1)}'"
	elif "win" in os_type:
		command = "wmic baseboard get serialnumber"
	
	return os.popen(command).read().replace("\n","").replace("	","").replace(" ","").replace("SerialNumber","")


def is_activate(activate_code, serial_code):
    if serial_code == None:
        return False
    else:
        response = requests.post('https://dev.kevins.fun/v1.0/activate/verify-code', json={'activate_code': activate_code, 'serial_code': serial_code})
        if response.json()['returnCode'] == '000000':
            return True
        if response.json()['returnCode'] == '000001':
            with open('activate_key', 'w') as f:
                f.write(response.json()['info']['activate_code'])
            return True



