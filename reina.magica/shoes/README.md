# Reina Magica
# Shoe project

I aim to make a custom pair of moulded shoes made out of plastic, inspired by these cool shoes I saw designed by United Nude.

![unitednude](http://uk.dutchdesigninchina.com/wp-content/uploads/United-Nude-2-240x240.jpg)

The idea is that the shoes would be comfortable, because it is made to fit the soles of my feet smoothly.  Especially important that it is comfortable is because high heels usually are the most uncomfortable things in the world besides wedgies.  My aim is to make a nice looking and hopefully ergonomically good shoes that will also look nice.

I started by looking for ways to scan my feet into 3d.  I tried using pictures and 123d catch but the result was not good as I could not keep my feet still in that position, it was a real mess.

I heard a fellow student used kinect to scan his face, so I downloaded the same program OSX connect from (http://www.thingiverse.com/thing:8262)

![kinect](https://github.com/DigitalFabricationStudio/Project_0.2/blob/master/reina.magica/shoes/screenshotkinect.png)

I set the kinect on the table, and because the distance was too close, I sat on the next table.  Then I bought the laptop to where I was sitting and arranged myself and the depth settings on the program so I could get a shot of just my leg.  Anyway, I wanted the curvature in my sole when I tiptoe, so I took some shots like that.  But that wasnt getting the bottom of the foot, so I took some like that also.

Because the kinect detects depth pretty nicely, I ended up using the bottom sole shots for the model I will base my shoes on:

![feet](https://github.com/DigitalFabricationStudio/Project_0.2/blob/master/reina.magica/shoes/screenshotfeet.png)


Tues Oct 16th

![shoemake](https://www.dropbox.com/s/6djmtwziqbv3c3u/Screen%20shot%202012-10-16%20at%203.18.49%20PM.png)

Spent time designing the shoe file.  Extruded out of the faces of the foot scan, and then levelled the bottom with a boolean difference function with a box.  All the faces were missing below the shoe somehow, and also aethetically corrected some geometries and extra faces by moving vertexes.  Corrected the toe area because it was on a slight bend upwards.  Added some holes using boolean difference between cylinders and models because that's where I put in some ribbons to tie the shoes on.

![shoemake](https://www.dropbox.com/s/adhaf34va63823h/Screen%20shot%202012-10-16%20at%204.36.52%20PM.png)

Wednesday Oct 17th

Loaded .stl file of shoe into B2B and there were some issues.  There were some extra vertices and fixed those in Blender.  Fixed the next file in B2B as an .stl and built a b2b file to print.  The estimate was 14 hours, actually the first with 40% fill was maybe 34 hours.  Anyhow, I changed the plastic to White ABS, and while printing, it wasn't really sticking to the surface, as happened often with 3dtouch, it was cooling too quick, so when the Ultimaker was back, I switched machines. In the new preview of the Macpronterface software, we could see that the bottom of the shoe was not flat, so corrected that again in blender.  The ultimaker was broken and needed recalibration, so now its the second/third attempt to print and looking alright. Also, the length was only 16.5 instead of 19.98 as stated in the b2b software, so the scaling function is inaccurate in B2B. 


![b2btouchsucks](http://farm9.staticflickr.com/8193/8096917823_82ee505c57_z.jpg)

I switched to clear PLA because its already there and has a nice effect so you can see the meshes and inside the shoe.

![ultimaker](http://farm9.staticflickr.com/8193/8096917105_a7ae74c27c_z.jpg)


Settings:
Layer Height:0.4
Fill density: 0.2
Fill Pattern: Honeycomb
top/bottom fill: rectilinear

Infill every 1 layer
solid infill every 0 layer
fill angle 45
Solid infill threshold 70mm2
Speed: 30mm/s on perimeters
60mm on infills and bridges
130 mm travel
first layer at 30%
skirt  - 3loops, 6mm, 1 layer, 5mm width
support material yes, overhang threshold 45, rectilinear, 4mm pattern spacing, pattern angle 0


## LICENSE
<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-nd/3.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/3.0/deed.en_US">Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License</a>.