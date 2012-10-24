# Matti Niinimäki
# Chameleon Lamp

Personal project developed during the Digital Fabrication Studio course, 0.2 edition

<img alt="lamp proto" src="https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/matti.niinimaki/finalproject/images/lamp001.jpg" />
<img alt="lamp proto" src="https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/matti.niinimaki/finalproject/images/lamp002.jpg" />

Chameleon Lamp is a lamp that changes its color based on the color of the surface it's placed on. A color sensor on the bottom of the lamp detects the color of the surface and controls RGB LED lights inside the lamp.

## Materials

### Base of the lamp

The base of the lamp is made with laser cut 4 mm plywood with all the electronics embedded inside the base in a sandwich design. No screws are needed for assembling the base or for attaching the electronics. Each layer of the sandwich is cut so that the electronics click into place.

Designing some sort of stands for the parts would have taken less material and might have been easier, but the design I chose also adds some weight to the base, which makes the lamp more stable when using a larger diffuser.

<img alt="laser cutting" src="https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/matti.niinimaki/finalproject/images/lamp_base.png-01.jpg" />
<img alt="laser cutting" src="https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/matti.niinimaki/finalproject/images/proto003.jpg" />


The rounded corners were made with the help of this <a href="http://www.thingiverse.com/thing:17240">Parametric Flexbox.</a>

<ul>
	<li>Laser cut 4 mm plywood</li>
</ul>

Settings for the laser cutter:
<ul>
<li>cutting: 8/65/500</li>
<li>engraving: 60/90</li>
</ul>

Finishing:

<img alt="osmo" src="https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/matti.niinimaki/finalproject/images/finishing001.jpg" />
<img alt="osmo" src="https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/matti.niinimaki/finalproject/images/finishing002.jpg" />


#### The Lamp Diffuser

I decided to make the diffuser out of silicone since there was no diffused acrylic available

<img alt="bulb" src="https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/matti.niinimaki/finalproject/images/bulb001.jpg" />
<img alt="bulb" src="https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/matti.niinimaki/finalproject/images/bulb002.jpg" />
<img alt="bulb" src="https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/matti.niinimaki/finalproject/images/bulb003.jpg" />
<img alt="bulb" src="https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/matti.niinimaki/finalproject/images/bulb004.jpg" />
<img alt="bulb" src="https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/matti.niinimaki/finalproject/images/bulb005.jpg" />

I also tried to 3d print it, but the Ultimaker was having a bad day, so I only got part of it printed.

<img alt="lamp proto" src="https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/matti.niinimaki/finalproject/images/diffuser_3dprint.jpg" />
<ul>
	<li>The diffuser can be changed. I made a couple of different ones.</li>
	<li>One was made with silicone</li>
	<li>The other was 3d printed with translucent PLA plastic</li>
</ul>

#### Electronics
<img alt="electronics" src="https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/matti.niinimaki/finalproject/images/proto001.jpg" />

The sensor is connected to the Arduino Pro Mini, which scales the RGB input values and controls the MaxM RGB LED. The BlinkM MaxM also supports straight input from sensors, but the scaling was much easier when using the Arduino in between.

<ul>
	<li>BlinkM MaxM</li>
	<li>HDJD-S822 Color Sensor Breakout</li>
	<li>Arduino Pro Mini 5V</li>
</ul>


## LICENSE
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US">Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License</a>.

The Månsteri logo is a trademark of <a href="http://mansteri.com/">Månsteri </a>