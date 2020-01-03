#!/user/bin/env python
# -*- coding:utf-8 -*-
import MySQLdb
import MySQLdb.cursors
import redis
from code_file import MYSQLINFO,REDISINFO

# 数据库连接
class SqlConn(object):
    def __init__(self,host,port):
        self.host = host
        self.port = port

    def mysql_con(self,user,passwd,db):
        try:
            db_conn = MySQLdb.connect(host=self.host,
                                      port=self.port,
                                      user=user,
                                      passwd=passwd,
                                      db=db,
                                      cursorclass=MySQLdb.cursors.DictCursor)
            db_conn.autocommit(True)
            return db_conn
        except Exception as e:
            print "MySql连接失败,%s" % e
            return None

    def redis_con(self):
        try:
            POOL = redis.ConnectionPool(host=self.host,
                                        port=self.port,
                                        max_connections=1000)
            conn = redis.Redis(connection_pool=POOL)
            return conn
        except Exception as e:
            print "Redis连接失败,%s" % e
            return None

# Mysql配置
dbfirst = SqlConn(MYSQLINFO.HOST,MYSQLINFO.PORT)
db = dbfirst.mysql_con(MYSQLINFO.USER,MYSQLINFO.PASSWD,MYSQLINFO.DB)
# Redis配置
connfirst = SqlConn(REDISINFO.HOST,REDISINFO.PORT)
conn = connfirst.redis_con()