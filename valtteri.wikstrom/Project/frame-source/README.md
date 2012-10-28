# Valtteri Wikström

## Step-by-step installation instructions for the software and drivers
###for following components:
* Raspberry pi (model B 256MB)
* Ricoh R5U870 webcam (ID: 0x1810), but it should work for any webcam running on raspberry pi.
* MCP3008 ADC (for the distance sensors analog values)
* Mini WLAN adapter Realtek RTL8188CUS (but any raspberry pi compatible WLAN adapter is ok)
* Second computer (running Processing, ssh)

### Raspbian
This installation guide assumes a clean installation of the official Raspbian "wheezy" distribution. The exact version used in this case is the 2012-09-18 release.

### Installation
1. Network configuration
  * To begin with, the raspberry pi should be connected to a screen, keyboard and mouse.
  * Boot up for the first time, in raspi-config I recommend:
    1. expand\_rootfs
    2. memory split: 240
	3. ssh: Enable (**very important!**)
	4. Finish and reboot, login is pi/raspberry
  * `startx`
  * "Wifi Config" from desktop, configure your raspberry pi to the same network as your photo-receiving computer.
  * Note down raspberry pi's ip adress (in my case *192.168.0.13*, which will be used in the example)
  * In LXTerminal: `sudo shutdown -h now`
  * Remove keyboard, mouse, screen and make sure the webcam, WLAN adapter and MCP3008 shield (or the same connections realized in another way) are connected.
2. Software installation on raspberry pi
  * Repower raspberry pi
  * Take your second computer and connect via ssh to the raspberry pi (with os x: open Terminal and type `ssh pi@192.168.0.13`, where you substitute your raspberry pi's ip adress. After log-in it should look like this: `pi@raspberrypi ~ $`
  * start with updates (this may take a while): `sudo apt-get update` and `sudo apt-get upgrade`.
  * check that your devices are connected by running `lsusb`, my output includes:
  	`Bus 001 Device 004: ID 0bda:8176 Realtek Semiconductor Corp. RTL8188CUS 802.11n WLAN Adapter`
	`Bus 001 Device 005: ID 05ca:1810 Ricoh Co., Ltd Pavilion Webcam [R5U870]`
  * check that you have a videoX device by `cd /dev` and `ls`, look for the `video0` device in the list. Look in the next part of the instructions if you are using Ricoh R5U870.
  * `cd /home/pi`
  * `mkdir webcam`
  * `cd webcam`
  * Download source code for camera frame: `wget https://github.com/DigitalFabricationStudio/Project_0.2/raw/master/valtteri.wikstrom/Project/frame-source/camframe.py`
  * You might need to edit the source code, if your webcam uses a different resolution than 352x288 and if you are using different GPIO pins for the MCP3008.
  * Install opencv: `sudo apt-get install python-opencv`
3. Software installation on client computer that shows the imges
  * You need [Processing](http://www.processing.org) installed.
  * Install the [SFTP library](http://www.shiffman.net/2007/06/04/sftp-with-java-processing/) for Processing.
  * Download [source code](https://github.com/DigitalFabricationStudio/Project_0.2/raw/master/valtteri.wikstrom/Project/frame-source/camframe.py).
  * You should edit the ip adress in the code.
  * Run the pde-sketch!
  
####Notes:
  * Photos are not saved at the moment, just the newest one is shown. Expect an update soon.
  
#### Additional: compiling drivers for R5U870 camera
*note: My camera was originally with ID: 0x1870, I had to run a firmware update from HP on a windows machine that changed the ID to 0x1810, which works with the drivers used in these instructions.*
* You need to install these drivers if you are using a Ricoh R5U870 webcam component and there is no videoX device in /dev
  1. install dependencies: `sudo apt-get install libglib2.0-dev libusb-dev build-essential gcc automake mercurial`
  2. Download drivers: `wget https://bitbucket.org/ahixon/r5u87x/get/default.tar.gz`
  3. Unpack: `tar -zxvf default.tar.gz` and rename folder to something more appropriate: `mv ahixon-r5u87x-a9b2171d762b/ r5u87x/`
  4. `cd r5u87x`
  5. `make`
  6. `sudo make install`
  7. Run: `sudo r5u87x-loader --reload`, If you get a successfully uploaded -message, run `sudo reboot` and reconnect to your raspberry pi. Your camera should now work and there should now be a `video0` device in `/dev`. The r5u87x-loader will now run automatically on boot, so you don't need to do any of these steps again.
  8. I haven't had success with taking any pictures with the R5U870 of higher resolution than 352x288. I would love to hear if someone gets undistorted pictures with full resolution.
  
