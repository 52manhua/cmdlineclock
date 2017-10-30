#/usr/bin/env python
#encoding=utf-8
#coding:utf8
# Filename : test.py
# mod sixinice

from __future__ import division
from time import sleep
import sys
import os

sa = sys.argv
lsa = len(sys.argv)
if lsa == 2:
	try:
		my_minutes = int(sa[1])
	except ValueError:
		print "Invalid numeric value (%s) for minutes" % sa[1]
		print "Should be an integer >= 0"
else:
	my_minutes = input("倒计时时间（分钟）")

try:
  my_minutes = int(my_minutes)
except ValueError:
  print "Invalid numeric value (%s) for minutes " % my_minutes
  print "Should be an integer >= 0"
  sys.exit(1)

seconds = my_minutes *60;

def progress_show(val):
    bar_length=20
    percent=0
    for per in xrange(0, val):
        hashes = '#' * int(per/val * bar_length)
        spaces = ' ' * (bar_length - len(hashes))
	percent = per/val * 100
        sys.stdout.write("\rPercent: [%s] %d%%"%(hashes + spaces, percent))
        sys.stdout.flush()
        sleep(1)

try:  
	if my_minutes > 0 :
		print "Sleeping " + str(my_minutes) + " 分钟"
		progress_show(seconds)
		print("!!时间已到!!");
		os.system("BB")
except KeyboardInterrupt:
	print "==键盘中断=="
	sys.exit(1)