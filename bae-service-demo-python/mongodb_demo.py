#-*- coding:utf-8 -*-

def test_mongo():
    import pymongo
    db_name = "jdNoMPGWVKiHVybCNETJ"

    ### ����MongoDB����
    con = pymongo.Connection(host = "mongo.duapp.com", port = 8908)
    db = con[db_name]
    db.authenticate("apikey", "secretkey")

    ### �������ݵ�����test
    collection_name = 'test'
    db[collection_name].insert({"id":10, 'value':"test test"})
    
    ### ��ѯ����test
    cursor = db[collection_name].find()
    con.disconnect()
    return "select collection test %s"%str(cursor[0])

def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    try:
        return test_mongo()
    except:
        return 'handle exceptions'

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)