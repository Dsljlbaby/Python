# -*- coding: cp936 -*-
import urllib2
import json
from city import city
exit=False
while not exit:
   cityname = raw_input('������Ҫ��ѯ�ĳ��У�������q������ѯ��\n')
   if cityname=="q" or cityname=="Q":
        print('���β�ѯ��������ӭ�´�ʹ�ã�!')
        exit=True
   else:
       citycode = city.get(cityname)
       if citycode:
             try:
                url = ('http://www.weather.com.cn/adat/sk/%s.html'
                        % citycode)
                content1 = urllib2.urlopen(url).read()
                data1 = json.loads(content1)
                result1 = data1['weatherinfo']
                ur2 = ('http://www.weather.com.cn/data/cityinfo/%s.html'
                        % citycode)
                content2 = urllib2.urlopen(ur2).read()
                data2 = json.loads(content2)
                result2 = data2['weatherinfo']
                str_temp = ('The wind:%s\nThe wind scale:%s\nThe Humidity:%s\nTemperature:%s~%s\nThe weather:%s\nUpdate time:%s') % (
                     result1['WD'],
                     result1['WS'],
                     result1['SD'],
                     result2['temp1'],
                     result2['temp2'],
                     result2['weather'],
                     result1['time']
                 )
                print str_temp
             except:
                print '��ѯʧ��'
       else:
           print 'û���ҵ��ó���'

   

