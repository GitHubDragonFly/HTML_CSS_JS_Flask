#!flask/bin/python

import os
from flask import Flask, send_file, render_template, request, make_response

app = Flask(__name__)

fname, lname, gender, vehicle1, vehicle2, vehicle3, favcolor, pictures, img = [], [], [], [], [], [], [], [], None

uploads_dir = os.path.join(app.root_path, 'uploads')
os.makedirs(uploads_dir, mode=0o777, exist_ok=True)

@app.route('/', methods=['GET'])
def get_exercise():
    return render_template('Exercise.html')

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
        img.save(os.path.join(uploads_dir, img.filename))
        pictures.append('uploads/' + img.filename)
    else:
        pictures.append('None')

    return make_response('Form Data Processed')

@app.route('/display_form_data', methods=['GET'])
def display_form_data():
    return render_template('FormData.html', fname=fname, lname=lname, gender=gender, vehicle1=vehicle1, vehicle2=vehicle2, vehicle3=vehicle3, favcolor=favcolor, pictures=pictures)

@app.route('/<path:path>', methods=['GET'])
def get_path(path):
    if path.startswith('uploads/'):
        return send_file(os.path.join(uploads_dir, path[8:]), attachment_filename=path[8:])
    else:
        return render_template(path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)