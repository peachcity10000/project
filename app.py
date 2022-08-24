from flask import *
from werkzeug.utils import *
import flask_login
import os
from py.sqlProcess import *

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
    return render_template('index.html')


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

@app.route("/<path:path>")
def indexjs(path):
    return send_from_directory(directory='./js/',
    path=path,
    as_attachment = True,
    environ=request.environ
    )


@app.route('/get_info',methods=['GET','POST'])
def query_info():
    return """
    {
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}
    """

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


