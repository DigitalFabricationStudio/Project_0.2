# Valtteri Wikström

Personal project developed during the Digital Fabrication Studio course, 0.2 edition

## PROPOSAL 01 : Connector X (Working title)
### Background:
I have realised that prototyping projects often consist of different components on the hardware side, which makes it difficult to keep the prototype tidy and functional without always having to build a custom case to encompass all these components. A project I work on can consist for example of an Arduino, breadboard or pcb with electronic components, a physical interface, a raspberry pi, an Android phone, or at least some of the above. Having an easy way to physically combine these components would be neat-o.

### Description
Connector X is a opendesign connector for prototyping projects with different components. It's meant for physically stacking together different components of a prototype project. I'm not including a usb connector in my preliminary plans, to keep it versatile and modifiable, but implementing a power connector could be a future direction.

### Details
I have yet to make concrete plans about the details of the connector. I plan to produce a set of connector X components to demonstrate its use in a project. Depending on my Raspberry Pi arriving safely in time, I plan to follow either Path I or Path II.

Path I:
-Raspberry Pi case
-(Empty) photoframe with room for embedded camera and distance sensor, including simple pcb design (See proposal 2)

Path II:
-Arduino Mega ADB case
-(Empty) photoframe with Android phone holder and embedded distance sensor


## PROPOSAL 02 Photoframe camera
### Description:
The photoframe camera consists of an empty photoframe, a camera and a distance sensor. It is used to take pictures looking through the photoframe, using it as a large viewfinder. The data from the distance sensor is used to crop the picture obtained from the camera. This cropped photo is then uploaded to a server and connected to a look-a-like, _digital_ photoframe showing the latest photo in real-time. (As you might have noticed, I wish to make this photoframe in any case, but if the connector X plan is too ambitious or if it turns out that a similar open source connector has already been made, I'm more than happy to just concentrate on this project).

### Details
Apart from the components mentioned in the description, we also need a way to process the distance sensor data and pictures. For this I plan to use a Raspberry Pi, but due to trouble with delivery I might not be able to receive my unit in time. If this is the case, I plan to use an Android phone and an Arduino to serve the same purpose.


## LICENSE
I'm using this license to start with, but plan to license connector X allowing commercial use in the end.

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US">Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License</a>.