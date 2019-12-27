# -*- coding:utf-8 -*-

import time,hashlib

# 生成唯一id
def create_id():
    m = hashlib.md5(str(time.clock()).encode('utf-8'))
    return m.hexdigest()