# Valtteri Wikström

Description of the design and fabrication process

## Camera frame
### Project:
The camera frame is here to re-imagine how we think of a viewfinder. The active viewfinder defines the captured photo based on what you see through the frame! This photo can then be instantly displayed on an actual digital photoframe. Apart from a user interface concept, this project is a comment on tablet-photographers, augmented reality and teleportation. 

### Design
The design for the camera frame was dictated by the desire to imitate a regular photo frame. The classic *kymppikuva* photo-size (10x15cm) was a natural decision for the size of the viewfinder. Rounded edges were chosen because they seemed most user-friendly. The first acrylic prototype looked like this:
![Prototype frame](https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/valtteri.wikstrom/Project/frame-proto.jpg)

This initial model was used for testing the software running on the raspberry pi, and calibrating the cropping (which is still not perfect in the version provided in /frame-source).

As evident, the raspberry pi was initially placed on the outside of the frame, to not be a part of the users experience. (It was connected to the prototype with the *H-clip*, see end of page.) It turned out that this blocks the view from the viewfinder, so it was placed on the inside instead. Regardless, it is important to note that the raspberry pi is for this design an external part necessary for prototyping, but not imagined for what would be a final product, that's why it has a clear case.

![Finished frame](https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/valtteri.wikstrom/Project/frame-finished2.jpg)

A 3-layer acrylic sandwich was decided for the final design, because this allowed for the middle layer to be a sort of container for components with the outer layers protecting them. There was a need for grooves in different places because of not all the components fitting to the 3mm footprint of the acrylic sheet. The first layer holds the hole for the camera objective and a groove for the shutter button and its cable, and a small groove for the camera cable. The second layer has a hole for the camera component, the infrared distance sensor base, the button base and a hole for the button cable coming through the groove in the first layer. The final layer has a hole for the infrared distance sensor and its connector, which is used also for the button cable, the camera usb cable has its own hole.

![Frame in use](https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/valtteri.wikstrom/Project/frame-finished.jpg)


### Technical 
#### Components
* Raspberry pi
* Webcam removed from an old laptop computer (Here using a Ricoh R5U870 0x810 model from HP Pavilion dv6000 series). When the Raspberry Pi camera module is released that will be used instead for better resolution.
* Infrared distance sensor (Sharp GP2xxx) and Analog to digital converter (MCP3008)
* Wifi module (Realtek)

An infrared distance sensor is used to measure how far the user is from the frame when taking a picture. A recycled laptop webcam is used for the camera component and a Raspberry pi is used for interfacing with these devices and processing the photo to the final format. Finally a processing application running on another computer accesses the raspberry pi through sftp to retrieve the photo and show it on its screen, or a digital photoframe of the same dimensions as the camera frame.

#### Raspberry pi Analog shield
I wanted to place the MCP3008 firmly inside the raspberry pi case. For this I designed a pcb in eagle that fits with a connector to the GPIO pins and can be removed. It has connections for soldering a wire to each analog input and holes for 3 ground and 3 +3.3V connections. Additionally it breaks out one of the GPIO pins to be used for the shutter button. This pcb was milled with the Roland Modela MDX-20. 

![Analog shield](https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/valtteri.wikstrom/Project/analog-shield.jpg)

#### Software
See the frame-source folder for the source code and installation instructions.


## LICENSE
The Camera frame is provided with the following creative commons license:

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US">Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License</a>.


## H-Clip
### Project:
This is the universal connector for prototyping projects! What are you waiting for, just add the connector to your case and project and have interchangeable parts between projects!
 
### Standard
The current connector is made for a 3mm laser cut material. The hole is 8x3mm and the connector snaps into this hole. I've used 20mm as the interval between connectors in y direction and 38 mm in x-direction, which work well having a 3x2 grid of connectors on the raspberry pi case, but something else might be suitable for other projects.

### Inspiration
After thinking about this and discussing with smart people, I decided to try to imitate a plastic buckle found in backpacks to some extent. Only difference would be to make it *pullable*, so that access to the inside of the case wouldn't be necessary.
![backpack buckle](https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/valtteri.wikstrom/Project/buckle.jpg)

### Process
I started off by making a simple connector with 2 mm thick legs and 2 mm thick body, without any extra easing and a 1 mm clipping edge. This didn't work and the connector was too stiff and fragile. I did find out that kerfing wasn't really necessary for the connector, it fits quite snug.

Many iterations went by, with some progress, but the connector was still breaking too often when inserting and removing. The final model had to be elongated and rounded, so that it still fit to the 3mm acrylic. Lo-behold:
![Stages of connector](https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/valtteri.wikstrom/Project/evolving_connector.png)

Here is a picture of the final model:
![The connector](https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/valtteri.wikstrom/Project/connector_final.jpg)




##Settings
All acrylic was cut with the laser cutter and the following settings:
>> Resolution: 1200 dpi
>> Speed: 20% (for coloured acrylic) and 22% (for clear acrylic)
>> Power: 100%
>> Freq: 500 Hz
For chord-paths and other functional engraving:
>> Speed: 35%
>> Power: 100%
For regular engraving:
>> Speed: 50%
>> Power 100%


## LICENSE
The H-clip is provided with the following creative commons license:

<a rel="license" href="http://creativecommons.org/licenses/by/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/3.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/3.0/deed.en_US">Creative Commons Attribution 3.0 Unported License</a>.