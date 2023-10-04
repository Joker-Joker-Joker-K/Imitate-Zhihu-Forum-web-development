import web
#https://blog.csdn.net/freeking101/article/details/53020865

urls = (
    #登录
    '/','login',
    #首页
    '/index','index',
    #用户信息管理
    '/users','users',
    '/insert','insert',
    '/drop','drop',
    '/upgate','upgate',
    '/select','select',
    '/show','show',
)

app = web.application(urls, globals())
render = web.template.render('templates/',cache = False )
db = web.database(dbn='mysql', host="localhost", port=3306,db='zhihu', user='root', pw='123456')

# 表示层
class login:
    def GET(self):
        return render.login() 


class index:
    def GET(self):
        return render.app() 


class users:
    def GET(self):
        return render.users() 


# 业务逻辑层 /数据访问层
class insert:
    def POST(self):
        use=web.input()
        n = db.insert('users', 用户ID=use.用户ID, 用户名=use.用户名,用户介绍=use.用户介绍)
            
        return render.insert() 
    
class drop:

    def drop(self):
        # name = "Lisa"
        return render.drop() 

class upgate:

    def GET(self):
        # name = "Lisa"
        return render.upgate()

class select:

    def GET(self):
        # name = "Lisa"
        return render.select() 
    

    
class show:

    def GET(self):
        # name = "Lisa"
        return render.show() 





if __name__ == "__main__":
    #web.internalerror = web.debugerror
    app.run()

