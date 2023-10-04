#索引功能测试文件
from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy
import time
import random

app=Flask(__name__)

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
    性别=db.Column(db.String(5),nullable=False)
    学号=db.Column(db.Integer,nullable=False)
    学校=db.Column(db.String(45),nullable=False)
    院系专业=db.Column(db.String(45),nullable=False)
    
    def __init__(self,id, username, usersay,sex,number,school,major):
        self.用户ID = id
        self.用户名 = username
        self.用户介绍=usersay
        self.性别=sex
        self.学号=number
        self.学校=school
        self.院系专业=major

	# 返回函数
    # def __repr__(self):
    #     return '%s' % self.username

# 测试是否连接成功
# with app.app_context():
#     with db.engine.connect() as conn:
#         # rs = conn.execute("select 1")
#         rs = conn.execute(flask_sqlalchemy.text("select 1"))
#         print(rs.fetchone())  # 成功返回1 (1,)


@app.route('/test',methods=['GET','POST'])
def test():
    if request.method=='GET':
        select()
    elif request.method=='POST':
        insert(100000)
    return render_template('test.html')

def select():
    begin = time.perf_counter()
    result = Users.query.filter(Users.院系专业=="计算机").all()
    end = time.perf_counter()
    print(result)
    print(end-begin)
    with open('Lab7.txt', 'a', encoding='utf-8') as f:
        f.write(f" 查找院系专业为计算机----有索引------运行时间:    {end-begin}s\n")


def insert(max):
    begin = time.perf_counter()
    major_list=['计算机','经管','运输','电信','詹院','土木','机电','语传','建艺','理学院','Unknown']
    id=100
    username='user_100'
    usersay='这里空空如也'
    sex='sex'
    school='北京交通大学'
    major='计算机'
    number=20200000

    
    for i in range(20, max):
        id=id+1
        username='user_'+str(id)
        number=number+1
        n=random.randint(0, 10)
        major=major_list[n]
        user=Users (id, username, usersay,sex,number,school,major);
        db.session.add(user)
        db.session.commit()
    
    
    end = time.perf_counter()
    with open('Lab7.txt', 'a', encoding='utf-8') as f:
        f.write(f"SQL语句：插入---{max}组数据-----运行时间为:    {end - begin}s\n")

def test():
    print(000)

if __name__ == '__main__':
    
    app.run()
    
    
    
    

