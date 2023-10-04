import typing as t
from flask import Flask,render_template,request,redirect,url_for,make_response,json,jsonify,abort
#Flask实例化app,render_template渲染模板,
#request获取请求数据,
#redirect重定向,+urt_for重定向函数，
#make_response把数据传给前端,json,jsonify将字典转为json
#abort抛出异常
from wtforms import StringField,PasswordField,SubmitField  #类型
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,EqualTo #验证数据不能为空，验证数据是否相同
#等价于前端的form表单
from flask_sqlalchemy import SQLAlchemy
#flask数据库
from werkzeug.routing.map import Map

app=Flask(__name__)
app.config['JSON_AS_ASCII']=False
app.config['SECRET_KEY']='ASDFG'   #解决报错后端跨站访问

#数据库配置
#https://blog.csdn.net/qq_42265220/article/details/120670267
#https://blog.csdn.net/qq_41603102/article/details/88792295?ops_request_misc=&request_id=&biz_id=102&utm_term=flask_sqlalchemy%E6%95%99%E7%A8%8B&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-4-88792295.142^v86^wechat,239^v2^insert_chatgpt&spm=1018.2226.3001.4187
class Config:
    SQLALCHEMY_DATABASE_URI='mysql://root:123456@127.0.0.1:3306/zhihu'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
app.config.from_object(Config)
#SQLAlchemy和app绑定
db=SQLAlchemy(app)
#创建数据库模型类（表）
class Users(db.Model):
    # Users._Users__tablename__-'users'
    用户ID = db.Column(db.Integer, primary_key=True, nullable=False)
    用户名= db.Column(db.String(45),  nullable=False)
    用户介绍= db.Column(db.String(100),nullable=False)
    
    def __init__(self,id, username, usersay):
        self.用户ID = id
        self.用户名 = username
        self.用户介绍=usersay
	# 返回函数
    # def __repr__(self):

    #     return '%s' % self.username

@app.route('/skip_insert',methods=['GET','POST'])
def skip_insert():
    if request.method=='GET':
        return render_template('insert.html')

#创建所有表db.creat_all()清除所有表db.drop_all()
#添加用户
@app.route('/insert',methods=['GET','POST'])
def insert():
    #render_template('hello.html')
    if request.method=='GET':
        return render_template('insert.html')
    if request.method=='POST':
        #print("POST")
        id=int(request.form.get('用户ID'))
        username=request.form.get('用户名')
        usersay=request.form.get('用户介绍')
        user = Users(id,username,usersay)
        
        # user.用户ID=int(request.form.get('用户ID'))
        # user.用户名=request.form.get('用户名')
        # user.用户介绍=request.form.get('用户介绍')

        #print(username)
        # 将新创建的用户添加到数据库会话中
        db.session.add(user)
        # 将数据库会话中的变动提交到数据库中, 如果不commit, 数据库中是没有变化的.
        db.session.commit()
        return render_template('insert.html')
    
        
#删除用户
@app.route('/drop',methods=['GET','POST'])
def drop():
    if request.method=='POST':
        #print("POST")
        userid=int(request.form.get('删除ID'))
        
        # 获取用户对象
        user = Users.query.filter_by(用户ID=userid).first() #查询出id=1的用户
        # 删除用户
        db.session.delete(user)
        #提交数据库会话
        db.session.commit()
    return render_template('drop.html')
        


#修改用户信息
@app.route('/upgate',methods=['GET','POST'])
def upgate():
    if request.method=='POST':
        #print("POST")
        userid=int(request.form.get('userID'))
        username=request.form.get('username')
        usersay=request.form.get('usersay')
        # 获取用户对象
        user = Users.query.filter_by(用户ID=userid).first()
        # 直接赋值更新数据
        user.用户名 = username
        user.用户介绍=usersay
        #提交数据库会话
        db.session.commit()
    return render_template('upgate.html')


#查询用户信息
@app.route('/select',methods=['GET','POST'])
def select():
    #render_template('hello.html')
    if request.method=='GET':
        return render_template('select.html')
    if request.method=='POST':
        #print("POST")
        id=request.form.get('userID')
        username=request.form.get('username')
        usersay=request.form.get('usersay')
        print(usersay)
        print(username)
        print(id)
        
        if not id:
            if not username:
                if not usersay:
                    users_list=Users.query.all()
                    print(users_list)
                else:
                    users_list = Users.query.filter(Users.用户介绍==usersay).all()
            else:
                if not usersay:
                    users_list = Users.query.filter(Users.用户名==username ).all()
                else:
                    users_list = Users.query.filter(Users.用户名==username ,Users.用户介绍==usersay).all()
        else:
            id=int(id)
            if not username:
                if not usersay:
                    users_list = Users.query.filter(Users.用户ID==id).all()
                else:
                    users_list = Users.query.filter(Users.用户ID==id,Users.用户介绍==usersay).all()
            else:
                if not usersay:
                    users_list = Users.query.filter(Users.用户ID==id,Users.用户名==username ).all()
                else:
                    users_list = Users.query.filter(Users.用户ID==id,Users.用户名==username ,Users.用户介绍==usersay).all()

        return render_template('show.html',users_list=users_list)

