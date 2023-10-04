#完整项目运行主函数
import typing as t
from flask import Flask,render_template,request,redirect,url_for,make_response,json,jsonify,abort,session,g
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
from sqlalchemy .sql import select,join
from sqlalchemy import text
#flask数据库

from datetime import datetime

app=Flask(__name__)
app.secret_key = '11'  #session密钥
app.config['JSON_AS_ASCII']=False
app.config['SECRET_KEY']='ASDFG'   #解决报错后端跨站访问


class Config:
    SQLALCHEMY_DATABASE_URI='mysql://root:123456@127.0.0.1:3306/zhihu'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
app.config.from_object(Config)
#SQLAlchemy和app绑定
db=SQLAlchemy(app)

#想要将路由改成/<id>/myQuestions根据用户id访问




# 消除非主属性对码的部分函数依赖，消除非主属性对码的传递函数依赖。
# 所有实体型均满足了3NF。非主属性之间不存在函数依赖关系。
# 先并到一个文件里，之后再分到不同文件中
class Users(db.Model):
    # Users._Users__tablename__-'users'
    用户ID = db.Column(db.Integer, primary_key=True, nullable=False,autoincrement=True)
    用户名= db.Column(db.String(45),  nullable=False)
    用户介绍= db.Column(db.String(100),nullable=False)
    性别=db.Column(db.String(5),nullable=False)
    学号=db.Column(db.Integer,nullable=False)
    学校=db.Column(db.String(45),nullable=False)
    院系专业=db.Column(db.String(45),nullable=False)
    密码=db.Column(db.String(20),nullable=False)
    
    def __init__(self, user_name, user_say,sex,stu_number,school,major,password):
        # self.用户ID = user_id
        self.用户名 = user_name
        self.用户介绍=user_say
        self.性别=sex
        self.学号=stu_number
        self.学校=school
        self.院系专业=major
        self.密码=password

	# 返回函数
    # def __repr__(self):
    #     return '%s' % self.username

class Answers(db.Model):
    # Users._Users__tablename__-'users'
    答案ID = db.Column(db.Integer, primary_key=True, nullable=False,autoincrement=True)
    问题ID= db.Column(db.Integer,  nullable=False)
    回答者ID= db.Column(db.Integer,nullable=False)
    点赞数量=db.Column(db.Integer,nullable=False, default=0)
    回答内容=db.Column(db.String(100),nullable=False)
    #可以替换为LONGTEXT类型
    回答时间=db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self,user_id, reuser_id,hot_number,ans):
        # self.答案ID = ans_id
        self.问题ID = user_id
        self.回答者ID=reuser_id
        self.点赞数量=hot_number
        self.回答内容=ans
        
	# 返回函数
    # def __repr__(self):
    #     return '%s' % self.username

class Questions(db.Model):
    # Users._Users__tablename__-'users'
    问题ID = db.Column(db.Integer, primary_key=True, nullable=False,autoincrement=True)
    提问者ID= db.Column(db.Integer,  nullable=False)
    问题名称= db.Column(db.String(100),nullable=False)
    回答数量=db.Column(db.Integer,nullable=False, default=0)
    提问时间=db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, asuser_id, que,ans_number):
        # self.问题ID = que_id
        self.提问者ID = asuser_id
        self.问题名称=que
        self.回答数量=ans_number
        
	# 返回函数
    # def __repr__(self):
    #     return '%s' % self.username

class Articals(db.Model):
    # Users._Users__tablename__-'users'
    文章ID = db.Column(db.Integer, primary_key=True, nullable=False,autoincrement=True)
    作者用户ID= db.Column(db.Integer,  nullable=False)
    赞同数= db.Column(db.Integer,nullable=False,default=0)
    文章内容=db.Column(db.String(1000),nullable=False)
    文章名称=db.Column(db.String(100),nullable=False)
    创作时间=db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, auuser_id, yes_number,art,art_tittle):
        # self.文章ID = art_id
        self.作者用户ID = auuser_id
        self.赞同数=yes_number
        self.文章内容=art
        self.文章名称=art_tittle

	# 返回函数
    # def __repr__(self):
    #     return '%s' % self.username

