#存储功能测试文件
import pymysql




def find_name(id):
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.callproc("find_name", [id]) # 参数为存储过程名称和存储过程接收的参数
    db.commit()
    # 获取数据
    data = cursor.fetchall()
    
def insert_user(id,item):
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.callproc("insert_user", [id,item]) # 参数为存储过程名称和存储过程接收的参数
    db.commit()
    # 获取数据
    data = cursor.fetchall()

def delete_user(id):
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.callproc("delete_user", [id]) # 参数为存储过程名称和存储过程接收的参数
    db.commit()
    # 获取数据
    data = cursor.fetchall()

def update_sex(id,sex):
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.callproc("update_sex", [id,sex]) # 参数为存储过程名称和存储过程接收的参数
    db.commit()
    # 获取数据
    data = cursor.fetchall()





if __name__ == '__main__':
    db = pymysql.connect(host='localhost', port=3306, user='root',password='123456', db='zhihu')
    # find_name(1)
    # print(data1)
    # insert_user(18,1)
    # delete_user(15)
    update_sex(18,'女')


    
    # 关闭数据库连接
    db.close()