from flask import *
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from peach10000 import Sql, app, User

import os

app.secret_key = os.urandom(16).hex()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = "strong"
login_manager.login_view = 'login'


@login_manager.user_loader
def user_loader(user):
    temp_user = User.user()
    if(temp_user.checkUser(username = user)==True):
        user = User.flask_login_user()
        user.id = user
        return user

    else:
        return 

@login_manager.request_loader
def request_loader(request):
    temp_user = User.user()
    user_str = request.form.get('user_id')
    # password = request.form['password']
    if (temp_user.checkUser(username = user_str)==True):
        user = User.flask_login_user()
        user.id = user_str
        user.is_authenticated = temp_user.checkLogin(username = user_str, password = request.form['password'])
        return user

@app.route("/")
def index():
    db = Sql.peachDB()
    result = db.getAllPost()
    db.close_sql()
    return render_template('index.html',result=result)


@app.route("/Map")
def map():
    return render_template('Map.html')


@app.route("/test")
def test():
    return render_template('test.html')

@app.route("/Login", methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', message = '請登入帳號')

    if request.method == 'POST':
        account = request.form['account']
        password = request.form['password']
        temp_user = User.user()
        status = temp_user.checkLogin(username = account, password = password)
        
        if(status == True):
            user = User.flask_login_user()
            user.id = account
            login_user(user)
            return redirect(url_for('controlPanel'))    
        else:
            return render_template('login.html', message='帳號或密碼錯誤')

@app.route('/logout')
def logout():
    user = current_user.get_id()
    logout_user()
    return render_template('login.html', message = f'{user}帳號已登出.')

@app.route('/get_info',methods=['GET','POST'])
def query_info():
    html_id = request.get_data()
    db = Sql.peachDB()
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


@app.route("/font/<path:path>")
def ttf(path):
    return send_from_directory(directory = './font/', 
        path = path, 
        as_attachment = True,
        environ = request.environ
    )


@app.route('/post/<path:path>')
def getPost(path):
    try:
        # get db item
        db = Sql.peachDB()
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
    db = Sql.peachDB()
    result_img = db.getPost((html_id).decode('ascii'))
    db.close_sql()
    result_img = result_img[6]
    return result_img


@app.route('/ControlPanel')
def controlPanel():
    return render_template('controlPanel.html')


