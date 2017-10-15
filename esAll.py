# -*- coding: utf-8 -*-

from datetime import datetime
from elasticsearch import Elasticsearch

# 預設連線至 ElasticSearch Server Port 9200,  localhost:9200
es = Elasticsearch()

# 加入資料進行索引, 自己設定  id = 1
# http://localhost:9200/social/tweet/1
setdata = es.index(index="social", doc_type="tweet", id=1, body={"content": "aa1","user":{"name":"xx","id":670085},"tags":["demo","test"], "timestamp": datetime.now()})
setdata = es.index(index="social", doc_type="tweet", id=2, body={"content": "aa2","user":{"name":"小xx王","id":670086},"tags":["demo","test2"], "timestamp": datetime.now()})
setdata = es.index(index="social", doc_type="tweet", id=3, body={"content": "aa3","user":{"name":"老xxx王","id":670085},"tags":["demo","test"], "timestamp": datetime.now()})
setdata = es.index(index="social", doc_type="tweet", id=4, body={"content": "aa2","user":{"name":"小xx王","id":670086},"tags":["demo","test2"], "timestamp": datetime.now()})
setdata = es.index(index="social", doc_type="tweet", id=5, body={"content": "aa2","user":{"name":"老xx王","id":670085},"tags":["demo","test"], "timestamp": datetime.now()})
setdata = es.index(index="social", doc_type="tweet", id=6, body={"content": "大家好2","user":{"name":"小xxx王","id":670086},"tags":["demo","test2"], "timestamp": datetime.now()})

#  取得 id=1 資料
getdata = es.get(index="social", doc_type="tweet", id=1)['_source']
print (getdata)


es.indices.refresh(index="social")
# Search
qdoc = {
 "query": {
  "match" : {
   "tags" : "demo"
  }
 }
}

getdata = es.search(index="social", body=qdoc)
#print type(getdata)
print("Got %d Hits:" % getdata['hits']['total'])
for hit in getdata['hits']['hits']:
    print("%(content)s %(user)s: %(tags)s" % hit["_source"])