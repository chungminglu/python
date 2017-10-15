# -*- coding: utf-8 -*-
from datetime import datetime
from elasticsearch import Elasticsearch
import json
import requests

# es = Elasticsearch()
es = Elasticsearch([{'host':'localhost','port':9200}])

# 加入資料進行索引, 自己設定  id = 1
# http://localhost:9200/social/tweet/1
setdata = es.index(index="social", doc_type="tweet", id=11, body={"content": "aa1","user":{"name":"xx","id":670085},"tags":["demo","test"], "timestamp": datetime.now()})
setdata = es.index(index="social", doc_type="tweet", id=12, body={"content": "aa2","user":{"name":"小xx王","id":670086},"tags":["demo","test2"], "timestamp": datetime.now()})
setdata = es.index(index="social", doc_type="tweet", id=13, body={"content": "aa3","user":{"name":"老xxx王","id":670085},"tags":["demo","test"], "timestamp": datetime.now()})
setdata = es.index(index="social", doc_type="tweet", id=14, body={"content": "aa2","user":{"name":"小xx王","id":670086},"tags":["demo","test2"], "timestamp": datetime.now()})
setdata = es.index(index="social", doc_type="tweet", id=15, body={"content": "aa2","user":{"name":"老xx王","id":670085},"tags":["demo","test"], "timestamp": datetime.now()})
setdata = es.index(index="social", doc_type="tweet", id=16, body={"content": "大家好2","user":{"name":"小xxx王","id":670086},"tags":["demo","test2"], "timestamp": datetime.now()})

r = requests.get('http://localhost:9200')
i = 1
while r.status_code == 200:
    r = requests.get('http://swapi.co/api/people/'+ str(i))
    es.index(index='social',doc_type='tweet',id=i,body=json.loads(r.content))
    i=i+1
print(i)