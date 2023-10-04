#模拟数据库类文件
#数据文件
from datetime import datetime
from zhihuflask import db

# 消除非主属性对码的部分函数依赖，消除非主属性对码的传递函数依赖。
# 所有实体型均满足了3NF。非主属性之间不存在函数依赖关系。
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