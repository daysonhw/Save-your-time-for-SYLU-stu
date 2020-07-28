#cookie = {'CenterSoftWeb': '###########################################################################################################################################################################################################################################################################################################################################################################################'}##############################################
rawBase64 = ''
webhook = ''
NotifyAPI = ''

# Sent mail if success?
SENT = False

# Mail Service with resent feature
def sentMail(title, content, *sub):
    value = {'value1': title, 'value2': content}
    if sub:
        return requests.post(webhook, data=value).status_code
    mail = requests.post(webhook, data=value)
    if mail.status_code != 200:
        times = 10
        while times:
            time.sleep(60)
            if sentMail(title, content, True) == 200:
                return None
            times -= 1
        return False

def sentNotify(title, content, *sub):
    value = {'value1': title, 'value2': content}
    if sub:
        pass
        

import requests, os, time, getpass, random, platform, base64, traceback
# import execjs, re

# Parameters
osSys = platform.system()
url = 'http://xg.sylu.edu.cn/SPCP/Web'
url1 = 'http://xg.sylu.edu.cn/SPCP/Web/Report/Index'
url2 = 'http://xg.sylu.edu.cn/SPCP/Web/Temperature/StuTemperatureInfo'

#init
path = os.path.realpath(__file__)
session = requests.session()
try:
    # Store Cookie in program file
    if cookie:
        session.cookies.update(cookie)
    else:
        print('You need a cookie to run this')
        user = input('Enter your username:')
        passwd = getpass.getpass()
        data = {'StuLoginMode': '1', 'txtUid': user, 'txtPwd': passwd}
        res = session.post(url, data=data)
        f = open(path,'r+')
        f.write('cookie = ' + str(session.cookies.get_dict()))
        print('Cookies wrote')

    # 验证登陆有效性 更新cookie
    vail = session.get(url)
    if not '开启中' in vail.text:
        print("Couldn't Login at Stage 1")
        # Using Drawin AppleScript
        if osSys == 'Darwin':
            os.system('''osascript -e 'display dialog "Could not Login at Stage 1, updating Cookie"' ''')
        else: exit()
    if cookie != session.cookies.get_dict():
        f = open(path,'r+')
        f.write('cookie = ' + str(session.cookies.get_dict()))
        print('Cookies updated')


    # 信息填报
    web1 = session.get(url1)
    if not '当前采集日期已登记' in web1.text:
        raw = base64.b64decode(rawBase64).decode('utf-8')
        raw = raw.split('&')
        data1 = {}
        for item in raw:
            item = item.split('=')
            data1[item[0]] =item[1]
        web1 = session.post(url1,data=data1)
        #vaildate
        if '提交成功' in web1.text:
            result1 = True
        else: result1 = False
    else: result1 = True


    # 体温填报
    web2 = session.get(url2)
    if not '今天填报次数已完成' in web2.text:
        temp2 = int(random.uniform(2,9))
        time2 = int(random.uniform(1,59))
        data2 = {'TimeNowHour':'8', 'TimeNowMinute':time2, 'Temper1':'36', 'Temper2':temp2}
        web2 = session.post(url2, data=data2)
        #vaildate
        if '填报成功' in web2.text:
            result2 = True
        else: result2 = False
    else: result2 = True
except :
    sentMail('ERROR', traceback.print_exc())

# Final vaildation
if result2 and result1 :
    print('Success')
    if SENT:
        sentMail('[AUTO] Success!', time.ctime())
else : 
    print('Something went wrong', str(result1), str(result2))
    sentMail('[ERROR] FORM AUTOSCRTIPT 1', str(result1) + str(result2))
if osSys == 'Darwin' and result1 and result2:
    os.system('''osascript -e 'display notification "Task Complete without error"' ''')
else:
    os.system('''osascript -e 'display dialog "error"''')
