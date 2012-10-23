# Matti Niinimäki
# Chameleon Lamp

Personal project developed during the Digital Fabrication Studio course, 0.2 edition

<img alt="lamp proto" src="https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/matti.niinimaki/finalproject/images/proto005.jpg" />

Chameleon Lamp is a lamp that changes its color based on the color of the surface it's placed on. A color sensor on the bottom of the lamp detects the color of the surface and controls RGB LED lights inside the lamp.

### Materials

#### Base of the lamp

The base of the lamp is made with laser cut 4 mm plywood with all the electronics embedded inside the base in a sandwich design. No screws are needed for assembling the base or for attaching the electronics. Each layer of the sandwich is cut so that the electronics click into place.

Designing some sort of stands for the parts would have taken less material and might have been easier, but the design I chose also adds some weight to the base, which makes the lamp more stable when using a larger diffuser.

The rounded corners were made with the help of this <a href="http://www.thingiverse.com/thing:17240">Parametric Flexbox.</a>

<ul>
	<li>Laser cut 4 mm plywood</li>
	<li>Surface finished with Osmo Color wood wax</li>
</ul>

#### The Lamp Diffuser
<ul>
	<li>The diffuser can be changed. I made a couple of different ones.</li>
	<li>Sorta-Clear Silicone</li>
	<li>3d printed PLA plastic</li>
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