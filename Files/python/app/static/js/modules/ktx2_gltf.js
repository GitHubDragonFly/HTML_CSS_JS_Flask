import { KTX2Loader } from '../KTX2Loader.js';

export function ktx2_loader( manager, gltf_loader, renderer ) {
    let ktx2 = new KTX2Loader( manager );
    ktx2.setTranscoderPath('../static/js/libs/basis/');
    ktx2.detectSupport( renderer );

    gltf_loader.setKTX2Loader( ktx2 );

    return ktx2;
}