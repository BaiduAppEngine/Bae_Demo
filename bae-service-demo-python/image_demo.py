#-*- coding:utf-8 -*-

from bae_image.image import BaeImage

def test_img_transform():
    img = BaeImage("apikey", "secretkey", "image.duapp.com")

    ### ���ô�����ͼƬ
    img.setSource("http://www.baidu.com/img/baidu_sylogo1.gif")

    ### ����Ŀ��ͼƬ�ߴ�
    img.setZooming(BaeImage.ZOOMING_TYPE_PIXELS, 100000)

    ### ���òü�����
    img.setCropping(0, 0, 2000, 2000)

    ### ������ת�Ƕ�
    img.setRotation(10)

    ### ���ûҶȼ���
    img.setHue(100)

    ### ����ͼƬ��ʽ
    img.setTranscoding('gif')

    ### ִ��ͼƬ����
    ret = img.process()

    ### ����ͼƬbase64 encoded binary data
    body = ret['response_params']['image_data']

    import base64
    return base64.b64decode(body)

def test_img_annotate():
    img = BaeImage("apikey", "secretkey", "image.duapp.com")

    ### ���ô�����ͼƬ
    img.setSource("http://www.baidu.com/img/baidu_sylogo1.gif")

    ### ����ˮӡ����
    img.setAnnotateText("hello bae")

    ### ����������Ϣ
    img.setAnnotateFont(3, 25, '0000aa')

    ### ִ��ͼƬ����
    ret = img.process()

    ### ����ͼƬbase64 encoded binary data
    body = ret['response_params']['image_data']

    import base64
    return base64.b64decode(body)

def test_img_qrcode():
    img = BaeImage("apikey", "secretkey", "image.duapp.com")

    ### ���ö�ά���ı�
    img.setQRCodeText('bae')

    ### ���ñ�����ɫ
    img.setQRCodeBackground('ababab')

    ### ִ��ͼƬ����
    ret = img.process()

    ### ����ͼƬbase64 encoded binary data
    body = ret['response_params']['image_data']

    import base64
    return base64.b64decode(body)


def test_img_composite():
    img = BaeImage("apikey", "secretkey", "image.duapp.com")

    ### ���ô�����ͼƬ0
    img.setSource("http://www.baidu.com/img/baidu_sylogo1.gif")

    ### ���ô�����ͼƬ1
    img.setCompositeSource("http://www.baidu.com/img/baidu_sylogo1.gif")

    ### ����ͼƬ0��ê��
    img.setCompositeAnchor(0, 1)

    ### ����ͼƬ1��͸����
    img.setCompositeOpacity(0.3, 1)

    ### ���úϳɺ󻭲��ĳ���
    img.setCompositeCanvas(50, 50)

    ### ִ��ͼƬ����
    ret = img.process()

    ### ����ͼƬbase64 encoded binary data
    body = ret['response_params']['image_data']

    import base64
    return base64.b64decode(body)

def test_vcode():
    img = BaeImage("apikey", "secretkey", "image.duapp.com")

    ### ����һ����֤�룬����ֵ�пɻ�ȡ����vcode_str����֤��ͼƬ����imgurl
    gret = img.generateVCode(5, 3)

    ### ��֤�����Ƿ�ƥ�䣬����ֵ�пɻ�ȡ��֤���status����֤��Ϣstr_reason
    vret = img.verifyVCode("abcde", "secret")

    return str(gret) + str(vret)

def app(env, start_response):
    status = "200 OK"
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    body = []
    try:
        body.append("image transform result: [%s]"%test_img_transform()[0:64])
        body.append("image annotate result: [%s]"%test_img_annotate()[0:64])
        body.append("image qrcode result: [%s]"%test_img_qrcode()[0:64])
        body.append("image composite result: [%s]"%test_img_composite()[0:64])
        body.append("image vcode result: [%s]"%test_vcode())
        return '<br>'.join(body)
    except:
        return 'handle exceptions'

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)
