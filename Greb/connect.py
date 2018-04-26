import pymysql

def mysqlconnect(host='localhost',user='root',password='gj5846gj',db = 'greb',port= 3306):
    msyql = pymysql.Connect(host=host,user=user,password=password,db = db,port=port)
    return msyql
