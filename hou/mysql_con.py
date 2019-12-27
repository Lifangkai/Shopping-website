#!/user/bin/env python
# -*- coding:utf-8 -*-
import MySQLdb
import MySQLdb.cursors

db = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', db='shop_management',
                     cursorclass=MySQLdb.cursors.DictCursor)
db.autocommit(True)
