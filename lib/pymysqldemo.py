import pymysql
try:
    conn=pymysql.connect(host="localhost",port=3306,
                    db="xzs",user="root",
                    password="root",charset="utf8")
    cursor=con.cursor()
    cursor.execute("select * from t_user where id=1")
    data=cursor.fetchone()
    print(data)
except Exception as e:
    print("出错了!错误信息为:{}".format(e))
finally:
    cursor.close()
    con.close()