# 用户密码视图
# 请注意，这里的写操作是针对基础表格而不是视图。当基础表格的数据更改后，视图将会自动更新。
# 通常情况下，数据库视图是只读的，因此无法直接通过模型类来插入或更新视图数据。如果你需要在视图上进行写操作，你可能需要针对视图所基于的表格进行插入和更新操作。
class V_users_password(db.Model):
    __tablename__ = 'V_users_password'
    用户ID = db.Column(db.Integer, primary_key=True, nullable=False,autoincrement=True)
    用户名= db.Column(db.String(45),  nullable=False)
    密码=db.Column(db.String(20),nullable=False)

#蓝图最后优化时再处理
@app.route('/',methods=['GET','POST'])
def hello():
    return '<h1>hello<h1>'

@app.route('/')
def execute_stored_procedure():
    procedure_name = 'your_stored_procedure_name'
    result = db.session.execute(text(f"CALL {procedure_name}()"))

    # 处理结果
    # ...

    return "Stored procedure executed successfully"

#登入
#界面优化，弹窗提示alert
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        print("获取到信息")
        # user=db.session.query(Users).filter(Users.用户名 == username).all()
        # 通过视图去查询
        user = db.session.query(V_users_password).filter(V_users_password.用户名 == username).all()  # 查询所有视图数据

        if(user==[]):
            # 注册
            user = Users(user_name=username,user_say="空空如也",sex="sex",stu_number=0,school="Unknown",major="Unknown",password=password)
            db.session.add(user)
            db.session.commit()
            print("注册成功")
            
        if username=='zhangsan' and password=='123':
            print("管理员")
            return render_template('index.html')
        else :
            user = Users.query.filter(Users.用户名 == username,Users.密码 == password).first()
            if(user):
                print(user.用户名)
                print(user.密码)
                session['id'] = user.用户ID
                
# 存储过程根据用户id返回用户名并打印
                procedure_name = 'find_userid'
                # result = db.session.execute(text(f"CALL {procedure_name}()"))
                # print(result)
                # for row in result.fetchall():
                # # 处理每一行数据
                # # ...
                result = db.session.execute(text(f"CALL {procedure_name}(:name, @user_id)"), {"name": username})
                #使用了命名参数 :name 来传递存储过程的输入参数 name 的值，并使用用户变量 @user_id 来存储存储过程的返回值。
                user_id = db.session.execute(text("SELECT @user_id")).scalar()
                # 使用了 text() 函数，明确将存储过程调用语句声明为文本 SQL 表达式。
                # 使用 .scalar() 方法从结果中获取单个值，即存储过程的返回值。
                print("使用存储过程获得用户ID:"+str(user_id))



                
                # return render_template('myQuestions.html')   #一直出错因为没有使用重定向
                return redirect(url_for('myQuestions'))
            else:
                #提示密码错误
                print("密码错误")
                return render_template('login.html')   

#《我的》
#导航：我的问题
@app.route('/myQuestions',methods=['GET','POST'])
def myQuestions():
    # questions=Questions.query.filter(Questions.提问者ID==id).all()
    id=session['id']
    print(id)
    user=db.session.query(Users).filter(Users.用户ID == id).all()
    questions = db.session.query(Users, Questions).filter(Users.用户ID==id,Users.用户ID == Questions.提问者ID).all()
    # query = db.session.query(Users, Questions).join(Post, User.id == Post.user_id).all()
    
    # print(questions[0].用户ID)这样的关键字是错误的
    #print(user[0].Users.用户名)也是错的
    
    return render_template('myQuestions.html',questions=questions,user=user)
#导航：我的文章
@app.route('/myArticals',methods=['GET','POST'])
def myArticals():
    id=session['id']
    print(id)
    user=db.session.query(Users).filter(Users.用户ID == id).all()
    articals = db.session.query(Users, Articals).filter(Users.用户ID==id,Users.用户ID == Articals.作者用户ID).all()
    print(articals)
    # print(articals[0].Articals.作者用户ID)
    return render_template('myArticals.html',articals=articals,user=user)
#导航：我的答案
@app.route('/myAnswers',methods=['GET','POST'])
def myAnswers():
    id=session['id']
    print(id)
    user=db.session.query(Users).filter(Users.用户ID == id).all()
    answers = db.session.query(Questions, Answers).filter(Questions.问题ID==Answers.问题ID,Answers.回答者ID == id).all()
    print(answers)
    return render_template('myAnswers.html',answers=answers,user=user)

