#Lasercut Zoetrope

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Lasercut Zoetrope</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://www.nstrm.com" property="cc:attributionName" rel="cc:attributionURL">toni</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/">Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License</a>.<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/DigitalFabricationStudio/Project_0.2/blob/master/toni.enstrom/03_zoetrope.md" rel="dct:source">https://github.com/DigitalFabricationStudio/Project_0.2/blob/master/toni.enstrom/03_zoetrope.md</a>.<br />Permissions beyond the scope of this license may be available at <a xmlns:cc="http://creativecommons.org/ns#" href="http://www.nstrm.com" rel="cc:morePermissions">http://www.nstrm.com</a>.

###Idea & structure

To build a laser cut "3D" zoetrope with a bicycling character.
<br/><br/>
<b>Material</b><br/>
- MDF 4mm<br/>
<br/>

<b>Pieces</b><br/>
- bottom (1) (approx 340mm diameter)<br/>
- top (1) (approx 340mm diameter) <br/>
- walls (15) (65*98mm) <br/>
- character frames (15) (60*75mm) <br/>

<b>Holes and notches</b><br/>
- holes 39,8*4mm
- notches 40*4mm

###Pipeline
1. 3D-modeled and animated character + bike. 15 frames loop cycle.<br/>
2. Export frames as .PNG (bitmap) images.<br/>
3. Convert bitmap images to vector paths (to achieve cutting lines).<br/>
4. Add bottom notch outline to vector images cutting line.<br/>
5. Keep bitmap & vector images aligned on top of each other.<br/>
6. Print and assemble. No glue should be needed.<br/>

<br/>
Examples.<br/>
<b>Vector images</b> (cutting):<br/>
<img src="https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/toni.enstrom/03_zoetope_frames_cutting.png">


<br/>
<b>Bitmap images</b> (engraving):<br/>
<img src="https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/toni.enstrom/03_zoetope_frames_engraving.png">


<br/>

###Printing
In laser cutting, i used default recommended settings for 4mm MDF. (cutting: 15/60/500). In engraving i used 70% speed / 65% power, but in the end engraving wasn't really noticeable, which can be seen photos below.<br/>

Printing:<br/>
<img src="https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/toni.enstrom/03_zoetrope_printing_.jpg"><br/>

###Assembly & usage
Assembling is rather straight forward procedure. You shouldn't need glue. Place 15 biker frames in order to a inner circle of bottom plate. Then place 15 wall pieces in order to outer circle. The trickiest part is now place the ceiling plate on top of everything and make the holes match. Finalize by attaching a pivot in the center hole of bottom plate and swing the zoetrope under a powerful light source. Watch the animation go through the wall pieces.<br/>

Ready printed and assembled:<br/>
<img src="https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/toni.enstrom/03_zoetrope.jpg"><br/>

A single animation frame:<br/>
<img src="https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/toni.enstrom/03_zoetrope_piece.jpg"><br/>


###Summary
I had already modeled and animated bicycling character in a 3D software. 2D animation could have been used as well in my project. However, 3D animation could have been used in 3D printer also. I included the 3D files (animation frames as separate models) in project folder. They can be used if someone wants to test printing them etc.

For a zoetrope pivot i used an old bicycle front wheel axis. It’s a little rough solution, but works in prototyping. A more elegant solution should be designed for next version. 

Also about other improvements, an enhanced version of a zoetrope could use a built-in light source, either placed between the layers (walls & character frames) or then in the ceiling piece. Now the zoetrope works as it is, but it needs to be used in a properly lit environment. 

One more note. The gaps between walls ("shutter length") are now little less 2mm. I prototyped with slightly wider gaps, but this made animation look more messy and didn't really provide more light to it. I also prototyped adding "background animation" to wall pieces (2d engraved horizon line) behind the cut biker, but this didn't seem to be a good idea, because it just made the overall animation more unclear and messy.
