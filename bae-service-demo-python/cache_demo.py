#-*- coding:utf-8 -*-

def test_cache():
    from bae_memcache.cache import BaeMemcache

    ### ����һ��cache
    cache = BaeMemcache("fUqxFBdrJSizQFSqxGUI", "cache.duapp.com:20243", "apikey", "secretkey")

    body = []
    ### ���һ��key��value��
    if cache.set('key', 'value'):
        body.append("set key => value success!")

    ### ��ȡkey��Ӧ��value
    body.append("get %s success!"%cache.get('key'))
    return body

def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    try:
        return '<br>'.join(test_cache())
    except:
        return 'handle exceptions'
    

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)