#搜索功能
@app.route('/showSearch/<search_term>',methods=['GET','POST'])
def showSearch(search_term):
    id=session['id']
    print(id)
    user=db.session.query(Users).filter(Users.用户ID == id).all()
    questions = db.session.query(Users, Questions,Answers).filter(Questions.问题名称.like(f'%{search_term}%'),Users.用户ID == Questions.提问者ID,Questions.问题ID==Answers.问题ID).all()
    articals = db.session.query(Users, Articals).filter(Articals.文章名称.like(f'%{search_term}%'),Users.用户ID == Articals.作者用户ID).all()
    # answers = db.session.query(Questions, Answers).filter(Questions.问题ID==Answers.问题ID,Answers.回答者ID == id).all()
    # print(answers)
    return render_template('showSearch.html',user=user,questions=questions,articals=articals)


# ———skip——— 》》》问题答案(成功版)
#点击回答数跳转到问题答案
#应该采用超链接方式的修改a标签
@app.route('/showAnswers/<ques_id>')
def showAnswers_id(ques_id):
    id=session['id']
    print("问题id",ques_id)
    user=db.session.query(Users).filter(Users.用户ID == id).all()
    question=db.session.query(Questions).filter(Questions.问题ID == ques_id).all()
    print("问题",question)
    answers=db.session.query(Users,Answers).filter(Users.用户ID ==Answers.回答者ID,Answers.问题ID == ques_id).all()
    return render_template('showAnswers.html',user=user,question=question,answers=answers)
# ———skip——— 》》》问题答案
#应该采用超链接方式的修改a标签
@app.route('/showAnswers',methods=['GET','POST'])
def showAnswers():
    if request.method=='GET':
        print("进入get")
        c=request.args.get('c')
        print("c=",c)

        ques_id=request.args.get('ques_id')

        id=session['id']
        user=db.session.query(Users).filter(Users.用户ID == id).all()
        question=db.session.query(Questions).filter(Questions.问题ID == ques_id).all()
        answers=db.session.query(Users,Answers).filter(Users.用户ID ==Answers.回答者ID,Answers.问题ID == ques_id).all()

        return render_template('showAnswers.html',user=user,question=question,answers=answers)
        # return redirect(url_for('myQuestions'))
    if request.method=='POST':
        print("进入post")
        return "进入post"

        #使用g对象全局变量测试
        # g.data = '111'
        # print(g.data)

        #获取登录用户个人信息
        # id=session['id']
        # user=db.session.query(Users).filter(Users.用户ID == id).all()

        #数据库操作
        # ques=db.session.query(Questions).filter(Questions.问题ID == ques_id).all()
        # answers=db.session.query(Users,Answers).filter(Users.用户ID ==Answers.回答者ID,Answers.问题ID == ques_id).all()
        
        #这是获取form表单数据
        # password=request.form.get('password')
        
        #这是获取post数据
        # ques_id = request.form['ques_id']
        # ques = request.form['ques']
        # as_user = request.form['as_user']

        
        # ques_id=request.form.get('ques_id')
        # ques=request.form.get('ques')#省略再次查询问题表所要的开销
        # as_user=request.form.get('as_user')#省略单独写一个根据问题查找提问者的函数

        # print("个人",user)
        # print("问题id",ques_id,"问题",ques)
        # #那我可以直接把as_user，ques合并发送啊，算了，下次再改
        # answers=db.session.query(Users,Answers).filter(Users.用户ID ==Answers.回答者ID,Answers.问题ID == ques_id).all()

        # #采用组件/模板...就可以省略掉user=user一直传输
        # return render_template('showAnswers.html',user=user,answers=answers,ques=ques,as_user=as_user)



#《首页》
#导航：问题
@app.route('/allQuestions',methods=['GET','POST'])
def allQuestions():
    id=session['id']
    print(id)
    user=db.session.query(Users).filter(Users.用户ID == id).all()
    questions = db.session.query(Users, Questions).filter(Users.用户ID==Questions.提问者ID).all()
    return render_template('allQuestions.html',questions=questions,user=user)
