import pymysql
def conn():
    con=pymysql.connect(host="localhost",port=3306,
                    db="xzs",user="root",
                    password="root",charset="utf8")
    return con
# 封装数据库查询操作
def query_db(sql):
    con=conn()
    # 创建游标
    cursor=con.cursor()
    # 利用游标执行sql
    cursor.execute(sql)
    # 获取执行的结果
    result=cursor.fetchall()
    # 关闭游标
    cursor.close()
    # 关闭连接
    con.close()
    return result

# 封装更改数据库操作
def chang_db(sql):
    con=conn()
    cursor=con.cursor()
    try:
        cursor.execute(sql)
        con.commit()
        # 如果成功就提交
    except:
        con.rollback()
        # 如果失败就回滚
    finally:
        cursor.close()
        con.close()

def check_user(name):
    rel=query_db("select * from t_user where name='{}'".format(name))
    return True if rel else False

def add_user(name,ps):
    chang_db("insert into t_user('user_name)','password') values ('{}','{}')".format(name,ps))

def del_user(name):
    chang_db("delete from t_user where name{}".format(name))
