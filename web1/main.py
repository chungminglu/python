import os.path
import random
import json
import requests
import datetime
import pymysql
import tornado.httpserver,tornado.ioloop,tornado.options,tornado.web
from pymongo import MongoClient
from tornado.options import define, options

define("port", default=7777, help="run on the given port", type=int)

class index(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")

class login(tornado.web.RequestHandler):
    def post(self):
        user_name = self.get_argument("username")
        user_email = self.get_argument("email")
        user_website = self.get_argument("website")
        user_language = self.get_argument("language")
        self.render("auth.html",username=user_name,email=user_email,website=user_website,language=user_language)        

class line(tornado.web.RequestHandler):
    def get(self):
        self.render("line.html")

class model(tornado.web.RequestHandler):
    def get(self):
        self.render("model.html")

class power(tornado.web.RequestHandler):
    def get(self):
        self.render("power.html")   

class bars(tornado.web.RequestHandler):
    def get(self):
        self.render("bars.html")       

class table(tornado.web.RequestHandler):
    def get(self):
        # self.render("table.html") 
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='ooxx@748', db='iii')
        cur = conn.cursor()
        cur.execute("SELECT typeid,lat,lng FROM test where typeid='102' limit 10")   
        rows = cur.fetchall()
        # for xx in rows:
        #     print xx
        self.render("table.html",dbrow=rows)                           
        
class test(tornado.web.RequestHandler):
    def get(self):
        conn = MongoClient("app.vietthuan.com",27777)
        db = conn.hsiung
        db.authenticate("hsiung","",source="admin")
        mdb = db.my_collection.find({})
            
        self.render('test.html',
                    header_text = "OOOO1",
                    footer_text = mdb[0])
    
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "http://app.vietthuan.com")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS") 

        conn = MongoClient("app.vietthuan.com",27777)
        db = conn.hsiung
        db.authenticate("hsiung","",source="admin")      
		
        username = self.get_argument("username")
        password = self.get_argument("password")
        imei = self.get_argument("imei")
        lat = self.get_argument("lat")
        lon = self.get_argument("lon")
        alt = self.get_argument("alt")
        db.hsiung.insert({"thisTime":str(datetime.datetime.utcnow()),"username":username,"password":password,"imei":imei,"lat":lat,"lon":lon,"alt":alt})
        self.write(username +"<br/>"+password+"<br/>"+imei+"<br/>"+lat+"<br/>"+lon+"<br/>"+alt)

class countMember(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Access-Control-Allow-Origin", "http://app.vietthuan.com")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS") 

        conn = MongoClient("app.vietthuan.com",27777)
        db = conn.hsiung
        db.authenticate("hsiung","",source="admin")       
        members = str(db.hsiung.find({}).count())
        self.write(members) 

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', index),
                  (r'/login',login),
                  (r'/test',test),                  
                  (r'/line',line),
		          (r'/countMember',countMember),
                  (r'/power',power),
                  (r'/bars',bars),
                  (r'/table',table)                  
                  ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
