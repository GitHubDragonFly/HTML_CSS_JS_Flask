#!flask/bin/python

# If required then implement user access authentication / authorization
# Possibly include some sort of SQL for saving form data or just create a CSV file
# The 'uploads' folder will be saving picture files uploaded via form

import os
from flask import Flask, send_from_directory, send_file, render_template, request, make_response
from flask_cors import CORS, cross_origin

app = Flask( __name__ )
cors = CORS( app )
app.config[ 'CORS_HEADERS' ] = 'Content-Type'

fname, lname, gender, vehicle1, vehicle2, vehicle3, favcolor, pictures, img = [], [], [], [], [], [], [], [], None

uploads_dir = os.path.join( app.root_path, 'uploads' )
os.makedirs( uploads_dir, mode=0o777, exist_ok=True )

def page_not_found(e):
    return render_template( '404.html' ), 404

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/', methods=['GET'])
def get_exercise():
    return render_template( 'Exercise.html' )

@app.route('/handle_form_data', methods=['POST'])
def handle_form_data():
    fname.append(request.form.get('fname'))
    lname.append(request.form.get('lname'))
    gender.append(request.form.get('gender'))
    vehicle1.append(request.form.get('vehicle1'))
    vehicle2.append(request.form.get('vehicle2'))
    vehicle3.append(request.form.get('vehicle3'))
    favcolor.append(request.form.get('favcolor'))

    img = request.files.get('file')

    if img:
        img.save( os.path.join( uploads_dir, img.filename ) )
        pictures.append( 'uploads/' + img.filename )
    else:
        pictures.append( 'None' )

    return make_response( 'Form Data Processed' )

@app.route('/display_form_data', methods=['GET'])
def display_form_data():
    return render_template( 'FormData.html', fname=fname, lname=lname, gender=gender, vehicle1=vehicle1, vehicle2=vehicle2, vehicle3=vehicle3, favcolor=favcolor, pictures=pictures )

@app.route('/static/js/libs/draco/draco_decoder.wasm')
def send_draco_wasm():
    file_path = app.root_path + os.path.normpath( '/static/js/libs/draco/draco_decoder.wasm' )
    return send_file( file_path , mimetype = 'application/wasm')

@app.route('/static/js/libs/basis/basis_transcoder.wasm')
def send_basis_wasm():
    file_path = app.root_path + os.path.normpath( '/static/js/libs/basis/basis_transcoder.wasm' )
    return send_file( file_path , mimetype = 'application/wasm')

@app.route('/static/js/libs/ammo.wasm.wasm')
def send_ammo_wasm():
    file_path = app.root_path + os.path.normpath( '/static/js/libs/ammo.wasm.wasm' )
    return send_file( file_path , mimetype = 'application/wasm')

@app.route('/<path:path>', methods=['GET'])
@cross_origin()
def get_path(path):
    if path != 'undefined':
        try:
            if path.startswith('uploads/'):
                return send_file( path )
            else:
                return render_template( path )
        except Exception as e:
            return page_not_found( e )
    else:
        return make_response( 'Path is undefined' )

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)