#!/usr/bin/env python3
import re
import io
input = open(file = 'in.txt', mode = 'r')

c = re.compile(r'([a-zA-ZА-Яа-я 0-9]+):(.*=(\d*\.\d*)\,(\d*\.\d*))$')
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
    print ('\n\nПортал основа: ',)
    print (a['name'],"X:",a['x'],"Y:",a['y'],'\n')
    while ((b['x'] * b['y']) != 0):
        s = input.readline()
        tuples = re.findall(c, s)
        b['x'] = float(tuples[0][3])
        b['y'] = float(tuples[0][2])
        b['name'] = tuples[0][0]
        b['link'] = tuples[0][1]
#        print (b['name'],"X:",b['x'],"Y:",b['y'])
        if ((b['x'] * b['y']) != 0):
            print ('Link: {0:7}--> {1:15} th(a)={2:18}'.format(a['name'],b['name'],(b['y']-a['y'])/(b['x']-a['x'])))
    print ('end.\n' )   
