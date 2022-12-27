import os

from flask import Flask, request, jsonify, render_template
from main import create_upload_file,create_upload_files
from PIL import Image
from flask import Flask, flash, request, redirect, render_template, jsonify
from werkzeug.utils import secure_filename
app = Flask(__name__)

app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
# Allowed extension you can set your own
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
# Get current path
path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, 'uploads')

# Make directory if uploads is not exists
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR/tesseract.exe'  # your path may be different
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def proceed():
    if 'file' not in request.files:
        return jsonify({'error':'no file uploaded'})
    img = Image.open(request.files['file'].stream)
    image = img.save('testtemp/test.jpg')
    results = create_upload_file('testtemp/test.jpg')
    return jsonify(results)

@app.route('/table')
def index2():
    return render_template('index.html')
@app.route('/table', methods=['POST'])
def proceed2():
    if 'file' not in request.files:
        return jsonify({'error':'no file uploaded'})
    img = Image.open(request.files['file'].stream)
    image = img.save('testtemp/test.jpg')
    results = create_upload_file('testtemp/test.jpg')
    data = results
    print(data)
    return render_template('table.html', data=data)
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=[ 'POST'])
def upload_file():
    if request.method == 'POST':

        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')
        filesresults={}

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                print(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                results = create_upload_files(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                filesresults[filename]=results

                #print(results)
        print(filesresults)
        #flash('File(s) successfully uploaded')
        return jsonify(filesresults)
if __name__ == "__main__":
   # app.run("0.0.0.0",port=5000, debug=True)
    app.run(debug=True)