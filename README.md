# HTML_CSS_JS_Flask
Generally intended for educational purposes.

This is a modified version of the [HTML_CSS_JS](https://github.com/GitHubDragonFly/HTML_CSS_JS) project so check a description of all the features there. It is set to be used with `python3` and `Flask` server. There are several Three.js viewers, not necessarily perfect but functional as they are (preview link is available in the `Usage` section).

The main differences:
 - the `Form` entries are handled by the server so that part of the GUI is slightly different
 - uploading any pictures via the `Form` will then have those saved in the new `uploads` folder
 - DRACO and KTX2 support were added to the GLTF Viewer:
   - this seems to work fine when using URL (see the screenshot) so try using it for fetching files both locally and from the Internet
   - this should work fine for browsing local files which are either in binary or embedded format (try loading some `.ktx2` or `JPG/PNG/BMP` texture file along just to see if and how it changes the object's appearance)
   - you can also open `.drc` file types either alone or together with some texture file

Additional Notes:
 - GLTF and Collada DAE viewers are set to use Orbit Controls which made the code and GUI slightly simpler (see the screenshot)
 - [OrbitControlsGizmo](https://github.com/Fennec-hub/ThreeOrbitControlsGizmo) module was added to GLTF and DAE viewers
 - GLTF and DAE viewers support animation whose button, with letter "A", will change green if any animation is detected and run the first one automatically
   - subsequent clicks of the button will run any subsequent animations one at the time
   - Xbot.glb is the multi-animation example that can be accessed in the GLTF viewer via URL: `https://raw.githubusercontent.com/GitHubDragonFly/HTML_CSS_JS_Flask/main/Files/python/app/static/Images/gltf/Xbot.glb`
 - GLTF viewer also includes an experimental material switcher button (with letter "M") based on and specifically designed for this example:
   - `https://raw.githubusercontent.com/mrdoob/three.js/master/examples/models/gltf/MaterialsVariantsShoe/glTF/MaterialsVariantsShoe.gltf`
 - GLTF viewer also includes an experimental extras / morph targets button (with letter "X") which was tested as working with this example:
   - `https://raw.githubusercontent.com/mrdoob/three.js/master/examples/models/gltf/RobotExpressive/RobotExpressive.glb`
   - do note that the above example seems to have some faults in it and has shown some disconnects and material issues, which are not necessarily visible in all viewers due to coding and design approach (try it in the viewers mentioned in the `Resources` section)
 - PLY viewer also includes STL file loader
 - See GLTF / DRACO / DAE / STL examples in the `Images` folder, most of which were downloaded from [Three.js](https://github.com/mrdoob/three.js) and there is more examples there if you bother checking it out (all of them should be accessible in the viewers via the URL option targeting `raw.githubusercontent.com`, just like the links above show)

Notes about showing the edges (button with letter "E"):
 - these are aplied to the still version of the object itself and will not follow the animation in case of GLTF and DAE viewers
 - thresholdAngle is set to 30 which produces approximate outline edges (if no edges are visible then lower this number)
 - use a combination of different opacity / directional light values to control visibility of the object vs edges
 - edges might not be visible if the wireframe is turned on
 - edges are not set to cast shadow

# Usage
All it takes to run this project is to do either of the below listed:

Even though this is all intended to be used with the `Flask` server, thanks to the [GitHub & BitBucket HTML Preview](https://github.com/htmlpreview/htmlpreview.github.com) you can still preview the [Exercise](https://htmlpreview.github.io/?https://github.com/GitHubDragonFly/HTML_CSS_JS_Flask/blob/main/Files/python/app/templates/Exercise.html) page online and use its fixed menu to access the rest, with the following limitations:
 - OrbitControlsGizmo will not work in either GLTF or DAE viewer (check the module "import" console error)
 - GLTF Viewer does allow loading DRACO files but does not allow loading KTX2 textures (check the module "import" console error)
 - DAE Viewer will not allow loading KTX2 textures (check the module "import" console error)
 - The Form entries are set to be handled by the server and will not work in the preview

OR with server support:

 - Download a zip file of this project (or clone the repo), also useful for having the example files available for loading
 - install `python3` and pip install the `flask` package
 - use the command prompt to navigate to the `app` folder and run the following command: `python -m app` or `python3 -m app`

The server will show you the IP address and the port, generally accessible in the Internet browser via `localhost:5000`.

Optionally use VS Code for editing, troubleshooting and running the app, which should be far easier than using the command prompt.

# Licensing
This is MIT licensed.

Three.js MIT license is included in the `python/app/static/js` folder together with a link to jQuery MIT license.
Some examples obtained from the three.js project might have a note included about their own license.

The beach video and the cube/die image were downloaded as a free media content and are under the [Pixabay License](https://pixabay.com/service/license/).

# Trademarks
Any and all trademarks, either directly or indirectly mentioned here, belong to their respective owners.

# Resources
Check the resources mentioned in the original HTML_CSS_JS project.

Here is also a couple of links to other online viewers:
- [Online 3D Viewer](https://github.com/kovacsv/Online3DViewer)
- [GLTF Viewer](https://gltf-viewer.donmccurdy.com/)