#导航：文章
@app.route('/allArticals',methods=['GET','POST'])
def allArticals():
    id=session['id']
    print(id)
    user=db.session.query(Users).filter(Users.用户ID == id).all()
    articals = db.session.query(Users, Articals).filter(Users.用户ID == Articals.作者用户ID).all()
    
    return render_template('allArticals.html',articals=articals,user=user)


#尝试用g对象来实现页面传输数据，失败
@app.route('/g',methods=['GET','POST'])
def show():
    # return '111'
    print(g.data)
    return g.data
    # return render_template(,a)




#数据库操作

#问题（增加，删除）....
#没必要增加修改问题功能
@app.route('/addQuestion',methods=['POST'])
def addQuestion():

    id=session['id']
    addQuestion_text=request.form['addQuestion_text']
    print(addQuestion_text)
    question = Questions(asuser_id=id,que=addQuestion_text,ans_number=0)
    db.session.add(question)
    db.session.commit()
    return '1'
#双击阴影“-”删除文章
@app.route('/delQuestion',methods=['POST'])
def delQuestion():
    ques_id=request.form['ques_id']
    print(ques_id)
    question = Questions.query.filter_by(问题ID=ques_id).first() #查询出id=1的用户
    db.session.delete(question)
    db.session.commit()
    # 获取用户对象
    return '1'

#答案（增加，删除）....
# 触发器：插入回答，问题.回答数+1
@app.route('/addAnswer',methods=['POST'])
def addAnswer():

    id=session['id']
    ques_id=request.form['ques_id']
    addAnswer_text=request.form['addAnswer_text']
    print(ques_id)
    answer = Answers(user_id=ques_id,reuser_id=id,hot_number=0,ans=addAnswer_text)
    db.session.add(answer)
    db.session.commit()

    return '1'
@app.route('/delAnswer',methods=['POST'])
def delAnswer():
    ans_id=request.form['ans_id']
    print(ans_id)
    answer = Answers.query.filter_by(答案ID=ans_id).first()
    db.session.delete(answer)
    db.session.commit()

    return '1'

#文章（增加，删除）....
#单击任意一个地方显示文章内容
@app.route('/addArtical',methods=['POST'])
def addArtical():

    id=session['id']
    addArtical_tittle=request.form['addArtical_tittle']
    addArtical_text=request.form['addArtical_text']
    artical = Articals(auuser_id=id,yes_number=0,art=addArtical_text,art_tittle=addArtical_tittle)
    db.session.add(artical)
    db.session.commit()

    return '1'
#双击阴影“-”删除文章
@app.route('/delArtical',methods=['POST'])
def delArtical():
    arti_id=request.form['arti_id']
    print(arti_id)
    artical = Articals.query.filter_by(文章ID=arti_id).first()
    db.session.delete(artical)
    db.session.commit()

    return '1'

#个人信息修改
@app.route('/myInformation',methods=['GET','POST'])
def myInformation():
    id=session['id']
    print(id)
    
    if request.method=='GET':
        user=db.session.query(Users).filter(Users.用户ID == id).all()
        return render_template('myInformation.html',user=user)
    if request.method=='POST':
        
        username=request.form['username']
        usersay=request.form['usersay']
        sex=request.form['li_sex']
        school=request.form['li_school']
        major=request.form['li_major']
        # 这里要转为Int类型,我怎么之前都没有注意过,是没遇到这种问题吗
        number=int(request.form['li_number'])
        
        # 获取用户对象
        newuser = Users.query.filter_by(用户ID=id).first()
        # 直接赋值更新数据
        newuser.用户名 = username
        newuser.用户介绍=usersay
        newuser.性别=sex
        newuser.学校=school
        newuser.院系专业=major
        newuser.学号=number
        #提交数据库会话
        db.session.commit()
        user=db.session.query(Users).filter(Users.用户ID == id).all()
        return render_template('myInformation.html',user=user)
    
#管理员操作
#相当垃圾,没有去改
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
        # user = Users(id,username,usersay)
        user = Users(user_name=username,user_say="空空如也",sex="sex",stu_number=0,school="Unknown",major="Unknown",password="0")
        
        
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







if __name__=='__main__':
    app.run(debug=True)
