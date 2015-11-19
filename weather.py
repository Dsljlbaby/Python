# -*- coding: cp936 -*-
import urllib2
import json
from city import city
exit=False
while not exit:
   cityname = raw_input('请输入要查询的城市:（输入q结束查询）\n')
   if cityname=="q" or cityname=="Q":
        print('本次查询结束，欢迎下次使用！!')
        exit=True
   else:
       citycode = city.get(cityname)
       if citycode:
             try:
                url = ('http://www.weather.com.cn/data/cityinfo/%s.html'
                        % citycode)
                content = urllib2.urlopen(url).read()
                data = json.loads(content)
                result = data['weatherinfo']
                str_temp = ('%s\n%s ~ %s') % (
                     result['weather'],
                     result['temp1'],
                     result['temp2']
                 )
                print str_temp
             except:
                print '查询失败'
       else:
           print '没有找到该城市'