##################################################################################################

#hello
@app.route('/hello',methods=['GET','POST'])
def hello():
    return '<h1>hello<h1>'

#json数据
@app.route('/json',methods=['GET','POST'])
def json():
    data={
        'name':"张三"
    }
    #转为json(1) 
    response= make_response(json.dumps(data,ensure_ascii=False))#中文
    response.mimetype='application/json'
    #转为json(2)
    #前面加上一行app.config['JSON_AS_ASCII']=False
    response=jsonify(data)
    return response


#<url提取参数>
#'/hi/<int:id>'
#'/hi/<string:id>'接受不包含/的文本
#'/hi/<path:id>'接受包含/的文本
#'/hi/<float:id>'接受正浮点数
#'/hi/1\d{10}'以1开头10位
@app.route('/url/<id>',methods=['GET','POST'])
def url():
    if id=='1':
        return 'url'
    return '<h1>url<h1>'
#自定义转换器
# from werkzeug.routing import BaseConverter
# class RegexConverter(BaseConverter):
#     def __init__(self, url_map,regex):
#         #调用父类方法
#         super(RegexConverter.self).__init__(url_map)
#         self.regex=regex
#     def to_python(self, value: str):
#         return value
#将自定义转换器添加到flask应用中
#app.url_map_converters['re']=RegexConverter
#@app.route('/hi/<re("")>',methods=['GET','POST'])

#重定向
@app.route('/baidu')
def baidu():
    #return redirect('https://www.baidu.com')
    return redirect(url_for('login'))

#模板
#https://www.cnblogs.com/xiaxiaoxu/p/10428508.html
@app.route('/temp',methods=['GET','POST'])
def temp():
    data={
        'username':"张三",
        'password':'123',
        'admin':[0,1,2],
    }
    #前端中使用
    # {{data}}
    # {{data.mylist[0]}}
    # {{data.mylist[0]+data.mylist[0]}}
    return render_template('login.html',data=data)
#过滤器
    #{{"hello" | upper}}
    #{{"hello" | replace('hello','hi')}}
#自定义过滤器
def list_step(li):
    return li[::2]
#注册过滤器(自定义函数名字，你要用时的名字)
app.add_template_filter(list_step,'li2')
#前端中{{"hello" | li2}}


#定义表单模型类
class Register(FlaskForm):
    username=StringField(label='用户名',validators=[DataRequired('用户名不能为空')])
    password=StringField(label='密码',validators=[DataRequired('密码不能为空')])
    password2=StringField(label='再次输入密码',validators=[DataRequired('密码不能为空'),EqualTo('password')])
    sunmit=SubmitField(label='提交')
#form表单
@app.route('/register',methods=['GET','POST'])
def register():
    #创建表单对象
    form=Register()
    if request.method=='GET':
        return render_template('register.html',form=form)
    else:
        #验证表单传过来的数据都是正确的
        if form.validate_on_submit():
            username=form.username.data
            password=form.password.data
        return render_template('register.html',form=form)

#前端使用form表单发送
#后端使用request获取数据
@app.route('/loginer',methods=['GET','POST'])
def loginer():
    if request.method=='GET':
        return render_template('login.html')
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        print(username)
        if username=='zhangsan' and password=='123':
            return 'login sucess'
        else :
            
            abort(404)    
            return 'this is post'
#自定义错误
@app.errorhandler(404)
def handle_404_error(err):
    return '出现了404错误，错误信息是s%'%err


##############################################################################################
#登入
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        print(username)
        if username=='zhangsan' and password=='123':
            return render_template('index.html')
        else :
            abort(404)    

#首页
@app.route('/index',methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('index.html')
    if request.method=='POST':
        return render_template('index.html')
    

#用户信息管理
@app.route('/users',methods=['GET','POST'])
def users():
    if request.method=='GET':
        return render_template('users.html')
    if request.method=='POST':
        return render_template('users.html')


if __name__=='__main__':
    app.run()