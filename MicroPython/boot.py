# boot.py -- run on boot-up

# Complete project details at https://RandomNerdTutorials.com
import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)       # turn off vendor O/S debugging messages
esp.osdebug(0)
import gc
gc.collect()

PC_switch = machine.Pin(4, machine.Pin.OUT)
PC_switch.value(1)

ssid = 'Your Wi-Fi name'
password = 'Your Password'
mqtt_server = 'your MQTT server IP address'
#EXAMPLE IP ADDRESS
#mqtt_server = '192.168.0.122'
client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = 'post_request'
topic_pub = 'get_request'

last_message = 0
message_interval = 5
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
