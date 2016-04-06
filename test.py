#-*-coding:utf-8-*-

from keywords import MyCustomLibrary
a = MyCustomLibrary()

#a.post_json("http://192.168.100.210","/crash","D:\\DEV\\robot_framework\\Artisan\\artisan_interface_test\\artisan-interface-prod-linux\\jsondata\\ios\\demo\\ios_crash_armv7s.json")

#a.editJson("D:\\DEV\\robot_framework\\Artisan\\artisan_interface_test\\artisan-interface-prod-linux\\ArtisanCustomLibrary\\android_java_crash_replace.json",device_id="111",app_key="123",os_version="5.0")

#a.getUserTrace("android",7)

headers = {
                'Connection': 'keep-alive',
                'Token': '4debb41d64a043d8a887199943095ead444444',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:44.0) Gecko/20100101 Firefox/44.0'

           }


cookies = {
                'csrftoken': 'cursaAAPMeNsEnEGg9BhfrSbxtu16nna11111',
                'sessionid': '38bh6069nfwk8283r81h0j2yvwk1knw1111k'
          }

response=a.postFile('http://test-xxx.testbird.com:9527/webapi/application/version_mapping_file_upload/',headers,cookies,{'id':110},'/Users/OV/work/Crash-Analysis/test_crash_app/crash_app_sp5_20160222/mapping-new.txt','file','map.txt','text/plain')
print response