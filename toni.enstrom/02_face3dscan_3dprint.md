
# Face scan

### Scanning

Kinect device and CocoaKinect application (http://www.thingiverse.com/thing:8262) was used to take a 3d scan of my face. CocoaKinect saved scan instantly to a .STL file, but basically the model geometry needed plenty of cleanup in 3d modeling software. I used 3ds Max and Blender3d to make the model's topology more clear and also to reduce the polygon count.

Alternative way to scan one's face in 3d, was taking a bunch of photos of a target and let the software (123D Catch) stitch the 3d model file from those. I tried this by placing my camera on a tripod, programming it to take photo every 2 seconds, and rotating myself in front of this fixed positioned camera. This didn't work, '123D Catch' only returned an error. My guess is, the target should be steady and camera go around it instead, so that the light source always touches same spots of target surface in every photo and the software can use triangulation in building the model.
So all i got from this test was this goofy animation:
http://dl.dropbox.com/u/24959049/toni_rotation.gif

### Printing

After cleaning up and cropping the 3d model, i just threw it in to a software (name of software?) that prepares the print-ready file for the 3d Touch printer. Didn't do much for the settings, just aimed to keep the print time estimation reasonable (25min, print size 2x3x2cm).

<img src="https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/toni.enstrom/02_face_print_settings.png">

<img src="https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/toni.enstrom/02_face.jpg">


### Milling

Milling took overall approx 60 minutes (surfacing + roughing + finalizing). I used same 3d model as in printing, plus added the box around the faceplate. Afterwards i thought i could have left the box unmodeled and instead crop the milling area in print settings, plus add few millimeters depth to the surfacing settings.

<img src="https://raw.github.com/DigitalFabricationStudio/Project_0.2/master/toni.enstrom/02_face_milling_.jpg">