import json
import time, datetime
import urllib.request

# 微信统一配置及数据
wx_app_id = 'wx6081c1591dc52981'
wx_app_secret = '094ad685a386a5f42fcadd0ff293eea9'
wx_data = {}


def fetch_session(code):
    """微信登录"""

    res = urllib.request.urlopen(
        'https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=%s' % (
            wx_app_id, wx_app_secret, code, 'authorization_code'
        ))

    json_result = res.read().decode('utf-8')
    print(json_result)
    return json.loads(json_result)


def fetch_access_token():
    """请求访问令牌"""

    res = urllib.request.urlopen(
        'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (
            wx_app_id, wx_app_secret
        ))

    json_result = res.read().decode('utf-8')
    print(json_result)
    return json.loads(json_result)


def get_access_token():
    """从本地存储中获取令牌，如果本地存储没有或令牌超时则重新请求令牌"""

    if not ('access_token' in wx_data) or wx_data['access_token']['expires'] <= int(time.time()):
        wx_data['access_token'] = fetch_access_token()
        wx_data['access_token']['expires'] = int(time.time()) + wx_data['access_token']['expires_in']
    return wx_data['access_token']['access_token']


def send_template_message(to_user, template_id, form_id, data, page='', emphasis_keyword=''):
    """发送模板消息"""
    ac = get_access_token()
    json_data = json.dumps({
            'touser': to_user,
            'template_id': template_id,
            'page': page,
            'form_id': form_id,
            'data': data,
            'emphasis_keyword': emphasis_keyword
        })
    bytes_data = bytes(json_data, 'utf8')

    res = urllib.request.urlopen(
        'https://api.weixin.qq.com/cgi-bin/message/wxopen/template/send?access_token=%s' % (ac,),
        data=bytes_data
    )

    json_result = res.read().decode('utf-8')
    print(json_result)
    return json.loads(json_result)


def send_feedback_template_message(to_user, form_id, reply):
    """意见反馈处理结果消息"""

    template_id = 'UZ_Th-i9HVDCyfxRbUvfI9VswnIxNyzxsMfoQFMlP1E'
    page = '/pages/index/index?go=feedback'
    data = {
        'keyword1': {
            'value': reply
        },
        'keyword2': {
            'value': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    }
    return send_template_message(to_user, template_id, form_id, data, page)
