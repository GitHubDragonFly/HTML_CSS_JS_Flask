# HTML_CSS_JS_Flask
Generally intended for educational purposes.

This is an expanded and modified version of the [HTML_CSS_JS](https://github.com/GitHubDragonFly/HTML_CSS_JS) project, set to be used with `python3` and `Flask` server.

The main differences between these 2 projects:
 - the `Form` entries are handled by the server so that part of the GUI is slightly different
 - uploading any pictures via the `Form` will then have those saved in the new `uploads` folder
 - new additions are three.js FBX, VRML, 3DM (rhino) and MMD (Miku Miku Dance) viewers and a TGA texture viewer
 - almost all viewers in this project support `URL` loading, use `Orbit Controls`, have a `grid / polar grid` buttons and a `gizmo` present
 - DRACO and KTX2 support were added to the GLTF Viewer:
   - this seems to work fine when using URL option (see the screenshot) so try using it for fetching files both locally from the server and from the Internet
   - this should work fine for browsing local files which are either in binary or embedded format (try loading some `.ktx2` or `JPG/PNG/BMP/GIF` texture file along just to see if and how it changes the object's appearance)
   - you can also open `.drc` file types either alone or together with some texture file
 - KTX2 support was also added to the DAE Viewer

There are several three.js viewers, not necessarily perfect but functional as they are. Online preview links are available in the `Usage` section but do have some limitations.

Additional Notes:
 - Single character buttons, where applicable: `E` - edges, `F` - flatShading, `K` - kinematics, `A` - animations, `X`- extras, `M` - materials, `T` - textures, `P` - poses, `#` - grid
 - [OrbitControlsGizmo](https://github.com/Fennec-hub/ThreeOrbitControlsGizmo) non-module version was added to all viewers
 - VRML viewer is module based, requires a server and will not be functional in the online preview:
   - if using a server then try the following link via the URL option:
   - `https://raw.githubusercontent.com/mrdoob/three.js/master/examples/models/vrml/house.wrl`
 - FBX viewer appears to be fully functional in the online preview, see the `Usage` section for the link
   - try the following link via the URL option or see a possible `cloth.fbx` experiment further below:
   - `https://raw.githubusercontent.com/mrdoob/three.js/master/examples/models/fbx/Samba Dancing.fbx`
 - 3DM viewer appears to be fully functional in the online preview, see the `Usage` section for the link
   - it also includes dat.GUI controls to show layers
   - you could try the following example via the viewer's URL option:
   - `https://raw.githubusercontent.com/mrdoob/three.js/master/examples/models/3dm/Rhino_Logo.3dm`
 - MMD viewer supports animation, pose, extras and audio and appears to be fully functional in the online preview, see the `Usage` section for the link:
   - `ammo.wasm.wasm` file was added to the `templates` folder so the loading of local files would work
   - tested with three.js examples and has audio delayTime set for those (with current value of 3.5)
   - observe the LICENSES of that and any other content you want to use
   - if loading local files then all those files need to be in the same folder (PMD, PMX, VMD, VPD, MP3)
   - try all the different combinations of the mentioned files to see what works
   - loading files via URL option is set for either 1 or more comma separated URLs, allowing mixed sites, like the following:
   - `https://raw.githubusercontent.com/mrdoob/three.js/master/examples/models/mmd/miku/miku_v2.pmd`
   - `https://raw.githubusercontent.com/mrdoob/three.js/master/examples/models/mmd/miku/miku_v2.pmd, https://raw.githubusercontent.com/mrdoob/three.js/master/examples/models/mmd/vmds/wavefile_v2.vmd, https://raw.githubusercontent.com/mrdoob/three.js/master/examples/models/mmd/vmds/wavefile_camera.vmd, https://raw.githubusercontent.com/mrdoob/three.js/master/examples/models/mmd/audios/wavefile_short.mp3`
   - `https://raw.githubusercontent.com/takahirox/mmd-viewer-js/master/model/default/meiko_sakine.pmd, https://raw.githubusercontent.com/mrdoob/three.js/master/examples/models/mmd/vmds/wavefile_v2.vmd, https://raw.githubusercontent.com/mrdoob/three.js/master/examples/models/mmd/vmds/wavefile_camera.vmd, https://raw.githubusercontent.com/mrdoob/three.js/master/examples/models/mmd/audios/wavefile_short.mp3`
   - it includes TGA texture loader, which can be seen in action if you replace the very first line in the last example listed above to:
   - `https://raw.githubusercontent.com/takahirox/mmd-viewer-js/master/model/low_miku/gumi.pmd,`
 - DAE viewer also supports kinematics, controlled by the button with letter "K", which is module based, requires server and will not work in the online preview
   - if using a server then try the following link via the URL option:
   - `https://raw.githubusercontent.com/mrdoob/three.js/master/examples/models/collada/abb_irb52_7_120.dae`
 - DAE viewer was also updated to support DDS textures, which is functional in the online preview and can be tested via the viewer's URL option with the following example:
   - `https://raw.githubusercontent.com/SaschaWillems/VulkanSponza/master/data/sponza.dae`
 - GLTF / DAE / FBX viewers support animation whose button, with letter "A", will change green if any animation is detected and run the first one automatically
   - subsequent clicks of the button will run any subsequent animations one at the time
   - Xbot.glb is the multi-animation example that can be accessed in the GLTF viewer via the following URL:
   - `https://raw.githubusercontent.com/GitHubDragonFly/HTML_CSS_JS_Flask/main/Files/python/app/static/Images/gltf/Xbot.glb`
 - GLTF viewer also includes an experimental material switcher button (with letter "M") based on and specifically designed for this example:
   - `https://raw.githubusercontent.com/mrdoob/three.js/master/examples/models/gltf/MaterialsVariantsShoe/glTF/MaterialsVariantsShoe.gltf`
 - GLTF viewer also includes an experimental extras / morph targets button (with letter "X") which was tested as working with this example:
   - `https://raw.githubusercontent.com/mrdoob/three.js/master/examples/models/gltf/RobotExpressive/RobotExpressive.glb`
   - subsequent clicks of the button will run any subsequent morph target one at the time
   - visible facial expressions of the mentioned example are located at X6-X7-X8 for `Head_4` object, while X0 to X5 contain those same expressions but for `Head_2` and `Head_3` objects, which don't seem to have any functionality
   - do note that the above example seems to have some faults in it and has shown some disconnects and material issues, which are not necessarily visible in all viewers due to coding and design approach (try it in the viewers mentioned in the `Resources` section, with Don McCurdy's `GLTF Viewer` actually showing how many errors were detected)
   - other examples, like `Horse.glb` or `Parrot.glb`, will be showing those morph targets like frames of the animation itself
 - PLY viewer now includes STL file loader
 - 3DM / PLY / OBJ viewers also include an experimental flat shading button, with letter "F", which will be disabled for STL files
 - FBX / OBJ viewers also include an experimental texture switching button, with letter "T", which can be tested as working with the `Cerberus.obj` example:
   - local loading of the this OBJ example should also include all the image files: Cerberus_A.jpg, Cerberus_M.jpg, Cerberus_N.jpg, Cerberus_R.jpg, Cerberus_RM.jpg
   - URL loading of the same OBJ example should be done with multiple comma separated URLs: `https://raw.githubusercontent.com/mrdoob/three.js/master/examples/models/obj/cerberus/Cerberus.obj, https://raw.githubusercontent.com/mrdoob/three.js/master/examples/models/obj/cerberus/Cerberus_A.jpg, https://raw.githubusercontent.com/mrdoob/three.js/master/examples/models/obj/cerberus/Cerberus_M.jpg, https://raw.githubusercontent.com/mrdoob/three.js/master/examples/models/obj/cerberus/Cerberus_N.jpg, https://raw.githubusercontent.com/mrdoob/three.js/master/examples/models/obj/cerberus/Cerberus_R.jpg, https://raw.githubusercontent.com/mrdoob/three.js/master/examples/models/obj/cerberus/Cerberus_RM.jpg`
   - for FBX viewer, you can experiment with the above just by changing the first line to: `https://raw.githubusercontent.com/mrdoob/three.js/master/examples/models/fbx/cloth.fbx,`
   - also check this [link](https://casual-effects.com/data/) for additional OBJ examples, specifically `Crytek Sponza` and `Dabrovic Sponza`
 - See GLTF / DRACO / DAE / STL examples in the `Images` folder, most of which were downloaded from [three.js](https://github.com/mrdoob/three.js) and there is more examples there if you bother checking it out (all of them should be accessible in all viewers via the URL option targeting `raw.githubusercontent.com`, just like the links above show)
 - TGA (Truevision TGA or TARGA) texture viewer is fully functional in the online preview:
   - it only serves a purpose of showing `tga` file when applied to a cube
   - source could be either local `tga` files or online files via their URLs (multiple URLs need to be comma separated), like the following:
   - `https://raw.githubusercontent.com/mrdoob/three.js/master/examples/textures/crate_grey8.tga, https://raw.githubusercontent.com/mrdoob/three.js/master/examples/textures/crate_color8.tga`
   - texture switching button ("T") will let you switch between multiple textures

Notes about showing the edges (button with letter "E"):
 - these are aplied to the still version of the object itself and will not follow the animation in supported viewers but will follow kinematics in the DAE viewer
 - thresholdAngle is set to 30 which produces approximate outline edges (if no edges are visible then lower this number)
 - use a combination of different Opacity / Directional Light Intensity values to control visibility of the object vs edges
 - edges might not be visible if the wireframe is turned on
 - some objects might have edges placed in awkward places (like the `Xbot.glb` example, barely visible between its feet)
 - edges are not set to cast shadow

# Usage
All it takes to run this project is to do either of the below listed:

a) Even though this is all intended to be used with the `Flask` server, thanks to the [GitHub & BitBucket HTML Preview](https://github.com/htmlpreview/htmlpreview.github.com) you can still preview the [Exercise](https://htmlpreview.github.io/?https://github.com/GitHubDragonFly/HTML_CSS_JS_Flask/blob/main/Files/python/app/templates/Exercise.html) page online and use its fixed menu to access the rest, with the following limitations:
 - GLTF Viewer does allow loading DRACO files but does not allow loading KTX2 textures (check the module "import" console error)
 - DAE Viewer will not allow loading KTX2 textures or support kinematics (check the module "import" console error)
 - VRML viewer is module based, requires a server and will not be functional in the preview (check the module "import" console error)
 - The Form entries are set to be handled by the server and will not work in the preview

And just for the convenience, you can access three.js viewers directly here: [OBJ](https://htmlpreview.github.io/?https://github.com/GitHubDragonFly/HTML_CSS_JS_Flask/blob/main/Files/python/app/templates/OBJ%20Viewer.html) / [PLY + STL](https://htmlpreview.github.io/?https://github.com/GitHubDragonFly/HTML_CSS_JS_Flask/blob/main/Files/python/app/templates/PLY%20Viewer.html) / [FBX](https://htmlpreview.github.io/?https://github.com/GitHubDragonFly/HTML_CSS_JS_Flask/blob/main/Files/python/app/templates/FBX%20Viewer.html) / [3DM](https://htmlpreview.github.io/?https://github.com/GitHubDragonFly/HTML_CSS_JS_Flask/blob/main/Files/python/app/templates/3DM%20Viewer.html) / [DAE](https://htmlpreview.github.io/?https://github.com/GitHubDragonFly/HTML_CSS_JS_Flask/blob/main/Files/python/app/templates/DAE%20Viewer.html) / [GLTF](https://htmlpreview.github.io/?https://github.com/GitHubDragonFly/HTML_CSS_JS_Flask/blob/main/Files/python/app/templates/GLTF%20Viewer.html) / [MMD](https://htmlpreview.github.io/?https://github.com/GitHubDragonFly/HTML_CSS_JS_Flask/blob/main/Files/python/app/templates/MMD%20Viewer.html) / [TGA](https://htmlpreview.github.io/?https://github.com/GitHubDragonFly/HTML_CSS_JS_Flask/blob/main/Files/python/app/templates/TGA%20Viewer.html)

b) OR with the `Flask` server support:

 - Download a zip file of this project (or clone the repo), also useful for having the example files locally available for loading
 - Install `python3` and pip install the `flask` package
 - Use the command prompt to navigate to the `app` folder and run the following command: `python -m app` or `python3 -m app`
 - The server will show you the IP address and the port, generally accessible in the Internet browser via `localhost:5000`.

Note: Opening any of the three.js viewers `HTML` files directly from your hard drive in the browser will probably have some limitations due to the CORS restrictions that your browser might have enabled. This is why the `Flask` server should be used. Also, loading any textures directly from your hard drive might make the object look either correct or interesting or funny.

Optionally use VS Code for editing, troubleshooting and running the app, which should be far easier than using the command prompt.

# Licensing
This is MIT licensed.

Three.js MIT license is included in the `python/app/static/js` folder together with a link to jQuery and OrbitControlsGizmo MIT license.
Some files/examples obtained from the three.js project might have a note included about their own license.

The beach video and the cube/die image were downloaded as a free media content and are under the [Pixabay License](https://pixabay.com/service/license/).

# Trademarks
Any and all trademarks, either directly or indirectly mentioned here, belong to their respective owners.

# Resources
Check the resources mentioned in the original HTML_CSS_JS project.

Here are links to other online viewers:
- [Online 3D Viewer](https://github.com/kovacsv/Online3DViewer)
- [GLTF Viewer](https://gltf-viewer.donmccurdy.com/)
- [3D Viewer](https://rufus31415.github.io/sandbox/3d-viewer)

The following viewer is a Windows application, useful to a degree but the project appears to have been abandoned:
- [Open 3D Model Viewer](https://github.com/acgessler/open3mod)
