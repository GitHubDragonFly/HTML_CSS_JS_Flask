The included MIT license is for three.js files in this and other project's folders. 

jQuery license can be seen here: https://jquery.org/license/

OrbitControlsGizmo MIT license can be seen here: https://github.com/Fennec-hub/ThreeOrbitControlsGizmo/blob/master/LICENSE

Notes about modifications:
 - MMDLoader file has an additional `@param {string} extension` since its code could not extract the file extension from loaded blob
 - OrbitControls file has `rotateLeft` and `rotateUp` exposed so the OrbitControlsGizmo could work properly
 - OrbitControlsGizmo file was converted to non-module so it works in preview
