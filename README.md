# HTML_CSS_JS_Flask
This is a modified version of the [HTML_CSS_JS](https://github.com/GitHubDragonFly/HTML_CSS_JS) project so check a description of all the features there. It is set to be used with `python3` and `Flask` server.

The main differences:
 - the `Form` entries are handled by the server so that part of the GUI is slightly different
 - uploading any pictures via the `Form` will then have those saved in the new `uploads` folder
 - DRACO and KTX2 support was added to the GLTF Viewer:
   - this seems to work fine when using URL (see the screenshot)
   - this should work fine for browsing local files which are either in binary or embedded format (try loading some `.ktx2` or `JPG/PNG` texture file along just to see if and how it changes the object's appearance)
   - you can also open `.drc` file types either alone or together with a texture file (do note that the scale is currently set to `100x` upon loading, so change it if needed)
   - see GLTF and DRACO examples in the `Images` folder (they were downloaded from [here](https://github.com/mrdoob/three.js))

All it takes to run this project is to:
 - Download a zip file of this project (or clone the repo)
 - install python3 and flask package
 - use the command prompt to navigate to the `app` folder and run the following command: `python -m app`

The server will show you the IP address and the port, generally accessible in the Internet browser via `localhost:5000`.

Optionally use VS Code for editing, troubleshooting and running the app, which should be far easier than using the command prompt.

# Licensing
This is MIT licensed.

The beach video and the cube/die image were downloaded as a free media content and are under the [Pixabay License](https://pixabay.com/service/license/).

# Trademarks
Any and all trademarks, either directly or indirectly mentioned here, belong to their respective owners.
