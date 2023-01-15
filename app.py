from unittest import result
from flask import *
from werkzeug.utils import *
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
    db = peachDB()
    result = db.getAllPost()
    db.close_sql()
    return render_template('index.html',result=result)


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
    html_id = request.get_data()
    db = peachDB()
    result = db.get_html_id_info((html_id).decode('ascii'))
    db.close_sql()    
    if(result!="error"):
        text = f'''
            "store_name" : "{result[1]}",
            "store_phone" : "{result[4]}",
            "store_web" : "{result[5]}",
            "store_addr" : "{result[6]}",
            "store_time" : "{result[7]}"
            
        '''
        return "{" + text + "}"
    else:
        return '{"error":"error"}'

@app.route('/post/<path:path>')
def getPost(path):
    try:
        # get db item
        db = peachDB()
        if(type(path) != str):
            path =(path).decode('ascii')
        result_context = db.getPost(path)
        result_img = db.getImgur(path)
        db.close_sql()

        # return the results
        result_string_list = result_context[3].split('\n')
        return render_template('post.html', title = result_context[2], context = result_string_list, result_img = result_img[2],titleImg = result_context[6])
    except Exception as ex:
        print(ex)
        return redirect('/',code=302)


@app.route('/getStoreTitleImg',methods=['GET','POST'])
def getStoreTitleImg():
    html_id = request.get_data()
    db = peachDB()
    result_img = db.getPost((html_id).decode('ascii'))
    db.close_sql()
    result_img = result_img[6]
    return result_img

@app.route('/ControlPanel')
def controlPanel():
    return render_template('controlPanel.html')
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
