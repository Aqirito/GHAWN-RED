## Prerequisites
- Raspberry pi with Raspberry pi OS installed. Recomended 32bit "NO DISPLAY".

# Installing or Upgrading to NODE-RED
1. $ sudo apt update
2. $ bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
3. $ sudo reboot
- for more information: https://nodered.org/docs/getting-started/raspberrypi

## NODE-RED basic commands
- node-red-start - this starts the Node-RED service and displays its log output.
- node-red-stop - this stops the Node-RED service.
- node-red-restart - this stops and restarts the Node-RED service.
- node-red-log - this displays the log output of the service.

## Make NODE-RED start on boot
1. $ sudo systemctl enable nodered.service

### To disable the service, run the command:
1. $ sudo systemctl disable nodered.service

## Open NODE-RED Editor
1. http://localhost:1880

### Open with Local Network:
1. http://{your_ip_address}:1880


# MQTT Broker
## Installing MQTT Mosquitto Broker
1. $ sudo apt update
2. $ sudo apt install -y mosquitto mosquitto-clients

## Unauthenticated access
1. $ sudo nano /etc/mosquitto/mosquitto.conf
2. add this line:
  ```
  listener 1883
  allow_anonymous true
  ```

## Make MQTT Mosquitto start on boot
1. $ sudo systemctl enable mosquitto.service

### To disable the service, run the command:
1. $ sudo systemctl disable mosquitto.service

## Testing Mosquittoopen in the first tab:
1. $ mosquitto_sub -h {your_ip_address} -d -t testTopic
on second tab:
1. $ mosquitto_pub -h {your_ip_address} -d -t testTopic -m "Hello world!"

for more information of commands: https://mosquitto.org/man/mosquitto-8.html


# Testing MQTT clients on NODE-RED

1. Open Browser with: http://{your_ip_address}:1880
2. Import the test_mqtt.json file to the editor
3. Edit the mqtt nodes server to your ip address save it and deploy.
4. go to debug tab and trigger the inject.
5. check if the message is received from the mqtt_out at the same topic if not check your mqtt configurations or the network.