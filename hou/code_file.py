#!/usr/bin/python
# -*- coding:utf-8 -*-

class ERRORCODE(object):
    SUCCESS    =        "0000"
    ERROR_LOGIN =       "0001"
    ERROR_REGISTER =    "0002"
    ERROR_ADD =         "0003"
    ERROR_MODIFY =      "0004"
    ERROR_DELETE =      "0005"
    ERROR_QUERY =       "0006"
    ERROR_WEBSERVER =   "0507"


class ERRORMSG(object):
    SUCCESS =               "success"
    ERROR_UPLOAD =          "upload error"
    ERROR_DOWNLOAD =        "download error"
    ERROR_ADD =             "add error"
    ERROR_DELETE =          "delete error"
    ERROR_MODIFY =          "modify error"
    ERROR_PASSWORD =        "password error"
    ERROR_USERNAME =        "username error"
    ERROR_UPDATE =          "update error"
    ERROR_REPEAT_NAME =     "repeat name error"
    ERROR_INSERT_DB =       "insert database error"
    ERROR_NOT_EXIST =       "file dont exist"
    ERROR_BACKMSG =         "msg error"
    ERROR_WEBSERVER =       "webserver error"
    ERROR_GET_DATA =        "getdata error"
    ERROR_PARAMETER_ERROR = u"参数错误"
    ERROR_CHECK_ERROR =     "check error"
    ERROR_NO_MSG =          "no msg"
    ERROR_FORMAT =          "format error"
    ERROR_ENTRUST =         "entrust error"
    ERROR_INPUT_ERROR=      "input error"
    ERROR_ORDER_ID_ERROR=   "order id error"
    ERROR_NO_PARAM=         "no param "
    ERROR_LOGIN=            "session failure Please login "
    ERROR_DATE_ERROR =      u"日期不能小于当天时间"
    ERROR_DB_ERROR =        u"数据库错误"

