#!/usr/bin/env python
# -*- coding:utf-8 -*-
NAVACTIVE = {}

COMMONINFO = {'navactive':NAVACTIVE,'menuinfo' : [], 'navmenu':[]}

DB_USERNAME = 'root'
DB_PASSWORD = 'root'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'pdcenter1'

DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False