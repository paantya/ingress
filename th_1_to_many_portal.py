#!/usr/bin/env python3
import re
import io
input = open(file = 'in.txt', mode = 'r')

c = re.compile(r'([a-zA-ZА-Яа-я 0-9]+):.*=(\d*\.\d*)\,(\d*\.\d*)$')
#str = 'Шайба 1:ttps://www.ingress.com/intel?ll=59.865616,29.925498&z=16&pll=59.864079,29.92424'
#tuples = re.findall(c, str)
#print (tuples)
a = {'x':1.0, 'y':1.0, 'name':'a'}
b = {'x':2.0, 'y':2.0, 'name':'b'}

while ((b['x'] * b['y']) != 0):
    s = input.readline()
    tuples = re.findall(c, s)
    a['x'] = float(tuples[0][2])
    a['y'] = float(tuples[0][1])
    a['name'] = tuples[0][0]
    print ('Портал основа: ',a['name'],"X:",a['x'],"Y:",a['y'])
    while ((b['x'] * b['y']) != 0):
        s = input.readline()
        tuples = re.findall(c, s)
        b['x'] = float(tuples[0][2])
        b['y'] = float(tuples[0][1])
        b['name'] = tuples[0][0]
#        print (b['name'],"X:",b['x'],"Y:",b['y'])
        if ((b['x'] * b['y']) != 0):
            print ('Link: {0:7}--> {1:15} th(a)={2:18}'.format(a['name'],b['name'],(b['y']-a['y'])/(b['x']-a['x'])))
    print ('end.' )   
