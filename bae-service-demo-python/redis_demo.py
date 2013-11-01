#-*- coding:utf-8 -*-

def test_redis():
    import redis
    rd_name = "HsXNSJuTYsVJIJdeGnvY"
    myauth = "%s-%s-%s"%("apikey", "secretkey", rd_name)

    ### ����redis����
    r = redis.Redis(host = "redis.duapp.com", port = 80, password = myauth)

    ### ���и���redis��������set��get
    r.set("foo", "bar")
    return "get foo=> %s success!"%r.get("foo")


def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    try:
        return test_redis()
    except:
        return 'handle exception'
 
from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)