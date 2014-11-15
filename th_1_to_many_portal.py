#!/usr/bin/env python3
import re
import io
import math
input = open(file = 'in.txt', mode = 'r')

def portal_arctan(x1, y1):
    if ((x1 == a['x']) & (y1 == a['y'])):
        return 'NULL'
    if ((x1 - a['x']) <= 0):
        return math.degrees(math.pi + math.atan( (y1 - a['y']) / (x1 - a['x']) ))
    else:
        if ((y1 - a['y']) <= 0):
            return math.degrees(2 * math.pi + math.atan( (y1 - a['y']) / (x1 - a['x']) ))
        else:
            return math.degrees(math.atan( (y1 - a['y']) / (x1 - a['x']) ))

c = re.compile(r'([a-zA-ZА-Яа-я 0-9]*):(.*=(\d*\.\d*)\,(\d*\.\d*))$')
#str = 'Шайба 1:ttps://www.ingress.com/intel?ll=59.865616,29.925498&z=16&pll=59.864079,29.92424'
#tuples = re.findall(c, str)
#print (tuples)
a = {'x':1.0, 'y':1.0, 'name':'a', 'link':'ha'}
b = {'x':2.0, 'y':2.0, 'name':'b', 'link':'hb'}

while ((b['x'] * b['y']) != 0):
    s = input.readline()
    tuples = re.findall(c, s)
    a['x'] = float(tuples[0][3])
    a['y'] = float(tuples[0][2])
    a['name'] = tuples[0][0]
    a['link'] = tuples[0][1]
    print ('\nlinks emanating from: {0}({1},{2}).\n'.format(a['name'],a['x'],a['y']))
    print ('{0:18}>--->    {1:22}{2:13}'.format('from:','to portal:','Угол(в градусах):'))
    
    while ((b['x'] * b['y']) != 0):
        s = input.readline()
        tuples = re.findall(c, s)
        b['x'] = float(tuples[0][3])
        b['y'] = float(tuples[0][2])
        b['name'] = tuples[0][0]
        b['link'] = tuples[0][1]
#        print (b['name'],"X:",b['x'],"Y:",b['y'])
        if ((b['x'] * b['y']) != 0):
            print ('{0:15}(i)>--->(i) {1:21} ={2:13}'.format(a['name'],b['name'],portal_arctan(b['x'],b['y'])))
    print ('end.\n')   
