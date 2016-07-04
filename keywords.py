#!/usr/bin/python
# -*-coding:utf-8-*-

import httplib
import json
import requests
import sys
import time
import urllib2

# 将编码设置为utf-8，防止RF报编码错误

reload(sys)
sys.setdefaultencoding('utf8')


class MyCustomLibrary():
    """
    这个是daize的一个自定义库,bug挺多,够用就行,请见谅
    """

    def __init__(self):
        return None

    def postJson(self, jsonfile, url, url_dir="/crash", ):
        """
        使用urllib2标准库发送请求
        `url` 不包含路径的目标地址
        `jsonfile`:json数据文件
        `url_dir`:目标路径,没有路径请一定输入"/",否则默认是'/crash'
        """
        report = open(jsonfile, "r")
        report = report.read()
        print "data:" + report
        print "url:" + url + url_dir
        req = urllib2.Request(url + url_dir, data=report)
        response = urllib2.urlopen(req, timeout=10)
        print response.read() + "success"

    def sendCrash(self, jsonfile):
        """
        Waring!!!
        不建议使用,功能不完善!建议使用post_json关键字
        该关键字使用httplib发送一条crash日志，该关键字需要传入一个json文件
        """
        for i in range(1):
            # 获取当前路径
            # dir = sys.path[0]
            report = open(jsonfile)
            conn = httplib.HTTPConnection("123.59.132.227", 8080)
            headers = {
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'X-Requested-With': 'XMLHttpRequest',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-cn',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Connection': 'keep-alive',

            }
            httplib.request(method="post", url="/crash", body=report, headers=headers)
            response = conn.getresponse()
            print response.read()
            print response.status, response.reason
            conn.close()

    def postFile(
            self,
            url,
            headers=None,
            cookies=None,
            body_data=None,
            filepath=None,
            name=None,
            filename=None,
            contentType=None):
        """使用Content-Type为'multipart/form-data'上传文件
        :param url:接口地址,含路径
        :param headers:headers
        :param cookies:cookies
        :param body_data:跟随请求发送的参数,字典形式
        :param filepath:待上传的文件路径
        :param name:文件的key
        :param filename:文件名称
        :param contentType:该文件的内容类型
        :return:
        """

        files = {name: (filename, open(filepath, 'rb'), contentType)}
        request_data = body_data

        r = requests.post(url, cookies=cookies, headers=headers, data=request_data, files=files)
        status_code = r.status_code
        reponse = r.json()
        # headers=r.request.headers

        return status_code, reponse

    def editJson(self, inputJsonFile, **keyValue):
        """

        :param inputJsonFile: 待替换文件
        :param keyValue: 接受多对待替换的k-v,v为新值
        :return:
        """
        # 如果要输出一个替换后的文件，加入一个outputfile传参，然后再写到该文件即可
        fin = open(inputJsonFile, 'r')  # 打开原始文件
        for key in keyValue:
            print "will replace:", key
            for eachLine in fin:
                line = eachLine.strip().decode('utf-8')  # 去除每行首位可能的空格，并且转为Unicode进行处理
                line = line.strip(',')  # 去除Json文件每行大括号后的逗号
                js = None
                try:
                    js = json.loads(line)  # 加载Json文件
                except Exception, e:
                    print 'bad line'
                    print e
                    continue
                if js. has_key(key):  # 如果找到了key，直接替换。否则在第二层json中找
                    js[key] = keyValue[key]  # 对需要修改的项进行修改
                # print isinstance(js["event_info"],dict)
                else:
                    for i in js:
                        if isinstance(js[i], dict):  # 判断是否是字典
                            if js[i]. has_key(key):
                                js[i][key] = keyValue[key]
                            else:  # 判断第三层
                                for j in js[i]:
                                    if isinstance(js[i][j], dict):
                                        if js[i][j]. has_key(key):
                                            js[i][j][key] = keyValue[key]
                outStr = json.dumps(js, ensure_ascii=False, separators=(',', ':'))  # 处理完之后重新转为Json格式，并在行尾加上一个逗号，并去除空格
                fout = open(inputJsonFile, 'w')  # 重新以写权限打开原文件
                fout.write(outStr.strip().encode('utf-8'))  # 写回到这个/新的文件中去
                fout.close()  # 关闭
                fin = open(inputJsonFile, 'r')  # 重新打开这个已经替换过一次的输出文件
        fin.close()  # 关闭文件
        fout.close()

    '''
        def getValueFromDictByKey(self, dictionary, key):
        """
        从一个字典中根据key获取其value,返回一个所有符合条件的value列表
        :param dictionary:待查找的字典
        :param key:目标key

        """
        value=[]
        js=dictionary
        #try:
        #     js = json.loads(dictionary)  # 加载Json文件
        #except Exception, e:
        #    print 'bad line'
        #    print e
        if js.has_key(key):
            value.append(js[key])
        for i in js:
            if isinstance(js[i],dict):
                if js[i].has_key(key):
                    value.append(js[i][key])
                for k in js[i]:
                    if isinstance(js[i][k],list):
                        for j in range(len(js[i][k])) :
                            if isinstance(js[i][k],dict):
                                if js[i][k][j].has_key(key):
                                    value.append(js[i][k][j][key])
            if isinstance(js[i],list):
                for j in range(len(js[i])):
                    if isinstance(js[i][j],dict):
                        if js[i][j].has_key(key):
                            value.append(js[i][j][key])
        return value
    '''

    def __getvalue__(self, dictionary, key):
        for k in dictionary:
            # print k
            if k == key:
                self.value.append(dictionary[k])
            if isinstance(dictionary[k], dict):
                self.__getvalue__(dictionary[k], key)
            if isinstance(dictionary[k], list):
                for i in range(len(dictionary[k])):
                    if isinstance(dictionary[k][i], dict):
                        self.__getvalue__(dictionary[k][i], key)


    def getValueFromDictByKey(self, dictionary, key):
        """
        从一个字典中根据key获取其value,返回一个所有符合条件的value列表
        :param dictionary:待查找的字典
        :param key:目标key

        """
        self.value = []
        self.__getvalue__(dictionary, key)
        return self.value

    def randomStack(self, line=100, activity='LoginActivity'):
        """artisan专用,可无视
        :param line:
        :param activity:
        :return:
        """
        crash_stack = "java.lang.IndexOutOfBoundsException: Invalid index 0, size is 0\n\tat java.util.ArrayList.throwIndexOutOfBoundsException(ArrayList.java:255)\n\tat java.util.ArrayList.get(ArrayList.java:308)\n\tat com.artisan.demo.android.%s$1.onClick(%s.java:%s)\n\tat android.view.View.performClick(View.java:4401)\n\tat android.view.View$PerformClick.run(View.java:18184)\n\tat android.os.Handler.handleCallback(Handler.java:730)\n\tat android.os.Handler.dispatchMessage(Handler.java:92)\n\tat android.os.Looper.loop(Looper.java:150)\n\tat android.app.ActivityThread.main(ActivityThread.java:5390)\n\tat java.lang.reflect.Method.invokeNative(Native Method)\n\tat java.lang.reflect.Method.invoke(Method.java:525)\n\tat com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:737)\n\tat com.android.internal.os.ZygoteInit.main(ZygoteInit.java:553)\n\tat dalvik.system.NativeStart.main(Native Method)\n" % (
        activity, activity, line)
        return crash_stack

    def getUserTrace(self, os, activity_index=0):
        """
        activity_index=0,1,2;分别对应：mainactivity，activity1，activity2
        """
        utcTime = int(time.time() * 1000)
        # print utcTime
        if os == 'ios':
            trace = [{"event": "Session Start", "time": utcTime - 25000},
                     {"event": "UINavigationController#viewWillAppear", "time": utcTime - 22000},
                     {"event": "ViewController#viewWillAppear", "time": utcTime - 20000}]
        elif os == 'android' and 0 <= activity_index <= 2:
            trace = [{"event": "Session Start", "time": utcTime - 25000},
                     {"event": "MainActivity#OnCreate", "time": utcTime - 22000},
                     {"event": "MainActivity#OnResume", "time": utcTime - 20000}]
        elif os == 'android' and 3 <= activity_index <= 3:
            trace = [{"event": "Session Start", "time": utcTime - 25000},
                     {"event": "MainActivity#OnCreate", "time": utcTime - 122000},
                     {"event": "MainActivity#OnResume", "time": utcTime - 20000},
                     {"event": "Activity1#OnCreate", "time": utcTime - 19000},
                     {"event": "Activity1#OnResume", "time": utcTime - 18000}]
        elif os == 'android' and 4 <= activity_index <= 5:
            trace = [{"event": "Session Start", "time": utcTime - 25000},
                     {"event": "MainActivity#OnCreate", "time": utcTime - 22000},
                     {"event": "MainActivity#OnResume", "time": utcTime - 20000},
                     {"event": "Activity2#OnCreate", "time": utcTime - 19000},
                     {"event": "Activity2#OnResume", "time": utcTime - 18000}]
        else:
            trace = [{"event": "Session Start", "time": utcTime - 25000},
                     {"event": "MainActivity#OnCreate", "time": utcTime - 22000},
                     {"event": "MainActivity#OnResume", "time": utcTime - 20000}]
        # print trace
        return trace
