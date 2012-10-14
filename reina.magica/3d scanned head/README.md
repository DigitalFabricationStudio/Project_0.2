# Reina Magica
# 3d scanned head

![face](http://fablab.aalto.fi/site/sites/default/files/Screen%20Shot%202012-10-10%20at%201.29.37%20PM.png)

Took 54 surround pictures of model. 10 were of the top part of head. Generated 3d mesh in 123dcreate. Saved as .stl Opened in Blender apply ocmodifier in blender. Exported to .stl, opened in Netfabb, did the default repair. Brought it back to Blender, applied sculpting tools, manually resculpted the back and details. Bought it to Netfabb, repaired faces, export back to .stl.

![face](https://github.com/DigitalFabricationStudio/Project_0.2/blob/master/reina.magica/3d%20scanned%20head/reinaheadmodel.jpg?raw=true)

(https://github.com/DigitalFabricationStudio/Project_0.2/blob/master/reina.magica/reinahead5.stl)

Printed on fast setings today on Replicator:
* layer height =0.2
* perimeters = 2
* solid layers = 10
* filament diameter = 2.8
* infill speed =120
* travel_speed = 120
* single walla width = 0.56

Probably didn't need so many solid layers for such a small model.
Travel speed was too fast to be accurate, lots of blobs.

![faceonform](https://github.com/DigitalFabricationStudio/Project_0.2/blob/master/reina.magica/3d%20scanned%20head/cncmilling.jpg)

3d milling
I opened my previous head model in Blender, switched to top view, used B shortcut and select half the model to chop away.  It left a hollow half of a mesh.

I made a cube, resized it to be bigger than the half head, subdivided, selected faces to extrude, extruded a wall.  Put the head inside.  Join the two meshes together.  Exported to .stl.

In modela we checked and there were some problems with the edges of the head model because they were too close to the walls for the tool to drill, so stretched walls.

Brick of foam was too big to fit under the drill in Modela, cut it down a bit.
Made a surfacing process, 3mm depth.  Made a roughing process, and finishing process with reduced area. Set the drill point and starting point to the corner of the square which was 10mm at Y and 10mm X axis.

The whole process took something like 5 hours...
The drillhead was quite big for something so small, so its missing some details, but I had a pretty complex model with lots of faces because part of it was sculpted, not very much, but also it already was complex from the generated model alone.



## LICENSE
<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-nd/3.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/3.0/deed.en_US">Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License</a>.