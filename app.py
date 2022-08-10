from encodings import utf_8
from flask import *
from werkzeug.utils import *
import flask_login
import os
from sqlProcess import *

UPLOAD_FOLDER = './static/temp/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS



@app.route("/")
def index():
    db = peachDB()
    re = db.select_photoText()
    db.close_sql()
    return render_template('index.html',
    photo_text_title = re[0],
    photo_text_context = re[1],
    photo_text_photoAddr = re[2]
    )


@app.route("/Map")
def map():
    return render_template('Map.html')

    
@app.route("/test")
def test():
    return render_template('test.html')

@app.route("/upload",methods=['GET','POST'])
def upload_img():
    if request.method =='POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            return redirect(url_for('static', filename= 'temp/' + file.filename))
    return "error"

@app.route("/Login")
def login():
    return render_template('login.html')

@app.route("/font/<path:path>")
def ttf(path):
    return send_from_directory(directory = './font/', 
        path = path, 
        as_attachment = True,
        environ = request.environ
    )


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


